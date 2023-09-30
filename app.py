import tkinter as tk
import tkinter.font as tkFont
import serial.tools.list_ports as lp

class App:
    def __init__(self, root):
        #setting title
        root.title("DigiFG_RISC")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_331=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_331["font"] = ft
        GLabel_331["fg"] = "#333333"
        GLabel_331["justify"] = "center"
        GLabel_331["text"] = "Waveform Generator control"
        GLabel_331.place(x=150,y=10,width=311,height=38)

        GLabel_567=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_567["font"] = ft
        GLabel_567["fg"] = "#333333"
        GLabel_567["justify"] = "center"
        GLabel_567["text"] = "USB ports on PC"
        GLabel_567.place(x=230,y=50,width=132,height=30)

        l=[comport.device for comport in lp.comports]
        print(l)
        inc=0

        for i in l:
            GRadio_563=tk.Radiobutton(root)
            ft = tkFont.Font(family='Times',size=10)
            GRadio_563["font"] = ft
            GRadio_563["fg"] = "#333333"
            GRadio_563["justify"] = "center"
            GRadio_563["text"] = "RadioButton"
            GRadio_563.place(x=250,y=80+inc,width=85,height=25)
            GRadio_563["command"] = self.GRadio_563_command
            inc+=30

    def GRadio_563_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
