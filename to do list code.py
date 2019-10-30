import sys
import tkinter
todolist = []
root = tkinter.Tk()



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
        
    #fix file not read.
    
    
    

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
    listbox.delete(0,"end")
    load_data()
    print(todolist)
    for i in range(len(todolist)):
        listbox.insert(tkinter.END, str(i+1) + ":"+ todolist[i][0]+" Due: "+ todolist[i][1])
        
        

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
def quitme():
    root.destroy()

myfont = "arial 14 bold"
#make controlls
#place controlls on screen
title = tkinter.Label(root, text="Get This Stuff Done!", font ="Arial 20 bold")
title.grid(row=0, column=0, columnspan=3)
addbtn = tkinter.Button(root, text="Add", font=myfont)
addbtn.grid(row=2, column=2, rowspan=2)
quitbtn = tkinter.Button(root, text="Quit", font=myfont, command=quitme) 
quitbtn.grid(row=4, column=2, rowspan=2)
delbtn = tkinter.Button(root, text="Delete", font=myfont) 
delbtn.grid(row=4, column=1, rowspan=2)
itembox = tkinter.Entry(root)
itembox.grid(row=2, column=1)
databox = tkinter.Entry(root)
databox.grid(row=3, column=1)
itemLabel = tkinter.Label(root, text= "new item", font=myfont)
itemLabel.grid(row=2, column=0)
dataLabel = tkinter.Label(root, text= "Due Date", font=myfont)
dataLabel.grid(row=3, column=0)
listbox = tkinter.Listbox(root, width=40, height=20)
listbox.grid(row=1, column=0, columnspan=3)
show_list()
root.mainloop()


    
