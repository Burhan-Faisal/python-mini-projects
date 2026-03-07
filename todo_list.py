import termcolor,json

pending_tasks=[]
completed_tasks=[]
todo_list_menu=[
    "View Pending Tasks",
    "Add  a Task",
    "Remove a Task",
    "Mark tasks as completed",
    "View Completed Tasks",
    "Change Category",
    "Add Another Category",
    "Exit"
]
categories={

}

choices=[1,2,3,4,5,6,7,8]
Task_file="todo_list.json"

def view_comp_tasks(category):
    completed=categories[category]['Completed Tasks']
    if completed:
        for index,task in enumerate(completed,start=1):
            print(index,'. ',task)
        return True
    else:
        print("No tasks in the list.")
        return False


def view_pending_tasks(category):
    pending=categories[category]['Pending Tasks']
    if pending:
        for index,task in enumerate(pending,start=1):
            print(index,'. ',task)
        return True
    else:
        print("No tasks in the list.")
        return False

def remove_task(category):
        if(view_pending_tasks(category)):
            while True:
                try:
                    task_no=int(input("Enter the task number you want to remove: "))

                    if 1<=task_no<=len(categories[category]['Pending Tasks']):
                        categories[category]['Pending Tasks'].pop(task_no-1)
                        save_tasks()
                        print('Task no.',termcolor.colored(task_no,'red'),'is removed')
                        break
                    else:
                        raise ValueError("Invalid Task Number")
                except ValueError as e:
                    print(e)


def choose_category():
    if categories:
        for index,category_item in enumerate(categories,start=1):
            print(f"{index}.{category_item}")
    else:
        termcolor.cprint("Starting Fresh No Category yet..",'magenta')
        return add_category()
    while True:
            category=input("Enter your Category Name: ").strip().upper()
            if category in categories:
                return category
            else:
                print("Invalid Category Name..")

def mark_as_completed(category):
    if(view_pending_tasks(category)):
        while True:
            try:
                task_no=int(input("Enter the task no. that is completed: "))
                completed=categories[category]['Completed Tasks']
                if 1<=task_no<=len(categories[category]['Pending Tasks']):
                    completed.append(categories[category]['Pending Tasks'].pop(task_no-1))
                    save_tasks()
                    print('Task no.',termcolor.colored(task_no,'blue'),'is marked as completed')
                    break
                else:
                    raise ValueError("Invalid Task Number")
            except ValueError as e:
                    print(e)

def save_tasks():
    try:
        with open(Task_file,'w') as f:
            json.dump(categories,f,indent=4)
    except Exception as e:
        termcolor.cprint("Error in saving tasks",'red')


def load_tasks():
    try:
        global categories
        with open(Task_file,'r') as f:
            categories=json.load(f)
            termcolor.cprint("Successfully Loaded Pending and Completed tasks from previous session", 'yellow',attrs=['bold'])
    except Exception:
        termcolor.cprint("No previous session",'red')
        categories={}


def add_task(category): 
    while True:
        task=input("Add a task: ").strip()
        if len(task) != 0:
           categories[category]['Pending Tasks'].append(task)
           save_tasks()
           termcolor.cprint("Task Added.",'green')
           break
        else:
            print('Invalid task!')


def add_category():
    while True:
        category_name=input("Enter Your Category Name for your todos': ").strip().upper()
        if category_name:
            categories.update({category_name:{   
                'Pending Tasks':[],
                'Completed Tasks':[]
            }})
            termcolor.cprint("Category Added..",'green')
            return category_name
        else:
            termcolor.cprint("Invalid Category Name",'red')
        

def main():
    load_tasks()
    category=choose_category()
    print("Todo-List Menu :")
    for index,list in enumerate(todo_list_menu,start=1):
        print(index,'. ',list)
    while True:
        try:
            choice=int(input("Enter Your Choice:").strip())
            if choice in choices:
                if choice == 1:
                    view_pending_tasks(category)
                elif choice==2:
                    add_task(category)
                elif choice==3:
                    remove_task(category)
                elif choice==4:
                    mark_as_completed(category)
                elif choice==5:
                    view_comp_tasks(category)
                elif choice==6:
                    category=choose_category()
                elif choice==7:
                    add_category()
                else:
                    save_tasks()
                    exit()
            else:
                raise ValueError
        except ValueError:
            print("Enter a valid choice")

if __name__=='__main__':
    main()