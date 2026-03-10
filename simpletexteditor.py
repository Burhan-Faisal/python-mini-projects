import os,termcolor

choices=['Append Some Text',
        'Overwite All Text',
        'Replace Some Words']


def get_user_input():
    print("Enter your text(type 'Save' on a new line to save and exit)\n")
    lines=[]
    while True:
        line=input()
        if line.strip().upper()=='SAVE':
            break
        else:
            lines.append(line)
    return '\n'.join(lines)

def word_exists(name,word):
    with open(name,'r') as file:
        for line in file:
            if line.__contains__(word):
                return True
    return False


def replace_text(name):
    with open(name,'r+') as file:
        print("Existing Content: \n",file.read())
    while True:
        actual_word=input("Search For Your Specific Word or Phrase :").strip()
        if(word_exists(name,actual_word)) and actual_word :
            with open(name,'r+') as file:
                data=file.read()
                file.seek(0)
                replaced_word=input("Enter The word/Phrase You want to replace with: ").strip()
                file.write(data.replace(actual_word,replaced_word)) 
                return
        else:
            termcolor.cprint("Word don't Exist.Enter a valid word",'red')       

def simple_text_editor():
    name=input("Enter the file name want to open or create :")
    if os.path.exists(name):
        print("Which file operation you want to perform?")
        for index,choice in enumerate(choices,start=1):
            print(f'{index}.{choice}')
        while True:
            try:
                choice=input('Enter Your Choice No. : ').strip()
                if choice =='1' :
                    with open(name,'r+') as file:
                        print("Existing Content \n",file.read())
                        data=get_user_input()
                        file.write(f'{data}\n')
                        termcolor.cprint(f'{name} Saved Successfully','green')
                        return
                elif choice=='2':
                    with open(name,'w') as file:
                        data=get_user_input()
                        file.write(f'{data}\n')
                        termcolor.cprint(f'{name} Saved Successfully','green')
                        return
                elif choice=='3':
                    replace_text(name)
                    termcolor.cprint(f'{name} Saved Successfully','green')
                    return
                else:
                    raise NameError
            except NameError:
                termcolor.cprint("Invalid Choice",'red')
    else:
        print(f"{name} not found. Creating a new file\n ")
        with open(name,'w') as file:
            data=get_user_input()
            file.write(f'{data}\n')
            termcolor.cprint(f'{name} Saved Successfully','green')

simple_text_editor()


                



