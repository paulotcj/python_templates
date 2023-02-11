import tkinter

window = tkinter.Tk()
#------------------------------------------
# window settings
window.title("Window Title - Test Application")
window.minsize(width = 500, height = 300)

#Label 1
label1 = tkinter.Label(text="I am a label",font=("Arial", 24, "italic"))

#columns and rows are in reference to others. So if we were to define this as column 10 but no
# other item is referencing the grid system, this item would be placed at the leftmost place in the screen
label1.grid(column=0, row=0) 


label1["text"] = "I am a label - text modified"

#Button
def button1_clicked():
    print("button1 was clicked")
    # label1["text"] = "button1 was clicked"
    label1["text"] = input1.get()

button1 = tkinter.Button(text="click here", font=("Arial", 14), command=button1_clicked)
# button1.grid(column=5, row=1)  -> column 5 - it doesnt work
button1.grid(column=1, row=1) 


#input / entry
input1 = tkinter.Entry(width=30,font=("Arial", 14))
input1.grid(column=2, row=2) 



#------------------------------------------
window.mainloop()