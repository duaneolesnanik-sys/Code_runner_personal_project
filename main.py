import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import subprocess
import decoder

#----Variables----
chosen_file = ""
files_open = 0
files_list = []
#-----------------

#----Functions----
def run():
    global chosen_file
    subprocess.run(["python", chosen_file])

def open_program(given = ""):
    global chosen_file, files_open, files_list
    if given == "":
        next_file = askopenfilename(filetypes=[("Python Files", "*.py*")])
    else:
        next_file = given
    if next_file:
        if next_file != chosen_file:
            chosen_file = next_file
        if not files_list.__contains__(next_file):
            btn = tk.Button(main, text = chosen_file[chosen_file.rfind("/")+1:], command = lambda : open_program(next_file)).grid(row = 2, column = files_open)
            files_open += 1
            files_list += [next_file]
        file_display.config(text = chosen_file[chosen_file.rfind("/")+1:])
        code_area.delete("1.0", tk.END)
        with open(chosen_file, 'r') as file:
            code_area.insert(tk.END, decoder.recode(file.read()))

def run_program():
    global chosen_file
    with open(chosen_file, 'w') as file:
        file.write(decoder.decode(code_area.get("1.0", "end-1c")))
    run()

def clear():
    confirm = messagebox.askyesno("Confirmation", "Are you sure you want to clear the screen?\n\nYou wil not be able to undo this action.")
    if confirm:
        code_area.delete("1.0", tk.END)
#-----------------

#---Window Setup---
main = tk.Tk()
main.title("Code Runner")
open_button = tk.Button(main, text = "Open", command = open_program).grid(row = 0, column = 0)
file_display = tk.Label(main, text = "")
file_display.grid(row = 0, column = 1)
run_button = tk.Button(main, text = "Run", command = run_program).grid(row = 0, column = 5)
clear_button = tk.Button(main,text = "Clear", command = clear).grid(row = 0, column = 9)
code_area = tk.Text(main)
code_area.grid(row = 1, column = 0, columnspan=10)
main.mainloop()
#------------------