import tkinter

window = tkinter.Tk()
#------------------------------------------
# window settings
window.title("Window Title - Test Application")
window.minsize(width = 500, height = 300)

#Label 1
label1 = tkinter.Label(text="I am a label",font=("Arial", 24, "italic"))
label1.pack(side="left")
# label1.pack(side = "left")
# label1.pack(side = "bottom")
# label1.pack(expand = True)

label1["text"] = "I am a label - text modified"

#Button
def button1_clicked():
    print("button1 was clicked")
    # label1["text"] = "button1 was clicked"
    label1["text"] = input1.get()

button1 = tkinter.Button(text="click here", font=("Arial", 14), command=button1_clicked)
button1.pack(side="left")


#input / entry
input1 = tkinter.Entry(width=30,font=("Arial", 14))
input1.pack(side="left")



#------------------------------------------
window.mainloop()