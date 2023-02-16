from tkinter import *

class Footer:
    def __init__ (self, root, footerFrame):
        global sudoPassEntry
        
        self.root = root
        self.footerFrame = footerFrame

        self.sudoPassLabel = Label(self.footerFrame, text = "Sudo Password : ", font="Bahnschrift 15", bg="#333333", fg="#ffffff", padx = 20)
        self.sudoPassLabel.place(y = 8)

        sudoPassEntry = Entry(self.footerFrame, width = 40, font="bahnschrift 15", fg="#ffffff", bg="#252525", show="*")
        sudoPassEntry.place(x = 195, y = 8)

    def getSudoPass():
        return sudoPassEntry.get()

