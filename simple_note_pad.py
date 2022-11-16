from tkinter import *
from tkinter import font,filedialog
def savefile():
    global page
    text = page.get("1.0","send")
    fdialog=filedialog.asksaveasfilename(defaultextension=".txt")
    file=open(fdialog,"w+")
    file.write(text)
    file.close()
root=Tk()
root.title("Panda Express Notebook")
page=Text(root)
page.grid(row=2, columnspan=5)
icon = PhotoImage(file="index.png")
root.iconphoto(True,icon)
mainloop()
