import tkinter

# Initial answer for value


def calculate_km():
    answer_label2["text"] = round(int(miles_input.get()) * 1.60934, 2)


window = tkinter.Tk()
window.title("Mile to KM Converter")
window.minsize(width=250, height=150)
window.config(padx=20, pady=20)

# Input
miles_input = tkinter.Entry(width=8)
miles_input.grid(column=2, row=0)
miles_input.focus()

# Label for Input
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=3, row=0)

# Label for answer
answer_label1 = tkinter.Label(text=f"is equal to")
answer_label2 = tkinter.Label(text="0")
answer_label3 = tkinter.Label(text="KM")
answer_label1.grid(column=1, row=1)
answer_label2.grid(column=2, row=1)
answer_label3.grid(column=3, row=1)

# Button
calculate_btn = tkinter.Button(text="Calculate", command=calculate_km)
calculate_btn.grid(column=2, row=2)


window.mainloop()
