import tkinter as tk
from tkinter import messagebox

class ToDoList(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List")
        self.geometry("300x400")

        # Create a Listbox to display tasks
        self.tasks = tk.Listbox(self)
        self.tasks.pack()

        # Create a Entry widget to add new tasks
        self.task_create = tk.Entry(self)
        self.task_create.pack()

        # Create a button to add new tasks
        self.add_task = tk.Button(self, text="Add Task", command=self.add_task)
        self.add_task.pack()

        # Create a button to delete tasks
        self.del_task = tk.Button(self, text="Delete Task", command=self.del_task)
        self.del_task.pack()

    def add_task(self):
        task = self.task_create.get()
        if task:
            self.tasks.insert(tk.END, task)
            self.task_create.delete(0, tk.END)

    def del_task(self):
        task = self.tasks.get(self.tasks.curselection())
        if task:
            if messagebox.askyesno("Delete Task", f"Delete {task}?"):
                self.tasks.delete(self.tasks.curselection())

if __name__ == "__main__":
    todo = ToDoList()
    todo.mainloop()
