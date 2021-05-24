# !/usr/bin/python3
from tkinter import *
from tkinter import messagebox

def inputValue(valueA):

    if valueA.isnumeric():
        valueA = float(valueA)

    else:
        #messagebox.showinfo(("Invalid value", "O valor digitado não é um valor válido, digite novamente!"))
        #print("\033[0;31mO valor digitado não é um valor válido, digite novamente!\033[m")
        valueA = False

    return valueA


def sum_calc():
    if not (inputValue(entry1Field.get())) and not (inputValue(entry2Field.get())):
        messagebox.showinfo("Invalid value", "The first and second values are invalid!")
    elif not (inputValue(entry1Field.get())):
        messagebox.showinfo("Invalid value", "The first value is invalid!")
    elif not (inputValue(entry2Field.get())):
        messagebox.showinfo("Invalid value", "The second value is invalid!")
    else:
        return text.insert(INSERT, inputValue(entry1Field.get()) + inputValue(entry2Field.get()))

def sub_calc():
    if not (inputValue(entry1Field.get())) and not (inputValue(entry2Field.get())):
        messagebox.showinfo("Invalid value", "The first and second values are invalid!")
    elif not (inputValue(entry1Field.get())):
        messagebox.showinfo("Invalid value", "The first value is invalid!")
    elif not (inputValue(entry2Field.get())):
        messagebox.showinfo("Invalid value", "The second value is invalid!")
    else:
        return text.insert(INSERT, inputValue(entry1Field.get()) - inputValue(entry2Field.get()))

def mult_calc():
    if not (inputValue(entry1Field.get())) and not (inputValue(entry2Field.get())):
        messagebox.showinfo("Invalid value", "The first and second values are invalid!")
    elif not (inputValue(entry1Field.get())):
        messagebox.showinfo("Invalid value", "The first value is invalid!")
    elif not (inputValue(entry2Field.get())):
        messagebox.showinfo("Invalid value", "The second value is invalid!")
    else:
        return text.insert(INSERT, inputValue(entry1Field.get()) * inputValue(entry2Field.get()))

def div_calc():
    if not (inputValue(entry1Field.get())) and not (inputValue(entry2Field.get())):
        messagebox.showinfo("Invalid value", "The first and second values are invalid!")
    elif not (inputValue(entry1Field.get())):
        messagebox.showinfo("Invalid value", "The first value is invalid!")
    elif not (inputValue(entry2Field.get())):
        if inputValue(entry2Field.get()) is 0:
            messagebox.showinfo("Invalid division", "The denominator number can't be zero")
        else:
            messagebox.showinfo("Invalid value", "The second value is invalid!")
    else:
        return text.insert(INSERT, inputValue(entry1Field.get()) / inputValue(entry2Field.get()))

def sair():
    root.destroy()

def clear():
    entry1Field.delete(0, 'end')
    entry2Field.delete(0, 'end')
    text.delete('1.0', END)

root = Tk()
root.geometry("500x350")
root.title("Calculator")

#Top label
labelFrame = LabelFrame(root, text="\nPlease, choose the desired option")
labelFrame.pack(fill="both", expand="yes")
labelFrame.place(x=50, y=1, height=40, width=400)

# First entry
entry1Label = Label(root, text="First value")
entry1Label.pack(side=LEFT)
entry1Label.place(x=100, y=40, height=40, width=400)
entry1Field = Entry(root, bd=5, bg = "light gray", fg = "black")
entry1Field.pack(side=RIGHT)
entry1Field.place(x=250, y=70, height=40, width=100)
valueA = inputValue(entry1Field.get())

# Second entry
entry2Label = Label(root, text="Second value")
entry2Label.pack(side=LEFT)
entry2Label.place(x=100, y=100, height=40, width=400)
entry2Field = Entry(root, bd=5, bg = "light gray", fg = "black")
entry2Field.pack(side=RIGHT)
entry2Field.place(x=250, y=130, height=40, width=100)

# Total field
total = Label(root, text="Total")
total.pack(side=LEFT)
total.place(x=100, y=160, height=40, width=400)
text = Text(root, bd = 5, bg = "light gray", fg = "black")
text.pack(side=TOP)
text.place(x=250, y=190, height=35, width=100)
text.tag_add("here", "1.0", "1.4")
text.tag_config("here", background = "black", foreground = "blue")


# Sum button
sumButton = Button(root, text="Sum", command=sum_calc)
sumButton.place(x=50, y=50)

# Subtraction button
subtractionButton = Button(root, text="Subtraction", command=sub_calc)
subtractionButton.place(x=50, y=100)

# Multiplication button
multiplicationButton = Button(root, text="Multiplication", command=mult_calc)
multiplicationButton.place(x=50, y=150)

# Multiplication button
divisionButton = Button(root, text="Division", command=div_calc)
divisionButton.place(x=50, y=200)

# Sair button
divisionButton = Button(root, text="SAIR", fg = "Red", command=sair)
divisionButton.place(x=50, y=250)

# Clear button
divisionButton = Button(root, text="Clear", fg = "Blue", command=clear)
divisionButton.place(x=370, y=70,)

root.mainloop()
