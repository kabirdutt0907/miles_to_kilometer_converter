from tkinter import *


def calculate():
    miles = float(input.get())
    km = miles * 1.609
    Answer_Label.config(text=f"{km}")


window = Tk()
window.title("My first GUI program ")
window.minsize(height=500, width=500)
window.config(padx=200, pady=200)

input = Entry(width=30)
input.grid(column=2, row=0)
miles = input.get()

My_label = Label(text="Miles", font=("Arial", 15))
My_label.grid(column=3, row=0)
My_label.config(padx=20, pady=20)

Another_Label = Label(text="is equal to ", font=("Arial", 15))
Another_Label.grid(column=1, row=1)

My_label1 = Label(text="km", font=("Arial", 15))
My_label1.grid(column=3, row=1)

Answer_Label = Label(text="0")
Answer_Label.grid(column=2, row=1)
Answer_Label.config(padx=10, pady=10)

button = Button(text="Calculate", command=calculate)
button.grid(column=2, row=2)

window.mainloop()
