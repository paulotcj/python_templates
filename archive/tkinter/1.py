import tkinter

window = tkinter.Tk()
#------------------------------------------
# window settings
window.title("Window Title - Test Application")
window.minsize(width = 500, height = 300)

#Label 1
label1 = tkinter.Label(text="I am a label",font=("Arial", 24, "italic"))
# label1.pack()
# label1.pack(side = "left")
# label1.pack(side = "bottom")
label1.pack(expand = True)



#------------------------------------------
window.mainloop()