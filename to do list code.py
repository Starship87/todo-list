import sys

todolist = {}
next_key = 1
def menu():
    print("choose your option.")
    print("7 = delete item")
    print("8 = add_item")
    print("9 = quit")
    choice = input()
    if choice == "7":
        delete()
    elif choice == "8":
        add()
    elif choice  == "9":
        quit()
    else:
        print("Invalid selection.")
        
    
    
    
    

def add():
    global next_key
    print("add function")
    todo_item = ""
    while todo_item == "":
        print("what is your to do item")
        todo_item = input()
    print("when is it due")
    due_date = input ()

    todolist[next_key] = [todo_item, due_date]
    show_list()
    menu()

def delete():
    print("")
    show_list()
    print("which item number do you want ot delete?")
    delete_me = int(input())
    if delete_me in todolist:
        del todolist[delete_me]
    else:
        print("item not found")
    menu()
def show_list():
    print(todolist)


def quit():
    sys.exit()
  
menu()

    
