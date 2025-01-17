from tkinter import *

window = Tk()
window.title("Miles to Kilometer conversion")
window.config(padx=20, pady=20)

def milesToKm():
    miles = float(miles_input.get())  # Use float to allow decimal inputs
    km = round(miles * 1.609, 2)  # Round to 2 decimal places
    kilometer_result_label.config(text=f"{km}")

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=milesToKm)
calculate_button.grid(column=1, row=2)

window.mainloop()
