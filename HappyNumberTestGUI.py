import tkinter as tk
import HappyNumber

def hpynmb():
    try:
        s=txt1.get()
        if HappyNumber.ishappy(int(s)):
            v.set(s+" is a happy number")
        else:
            v.set(s + " is a not happy number")

    except:
        v.set("Please enter an integer!")


window=tk.Tk()
window.geometry("400x200")

v=tk.StringVar()
txt1=tk.Entry(window)
lbl=tk.Label(window,textvariable=v,fg="dark blue")
btn=tk.Button(window,command=hpynmb,width=15,height=4,text="Is my number\nHAPPY?",activebackground="yellow",background="red")
txt1.pack()
lbl.pack()
btn.pack()

window.mainloop()




