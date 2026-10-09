import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import subprocess

#----Variables----
chosen_file = ""
symbols = """`~1!2@3#4$5%6^7&8*9(0)-_=+qQwWeErRtTyYuUiIoOpP[{}]|aAsSdDfFgGhHjJkKlL;:'zZxXcCvVbBnNmM,<.>/?"""
screen_print = f"""import tkinter as tk
import threading
wndw = tk.Tk()
wndw.geometry("300x200")
screen = tk.Label(wndw, text = "")
screen.pack()
txt = ""

active_prompt = False
prompt_txt = ""
usable_symbols = "{symbols}"
prompt_answer = ""
def take_input(event):
    global prompt_txt, active_prompt, usable_symbols, txt, prompt_answer
    if active_prompt:
        if usable_symbols.find(event.keysym) > -1:
            prompt_txt += event.keysym
        elif event.keysym == "BackSpace":
            prompt_txt = prompt_txt[:-1]
        elif event.keysym == "space":
            prompt_txt += " "
        elif event.keysym == "Return":
            active_prompt = False
            txt += prompt_txt
            prompt_answer = prompt_txt
            prompt_txt = ""
wndw.bind("<Key>", take_input)

def update():
    global active_prompt
    cursor = ""
    if active_prompt:
        cursor = "_"
    else:
        cursor = ""
    screen.config(text = txt+prompt_txt+cursor)
    wndw.after(100,update)
backrun = threading.Thread(target = update, daemon = True)
def get_in(prompt):
    global active_prompt, prompt_answer, txt
    active_prompt = True
    txt += str(prompt)
    while active_prompt:
        pass
    return prompt_answer
def oust(q):
    global txt
    txt += str(q)
def main():
    global txt, active_prompt, prompt_answer
    """
screen_print_end = """
program = threading.Thread(target = main, daemon = True)
backrun.start()
program.start()
wndw.mainloop()"""
new_line = """
"""
tab_line = """
    """

#-----------------

#----Functions----
def run():
    global chosen_file
    subprocess.run(["python", chosen_file])

def open_program():
    global chosen_file
    chosen_file = askopenfilename(filetypes=[("Python Files", "*.py*")])
    file_display.config(text = chosen_file[chosen_file.rfind("/")+1:])
    code_area.delete("1.0", tk.END)
    with open(chosen_file, 'r') as file:
        code_area.insert(tk.END, file.read())

def plandecode(thing):
    """Very Bad"""
    #thing = thing[:thing.find("input(")+5]
    thing = screen_print + thing.replace("print","oust").replace(new_line,tab_line).replace("input","get_in") + screen_print_end
    return thing

def run_program():
    global chosen_file
    with open(chosen_file, 'w') as file:
        file.write(plandecode(code_area.get("1.0", "end-1c")))
    run()
#-----------------

#---Window Setup---
main = tk.Tk()
open_button = tk.Button(main, text = "Open", command = open_program).grid(row = 0, column = 0)
file_display = tk.Label(main, text = "")
file_display.grid(row = 0, column = 1)
run_button = tk.Button(main, text = "Run", command = run_program).grid(row = 0, column = 5)
code_area = tk.Text(main)
code_area.grid(row = 1, column = 0, columnspan=10)
main.mainloop()
#------------------