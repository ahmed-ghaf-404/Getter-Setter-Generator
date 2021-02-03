from tkinter import *
import pyperclip

root = Tk()
root.title("Getter and Setter Generator")




def generate_click():
	# current = text_box.get()
	# text_box.delete(0, END)
	# text_box.insert(0, str(current) + str(number))
    clear_text_box()
    var = text_field.get()
    if getter_var.get():
        text_box.insert(END, "def get_{0}(self):\n    return self.{0}\n\n".format(var))
    if setter_var.get():
        text_box.insert(END, "def set_{0}(self, {0}):\n    self.{0} = {0}".format(var))


def clear_text_box():
	text_box.delete(1.0,END)
 
def copy_click():
    pyperclip.copy(text_box.get("1.0","end"))


# Text widget
text_box = Text(root)
text_box.grid(row=0, column=0, rowspan=7, columnspan=7, padx=10, pady=10)

# text field
text_field = Entry(root)
text_field.grid(row=11, column=0)

# checkboxes
getter_var = IntVar()
getter_checker = Checkbutton(root, text="Getter", variable=getter_var, onvalue=1, offvalue=0)
getter_checker.grid(row=11,column=2)


setter_var = IntVar()
setter_checker = Checkbutton(root, text="Setter", variable=setter_var, onvalue=1, offvalue=0)
setter_checker.grid(row=11,column=3)

# Define Buttons

button_copy_to_clipboard = Button(root, text="Copy to clipboard", command=lambda: copy_click())

button_generate = Button(root, text="Generate", command=lambda: generate_click())

button_clear = Button(root, text="Clear", command=clear_text_box)


# Put the buttons on the screen

button_copy_to_clipboard.grid(row=11, column=5)
button_generate.grid(row=11, column=4)

button_clear.grid(row=11, column=6)


root.mainloop()