import tkinter as tk

# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('400x200')

def number():
    try:
       float(my_box.get())
       answer.config(text="That is a number! Congrats!")
    except ValueError:
        answer.config(text="That is NOTanumber!You silly person")

my_label=tk.Label(frame,text="Enter a Number")
my_label.pack(pady=20)
my_box=tk.Entry(frame)
my_box.pack(pady=10)
my_button=tk.Button(frame,text="Enter a Number",command=number)
my_button.pack(pady=5)
answer=tk.Label(frame,text='')
answer.pack(pady=20)

frame.mainloop()