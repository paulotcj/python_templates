from tkinter import *

#Creating a new window and configurations
window = Tk()
#------------------------------------------
# window settings
window.title("Widget Examples")
window.minsize(width=500, height=500)

#-----
#Labels
label1 = Label(text="This is old text",font=("Arial", 14))
label1.config(text="This is new text")
label1.pack()

#-----
#Buttons
def button1_click():
    print("Do something")
    label1["text"] = text1.get()

#calls action() when pressed
button1 = Button(text="Click Me",font=("Arial", 14), command=button1_click)
button1.pack()

#-----
#Entries
entry1 = Entry(width=30,font=("Arial", 14))
#Add some text to begin with
entry1.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry1.get())
entry1.pack()

#Text / text box / multi line
text1 = Text(height=5, width=30,font=("Arial", 14))
#Puts cursor in textbox.
text1.focus()
#Adds some text to begin with.
text1.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text1.get("1.0", END))
text1.pack()


#-----
#Spinbox / combo box / list
def spinbox1_click():
    #gets the current value in spinbox.
    print(spinbox1.get())

spinbox1 = Spinbox(from_=0, to=10, width=5, command=spinbox1_click, font=("Arial", 14))
spinbox1.pack()


#-----
#Scale / slider
#Called with current scale value.
def scale1_used(value):
    print(value)

scale1 = Scale(from_=0, to=100, command=scale1_used, font=("Arial", 14))
scale1.pack()

#-----
#Checkbutton
def checkbutton1_clicked():
    #Prints 1 if On button checked, otherwise 0.
    print(checkbutton1_state.get())


#variable to hold on to checked state, 0 is off, 1 is on.
checkbutton1_state = IntVar(value=1)
checkbutton1 = Checkbutton(text="Is On?", variable=checkbutton1_state, command=checkbutton1_clicked, font=("Arial", 14))
print(f"checkbutton1_state.get(): {checkbutton1_state.get()}")
checkbutton1.pack()


#-----
#Radiobutton
def radiobuttons_clicked():
    print(radiobutton1_state.get())


#Variable to hold on to which radio button value is checked.
radiobutton1_state = IntVar(value=2)

radiobutton1 = Radiobutton(text="Option1", value=1, variable=radiobutton1_state, command=radiobuttons_clicked, font=("Arial", 14))
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radiobutton1_state, command=radiobuttons_clicked, font=("Arial", 14))

radiobutton1.pack()
radiobutton2.pack()

#-----
#Listbox
def listbox1_clicked(event):
    # Gets current selection from listbox
    print(listbox1.get(listbox1.curselection()))

listbox1 = Listbox(height=4, font=("Arial", 14))

fruits = ["Apple", "Pear", "Orange", "Banana", "Pineapple", "Strawberry"]

for item in fruits:
    listbox1.insert(fruits.index(item), item)

listbox1.bind("<<ListboxSelect>>", listbox1_clicked)
listbox1.pack()



#------------------------------------------
window.mainloop()
