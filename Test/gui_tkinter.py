#Tkinter
# from tkinter import * #Import all definitions of tkinter

# def processOK():
#     print("Ok button clicked!")

# def processCancel():
#     print("Cancel button clicked!")    

# window = Tk() #Create window
# label = Label(window, text = "Welcome to the program!") #Create label
# click_button = Button(window, text = "Click to expand", fg = "red", command = processOK) #Create button | fg = foreground

# cancel_button = Button(window, text = "Click to cancel", bg = "yellow", command = processCancel) #bg = background

# label.pack() #Put label into window
# click_button.pack() #Put button into window
# cancel_button.pack()

# window.mainloop()

#Tkinter Class
# from tkinter import * 

# class ProcessButtonEvent:
#     def __init__(self):
#         window = Tk()
#         btOK = Button(window, text = "Ok", fg = "red", command = self.processOK)
#         btCancel = Button(window, text = "Cancel", bg = "yellow", command = self.processCancel)

#         btOK.pack()
#         btCancel.pack()

#         window.mainloop()

#     def processOK(self):
#         print("OK button is clicked!")

#     def processCancel(self):
#         print("Cancel button is clicked!")

# ProcessButtonEvent()

# #Widget Demos
# from tkinter import *

# class Widgets:
#     def __init__(self):
#         window = Tk()
#         window.title("Widgets Demo")

#         # Checkbutton and Radiobuttons in frame1
#         frame1 = Frame(window)
#         frame1.pack()
#         self.v1 = IntVar()
#         cbtbold = Checkbutton(frame1, text="Bold", variable=self.v1, command=self.processCheckButton)
#         self.v2 = IntVar()
#         rbRed = Radiobutton(frame1, text="Red", bg="red", variable=self.v2, value=1, command=self.processRadioButton)
#         rbYellow = Radiobutton(frame1, text="Yellow", bg="yellow", variable=self.v2, value=2, command=self.processRadioButton)

#         cbtbold.grid(row=1, column=2)
#         rbRed.grid(row=2, column=1)
#         rbYellow.grid(row=2, column=3)

#         # Add a label, an entry, a button, and a message to frame2
#         frame2 = Frame(window)
#         frame2.pack()
#         label = Label(frame2, text="Enter your name: ")

#         self.name = StringVar()
#         entryName = Entry(frame2, textvariable=self.name)
#         btGetName = Button(frame2, text="Get Name", command=self.processButton)
#         message = Message(frame2, text="It is a widgets demo")

#         label.grid(row=1, column=1)
#         entryName.grid(row=1, column=2)
#         btGetName.grid(row=1, column=3)
#         message.grid(row=1, column=4)

#         # Add text box
#         text = Text(window)
#         text.pack()
#         text.insert(END, "Tip\nThe best way to learn Tkinter is to read ")
#         text.insert(END, "these carefully designed examples and use them ")
#         text.insert(END, "to create your applications.")

#         window.mainloop()

#     def processCheckButton(self):
#         print("Check button is " + ("checked " if self.v1.get() == 1 else "unchecked"))

#     def processRadioButton(self):
#         print(("Red" if self.v2.get() == 1 else "Yellow") + " is selected ")

#     def processButton(self):
#         print("Your name is " + self.name.get())

# Widgets()
