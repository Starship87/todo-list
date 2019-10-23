import sys

todolist = []

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
    print("add function")
    todo_item = ""
    while todo_item == "":
        print("what is your to do item")
        todo_item = input()
    print("when is it due")
    due_date = input ()

    todolist.append([todo_item, due_date])
    save_data()
    show_list()
    
    menu()

def delete():
    print("")
    show_list()
    print("which item number do you want ot delete?")
    delete_me = int(input()) - 1
    if delete_me <= len (todolist):
        todolist.pop(delete_me)
        save_data()
    else:
        print("item not found")
    menu()
    
def show_list():
    for i in range(len(todolist)):
        print(str(i+1) + ":"+ todolist[i][0]+" Due: "+ todolist[i][1])
        
        

def save_data():
    global todolist

    try:
        myfile = open("todolist.txt", "w")
        #create a string out of our list
        s = ''
        for item in todolist:
            s = s + ','.join(item) + ";"
        s = s 
       

        myfile.write(s)
        myfile.close()
    except:
        print("File not updated")


    
def load_data():
    global todolist

    try:
        myfile = open ("todolist.txt", "r")
        mytext = myfile.read()
        myfile.close()

        #this is where we make the data into our data list
        #li = list(string.split(""))
        print(mytext)
        print(mytext.split(";"))
        print(firstlist)
        firstlist.pop()
        todolist = []
        for item in firstlist:
            todolist.append (item.split(","))
        print(todolist)
        
    except:
        print ("File not read")
def quit():
    sys.exit()

load_data()
menu()

    
