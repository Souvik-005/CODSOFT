from tkinter import *
root=Tk()

tasks_lst=[]

# AddTask function
def addTask():
    show_entry()
    task = entry.get()
    if task:
        tasks_lst.append([task,False])
        result.set("Task Added Successfully.")
    entry.delete(0, END)

# ShowTask function  
def showTasks():
    hide_entry()
    if not tasks_lst:
        result.set("You Don't have any Task.")
    else:
        text = "Tasks:\n"
        for i, task in enumerate(tasks_lst, start=1):
            name = task[0]
            status = "✔" if task[1] else ""
            text += f"{i}. {name} {status}\n"
        result.set(text)

# Marktask function
def markTask():
    show_entry()
    task = entry.get()
    if not task:
        result.set("Please enter a task name.")
        return
    for t in tasks_lst:
        if t[0] == task:          
            if not t[1]:          
                t[1] = True       
                result.set("Task Marked as Complete.")
            else:
                result.set("Task is already completed.")
            entry.delete(0, END)
            return
    result.set("Task not found.")

# DeleteTask function
def deleteTask():
    show_entry()
    task = entry.get()
    if not task:
        result.set("Please enter a task name.")
        return
    for t in tasks_lst:
        if t[0] == task:      
            tasks_lst.remove(t)
            result.set("Task Deleted Successfully.")
            entry.delete(0, END)
            return
    result.set("Task not found.")

# Exit function
def exit():
    root.destroy()

# Fixed Geometry
root.geometry("650x500")
root.resizable(0, 0)
root.title("To Do List")

# Entry
entry = Entry(root, font=("Times New Roman", 14))
def show_entry():
    entry.pack(pady=5)
def hide_entry():
    entry.pack_forget()

# Heading
root_label=Label(root, text="...Welcome To Daily To-Do List... ", font=("Times New Roman", 16,"bold"))
root_label.pack(pady=10)

# Buttons
b1=Button(root, text="Add task.", font=("Times New Roman", 12), command=addTask)
b1.pack(pady=5)

b2=Button(root, text="View tasks.", font=("Times New Roman", 12), command=showTasks)
b2.pack(pady=5)

b3=Button(root, text="Mark a task.", font=("Times New Roman", 12), command=markTask)
b3.pack(pady=5)

b4=Button(root, text="Delete a task.", font=("Times New Roman", 12), command=deleteTask)
b4.pack(pady=5)

b5=Button(root, text="Exit.", font=("Times New Roman", 12), command=exit)
b5.pack(pady=5)

# result
result = StringVar()
result.set("Enter your task")
l1=Label(root, textvariable=result, font=("Times New Roman", 12))
l1.pack(side=BOTTOM,pady=20)

# Mainloop
root.mainloop()