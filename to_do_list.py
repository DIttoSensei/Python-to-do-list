import tkinter as tk
from tkinter import messagebox
import os

root = tk.Tk() # this initializes the main window of the application
root.title("To-Do List") # Sets window title
root.geometry("400x500") # Set the window size to 400x400 pixels

top_frame = tk.Frame(root, bg='grey')
top_frame.pack(side="top", fill="both", expand=True)

bottom_frame = tk.Frame(root, bg='grey')
bottom_frame.pack(side="bottom", fill="both", expand=True)

# store checkbutton variables
tasks = []

# Frame to hold listbox and scrollbar
frame = tk.Frame(root)
frame.pack(pady=10)

# Create entry widget to type in new tasks
task_entry = tk.Entry(root,width=40)
task_entry.pack (pady=10)

#create a listbox to hold tasks
task_listbox = tk.Listbox(frame,height=10,width=50,selectmode=tk.MULTIPLE)
task_listbox.pack (side=tk.RIGHT, fill=tk.BOTH)

# scrollbar for the listbox
scrollbar = tk.Scrollbar(frame)
scrollbar.pack (side=tk.RIGHT, fill=tk.BOTH)

# Link scrollbar to listbox
task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

# function to add task
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append([task, False])
        task_listbox.insert (tk.END, task)
        task_entry.delete(0,tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task")        

# Function to delete a task
def delete_task():
    try:
        selected_task_index =task_listbox.curselection()[0] # Get the index of the selected task
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete")

# Function to save tasks to a file
def save_task():
    tasks = task_listbox.get(0,tk.END)
    with open("task.txt", "w") as f:
        for task in tasks:
            f.write(f"{task}\n")
            messagebox.showinfo("Save", "Tasks saved successfully")

# Function to load tasks from a file on startup
def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as f:
            for task in f.readlines():
                task_listbox.insert(tk.END, task.strip()) # strip to remove new lines

# Function to edit the selected text
def edit_task():
    try:
        # Get the selected task index
        selected_task_index = task_listbox.curselection()[0]
        # get the selscted task
        selected_task = task_listbox.get(selected_task_index)
        # insert the selected task in the entry box for editing
        task_entry.delete(0,tk.END) 
        task_entry.insert(tk.END, selected_task)
        # Function to update the task after editing
                
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to edit")

# Function to update the selectected and editected text
def update_task ():
            #Get the updated task from the entry
            selected_task_index = task_listbox.curselection()[0]
            updated_task = task_entry.get ()
            if updated_task != "":
                task_listbox.delete(selected_task_index)
                task_listbox.insert(selected_task_index, updated_task)
                task_entry.delete(0, tk.END) # clear the entry box
            else:
                messagebox.showwarning("Input Error", "Please enter a task.")

# Function to mark a function complete
def mark_complete():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_text, completed = tasks[selected_task_index]
        if completed:
            task_listbox.itemconfig(selected_task_index, {'fg': 'black'})
            tasks[selected_task_index][1] = False

        else:
            task_listbox.itemconfig(selected_task_index, {'fg': 'gray'})
            tasks[selected_task_index][1] = True
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

# Add a button to add a task
add_button = tk.Button(root, text="Add Task", width=42,command=add_task)
add_button.pack(pady=10)

# Add a button to delete tasks
delete_button = tk.Button (root,text="Delete Task", width=42,command=delete_task)
delete_button.pack(pady=10)

# Add a button to save tasks
save_button = tk.Button(root,text="Save Task",width=42,command=save_task)
save_button.pack(pady=10)

# Add a button to edit task
edit_task_button = tk.Button(root,text="Edit Task",width=30, command=edit_task)
edit_task_button.pack(pady=10)

# update button to save edited task
update_button = tk.Button (root, text="Update Task", command=update_task)
update_button.pack(pady=10)

# mark as completed button
mark_completed_button = tk.Button (root, text="Mark as Completed", width=30, command=mark_complete)
mark_completed_button.pack(pady=10)

#call the load task function after setting up window
load_tasks()

# run tkinter event loop
root.mainloop() 