from tkinter import *
import tkinter as tk


class MyApp:

    def __init__(self, root):
        root.title("The Window") #adds title
        root.geometry("500x400") #sets window dementions
        root.maxsize(1000, 800)  #sets max size to window

        frame = Frame(root, width=200, height=100, borderwidth=2, relief="sunken")
        frame.place(x=0, y=0)

        self.label_text = StringVar()
        label = Label(root, textvariable= self.label_text)
        # label.pack(side=TOP, padx=2) #packs everything and runs widget. Needed to work
        # label.grid(column=1, row=1)

        #dictionary syntax. These will change one at a time
        # label["text"] = "Dictionary syntax text"
        # label['font'] = ("Courier", 40)

        #configure() method. This can make multiple changes at once
        label.configure(text = "New Text", font = ("Courier", 20))

        self.entry_text = StringVar() #for having a string that can be updated
        entry = Entry(root, textvariable=self.entry_text) #Creates single line text inputs
        # entry.pack(side=LEFT, pady=3) #packs everything and runs widget
        # entry.place(x=50, y=0)
        # entry.grid(column=2, row=1)

        #This will start the button widget. The command= is what sets the press_button function to it.
        #The self.press_button does not have () at end since were not calling it, were just passing reference
        button = Button(root, text="Button Text", command=self.press_button)
        # button.pack(side=LEFT, pady=3)
        # button.grid(column=1, row=2)

        #This creates a listbox. A list will need to be created first, which will have to be passed through a StringVar
        #then it can be added to the listvariable
        self.list_item_string = ["Hi", "Hey", "Hello", "Howdy", "Greetings"]
        list_item = StringVar(value=self.list_item_string)
        listbox = Listbox(root, listvariable=list_item, height=3)
        # listbox.pack(side=RIGHT)
        listbox.bind("<<ListboxSelect>>", lambda s: self.select_item(listbox.curselection()))
        # listbox.grid(column=2, row=2)

    def press_button (self):
        #This will create a variable and get the entry_text, then set to label_text
        text = self.entry_text.get()
        self.label_text.set(text)

    def select_item (self, index):
        selected_item = self.list_item_string[index[0]]
        print(selected_item)


root = Tk() #creates app root
MyApp(root)
root.mainloop()

