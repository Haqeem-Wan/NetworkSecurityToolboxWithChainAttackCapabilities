from tkinter import *
from ProgramSetup.Header import Header

class ProgramWindow :
    def __init__ (self):
        self.root = Tk()
        self.root.geometry("1280x720")
        self.root.resizable(width = False, height = False)
        self.root.title("1191102618 - Network Security Toolbox With Chain Attack Capabilities")
        
        try:
            self.root.iconphoto(True, PhotoImage(file="fypcode/img/ToolboxLogo_White.png"))
        except:
            print("Error : ToolboxLogo_White.png not found!")


        self.headerFrame = Frame(self.root,width=1280,height=50,background="#333333",borderwidth=3,relief="raised")
        self.contentFrame = Frame(self.root, width=1280, height=620, background="#454545")
        self.footerFrame = Frame(self.root,width=1280,height=50,background="#333333",borderwidth=3,relief="raised")

        self.headerContents = Header(self.root, self.headerFrame, self.contentFrame)

        self.headerFrame.pack(side="top")
        self.contentFrame.pack_propagate(0)
        self.contentFrame.pack()
        self.footerFrame.pack(side="bottom")

    def start(self):
        self.root.mainloop()