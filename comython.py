import os
import subprocess
from tkinter import * # type: ignore

root = Tk()
root.geometry('600x700')
user_input = StringVar(root)
frm = Frame(root)
frm.grid()

commit = Entry(master=root, textvariable=user_input, width=30)

commit.grid(column=3, row=2)
label = Label(frm, text='')
label.grid(column=2, row=0)

label2 = Label(frm, text='')
label2.grid(column=2, row=1)

label3 = Label(frm, text='')
label3.grid(column=2, row=2)

label4 = Label(frm, text='')
label4.grid(column=2, row=3)

def gitStatus():
    result = subprocess.check_output('git status', shell=True, text=True)
    # label["text"] = user_input.get()
    label["text"] = result

def gitAdd():
    result = subprocess.check_output('git add .', shell=True, text=True)
    label2["text"] = 'ASDYBIUASDBUIASD'

def gitCommit():
    commitMsg = user_input.get()
    result = subprocess.check_output(f"git commit -m '{commitMsg}'", shell=True, text=True)
    print(result)
    label3["text"] = 'Your commit has been commited!'
    print(commitMsg)

def gitPush():
    result = subprocess.check_output('git push origin main', shell=True, text=True)
    label4["text"] = result

Button(frm, text="Check Repository Status",height= 10, width=30, command=gitStatus).grid(column=1, row=0)
Button(frm, text="Add Archives to the Commit",height= 10, width=30, command=gitAdd).grid(column=1, row=1)
Button(frm, text="Commit",height= 10, width=30, command=gitCommit).grid(column=1, row=2)
Button(frm, text="Git Push Origin Main",height= 10, width=30, command=gitPush).grid(column=1, row=4)




root.mainloop()