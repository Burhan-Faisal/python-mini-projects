
import termcolor,json,os
pending_tasks=[]
completed_tasks=[]
todo_list_menu=[
    "View Pending Tasks",
    "Add  a Task",
    "Remove a Task",
    "Mark tasks as completed",
    "View Completed Tasks",
    "Exit"
]


choices=[1,2,3,4,5,6]
Task_file="todo_list.json"

def view_comp_tasks():
    if completed_tasks:
        for index,task in enumerate(completed_tasks,start=1):
            print(index,'. ',task)
        return True
    else:
        print("No tasks in the list.")
        return False
    

def view_tasks():
    if pending_tasks:
        for index,task in enumerate(pending_tasks,start=1):
            print(index,'. ',task)
        return True
    else:
        print("No tasks in the list.")
        return False

def remove_task():
        if(view_tasks()):
            while True:
                try:
                    task_no=int(input("Enter the task number you want to remove: "))

                    if 1<=task_no<=len(pending_tasks):
                        pending_tasks.pop(task_no-1)
                        save_tasks()
                        print('Task no.',termcolor.colored(task_no,'red'),'is removed')
                        break
                    else:
                        raise ValueError("Invalid Task Number")
                except ValueError as e:
                    print(e)


def mark_as_completed():
    if(view_tasks()):
        while True:
            try:
                task_no=int(input("Enter the task no. that is completed: "))
                if 1<=task_no<=len(pending_tasks):
                    completed_tasks.append(pending_tasks.pop(task_no-1))
                    save_tasks()
                    print('Task no.',termcolor.colored(task_no,'blue'),'is marked as completed')
                    break
                else:
                    raise ValueError("Invalid Task Number")
            except ValueError as e:
                    print(e)

def save_tasks():
    try:
        data = {
            'pending': pending_tasks,
            'completed': completed_tasks
        }
        with open(Task_file,'w') as f:
            json.dump(data,f,indent=4)
    except Exception as e:
        termcolor.cprint("Error in saving tasks",'red')


def load_tasks():
    try:
        global pending_tasks, completed_tasks   
        with open(Task_file,'r') as f:
            data=json.load(f)
            pending_tasks = data.get('pending', [])
            completed_tasks = data.get('completed', [])

            termcolor.cprint("Loaded  pending and completed tasks from previous session", 'magenta',attrs=['underline'])

            termcolor.cprint("Pending Tasks:", 'yellow',attrs=['bold'])
            if pending_tasks:
                for index,task in enumerate(pending_tasks,start=1):
                    print(f"{index}.{task}")
            else:
                termcolor.cprint("No completed tasks.", 'yellow')


            termcolor.cprint("Completed Tasks:", 'green', attrs=['bold'])
            if completed_tasks:
                for index,task in enumerate(completed_tasks,start=1):
                    print(f"{index}.{task}")
            else:
                termcolor.cprint("No completed tasks.", 'magenta')


    except Exception:
        termcolor.cprint("Some error occurred in loading data ",'red')

def add_task(): 
    while True:
        task=input("Add a task: ").strip()
        if len(task) != 0:
           pending_tasks.append(task)
           save_tasks()
           termcolor.cprint("Task Added.",'green')
           break
        else:
            print('Invalid task!')


def main():
    load_tasks()
    print("Todo-List Menu :")
    for index,list in enumerate(todo_list_menu,start=1):
        print(index,'. ',list)
    while True:
        try:
            choice=int(input("Enter Your Choice:").strip())
            if choice in choices:
                if choice == 1:
                    view_tasks()
                elif choice==2:
                    add_task()
                elif choice==3:
                    remove_task()
                elif choice==4:
                    mark_as_completed()
                elif choice==5:
                    view_comp_tasks()
                else:
                    save_tasks()
                    exit()
            else:
                raise ValueError
        except ValueError:
            print("Enter a valid choice")


main()