
#---Variables---
new_line = """
"""
tab_line = """
    """
quote = """ " """.strip()
symbols = "`~1!2@3#4$5%6^7&8*9(0)-_=+qQwWeErRtTyYuUiIoOpP[{}]|aAsSdDfFgGhHjJkKlL;:'zZxXcCvVbBnNmM,<.>/?"
screen_print = f"""import tkinter as tk
import threading
wndw = tk.Tk()
wndw.geometry("300x200")
wndw.title("Screen")
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
            txt += prompt_txt + ""{f""" "{new_line}" """.strip()}""
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
def oust(q, end = ""{f""" "{new_line}" """.strip()}""):
    global txt
    txt += str(q)+end
def clear():
    global txt
    txt = ""
def main():
    global txt, active_prompt, prompt_answer
    """
screen_print_end = """
program = threading.Thread(target = main, daemon = True)
backrun.start()
program.start()
wndw.mainloop()"""
#---------------

def decode(thing):
    """Very Bad"""
    quotes = []
    thing2 = thing
    while thing2.find(quote) > -1:
        qstr = thing2[thing2.find(quote)  :  thing2.find(quote) + 1 + thing2[thing2.find(quote)+1 :].find(quote) + 1]
        quotes += [qstr]
        thing2 = thing2.replace(qstr,"")
        thing = thing.replace(qstr,"gorbadoodlydoo"+str(len(quotes)-1))
    thing = screen_print + thing.replace("print","oust").replace(new_line,tab_line).replace("input","get_in") + screen_print_end
    for i in range(len(quotes)):
        thing = thing.replace("gorbadoodlydoo"+str(i),quotes[i])
    return thing

def recode(thing):
    thing = thing.replace(screen_print,"").replace(screen_print_end, "")
    thing = thing.replace("oust","print").replace("get_in","input").replace(tab_line,new_line)
    return thing