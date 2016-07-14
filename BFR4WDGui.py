from Tkinter import *
from PIL import Image
from PIL import ImageTk
import BFR4WDserialGUI
import BFR4WDOpenCVGui



class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):

        ##################################################################
        # Robot Move control graphics
        ##################################################################
        self.moveControl = Canvas(self, width=305, height=305)
        self.moveControl.grid(row = 0, column = 0, columnspan = 2, rowspan = 2)
        self.moveImg = PhotoImage(file='Images/BFR4WDMove.gif')
        self.moveControl .create_image(0,0, anchor=NW, image=self.moveImg)
        self.moveControl.bind('<Button-1>', self.moveClick)

        
        ##################################################################
        # Head control graphics
        ##################################################################
        self.headControl = Canvas(self, width=305, height=305)
        self.headControl.grid(row = 0, column = 2, columnspan = 2, rowspan = 2)
        self.headImg = PhotoImage(file='Images/BFR4WDHead.gif')
        self.headControl .create_image(0,0, anchor=NW, image=self.headImg)
        self.headControl.bind('<Button-1>', self.headClick)


        ##################################################################
        # Compass turn to heading graphics
        ##################################################################
        self.compassControl = Canvas(self, width=152, height=152)
        self.compassControl.grid(row = 0, column = 4)
        self.compassImg = PhotoImage(file='Images/BFR4WDCompass.gif')
        self.compassControl .create_image(0,0, anchor=NW, image=self.compassImg)
        self.compassControl.bind('<B1-Motion>',  self.TurnToHeading)
        


        self.CamImage = Canvas(self, width=320, height=240,bg = "black")
        self.CamImage.grid(row = 3, column = 0)

        self.commandEntry= Entry(self)
        self.commandEntry.grid(row = 2, column = 0)
        self.commandEntry.bind('<Return>', self.sendCommand)

        self.returnEntry= Entry(self)
        self.returnEntry.grid(row = 2, column = 2)

        self.send = Button(self, text="Send")
        self.send.bind('<Button-1>', self.sendCommand)
        self.send.grid(row = 2, column = 1)

        self.servoOnbutton = Button(self, text="Servo Power On")
        self.servoOnbutton.bind('<Button-1>', self.servoOn)
        self.servoOnbutton.grid(row = 1, column = 5)

        self.servoOffbutton = Button(self, text="Servo Power Off")
        self.servoOffbutton.bind('<Button-1>', self.servoOff)
        self.servoOffbutton.grid(row = 2, column = 5)

        self.Capturebutton = Button(self, text="Capture", command = self.CaptureImage)
        self.Capturebutton.grid(row = 3, column = 5)


        self.QUIT = Button(self, text="QUIT", fg="red",command=root.destroy)
        self.QUIT.grid(row = 3, column = 3)


    def sendCommand(self,event):
        returned = BFR4WDserialGUI.sendcommand(self.commandEntry.get())
        self.returnEntry.delete(0,END)
        self.returnEntry.insert(10,returned) 
        self.commandEntry.delete(0,END)
        

    ##################################################################
    # Move Bar clicked event
    ##################################################################
    def moveClick(self,event):
        self.returnEntry.delete(0,END)
        # Speed select bar clicked
        if event.y > 10 and event.y < 40:
            if event.x >= 5 and event.x < 30:
                returned = BFR4WDserialGUI.sendcommand('S2V2')
                self.returnEntry.insert(10,returned)
            elif event.x >= 30 and event.x < 55:
                returned = BFR4WDserialGUI.sendcommand('S2V4')
                self.returnEntry.insert(10,returned)
            elif event.x >= 55 and event.x < 79:
                returned = BFR4WDserialGUI.sendcommand('S2V6')
                self.returnEntry.insert(10,returned)
            elif event.x >= 79 and event.x < 104:
                returned = BFR4WDserialGUI.sendcommand('S2V8')
                self.returnEntry.insert(10,returned)
            elif event.x >= 104 and event.x < 126:
                returned = BFR4WDserialGUI.sendcommand('S2V10')
                self.returnEntry.insert(10,returned)
        #Forward bar clicked
        if event.x > 133 and event.x < 170:
            if event.y >= 5 and event.y < 38:
                returned = BFR4WDserialGUI.sendcommand('W1D50')
                self.returnEntry.insert(10,returned)
            if event.y >= 38 and event.y < 70:
                returned = BFR4WDserialGUI.sendcommand('W1D30')
                self.returnEntry.insert(10,returned)
            if event.y >= 70 and event.y < 102:
                returned = BFR4WDserialGUI.sendcommand('W1D10')
                self.returnEntry.insert(10,returned)
            if event.y >= 102 and event.y < 133:
                returned = BFR4WDserialGUI.sendcommand('W1D5')
                self.returnEntry.insert(10,returned)
        #Reverse bar clicked
            if event.y >= 170 and event.y < 204:
                returned = BFR4WDserialGUI.sendcommand('W2D5')
                self.returnEntry.insert(10,returned)
            if event.y >= 204 and event.y < 235:
                returned = BFR4WDserialGUI.sendcommand('W2D10')
                self.returnEntry.insert(10,returned)
            if event.y >= 235 and event.y < 268:
                returned = BFR4WDserialGUI.sendcommand('W2D30')
                self.returnEntry.insert(10,returned)
            if event.y >= 268 and event.y < 300:
                returned = BFR4WDserialGUI.sendcommand('W2D50')
                self.returnEntry.insert(10,returned)
        #Turn ACW bar clicked
        if event.y > 134 and event.y < 172:
            if event.x >= 5 and event.x < 38:
                returned = BFR4WDserialGUI.sendcommand('W3D120')
                self.returnEntry.insert(10,returned)
            if event.x >= 38 and event.x < 70:
                returned = BFR4WDserialGUI.sendcommand('W3D90')
                self.returnEntry.insert(10,returned)
            if event.x >= 70 and event.x < 102:
                returned = BFR4WDserialGUI.sendcommand('W3D45')
                self.returnEntry.insert(10,returned)
            if event.x >= 102 and event.x < 133:
                returned = BFR4WDserialGUI.sendcommand('W3D30')
                self.returnEntry.insert(10,returned)
        #Turn CW bar clicked
            if event.x >= 170 and event.x < 204:
                returned = BFR4WDserialGUI.sendcommand('W4D30')
                self.returnEntry.insert(10,returned)
            if event.x >= 204 and event.x < 235:
                returned = BFR4WDserialGUI.sendcommand('W4D45')
                self.returnEntry.insert(10,returned)
            if event.x >= 235 and event.x < 268:
                returned = BFR4WDserialGUI.sendcommand('W4D90')
                self.returnEntry.insert(10,returned)
            if event.x >= 268 and event.x < 300:
                returned = BFR4WDserialGUI.sendcommand('W4D120')
                self.returnEntry.insert(10,returned)

            
                
       
    ##################################################################
    # Head move bar clicked event
    ##################################################################
    def headClick(self,event):
        self.returnEntry.delete(0,END)
        # Speed select bar clicked
        if event.y > 10 and event.y < 40:
            if event.x >= 5 and event.x < 30:
                returned = BFR4WDserialGUI.sendcommand('S3V2')
                self.returnEntry.insert(10,returned)
            elif event.x >= 30 and event.x < 55:
                returned = BFR4WDserialGUI.sendcommand('S3V4')
                self.returnEntry.insert(10,returned)
            elif event.x >= 55 and event.x < 79:
                returned = BFR4WDserialGUI.sendcommand('S3V6')
                self.returnEntry.insert(10,returned)
            elif event.x >= 79 and event.x < 104:
                returned = BFR4WDserialGUI.sendcommand('S3V8')
                self.returnEntry.insert(10,returned)
            elif event.x >= 104 and event.x < 126:
                returned = BFR4WDserialGUI.sendcommand('S3V10')
                self.returnEntry.insert(10,returned)
        #Head tilt up clicked
        if event.x > 133 and event.x < 170:
            if event.y >= 5 and event.y < 38:
                returned = BFR4WDserialGUI.sendcommand('H1T75')
                self.returnEntry.insert(10,returned)
            if event.y >= 38 and event.y < 70:
                returned = BFR4WDserialGUI.sendcommand('H1T50')
                self.returnEntry.insert(10,returned)
            if event.y >= 70 and event.y < 102:
                returned = BFR4WDserialGUI.sendcommand('H1T25')
                self.returnEntry.insert(10,returned)
            if event.y >= 102 and event.y < 133:
                returned = BFR4WDserialGUI.sendcommand('H1T10')
                self.returnEntry.insert(10,returned)
        #Centralise head pan and tilt if central section is clicked 
            if event.y >= 133 and event.y < 170:
                returned = BFR4WDserialGUI.sendcommand('H1T0P0')
                self.returnEntry.insert(10,returned)
        #Head tilt down clicked
            if event.y >= 170 and event.y < 204:
                returned = BFR4WDserialGUI.sendcommand('H1T-10')
                self.returnEntry.insert(10,returned)
            if event.y >= 204 and event.y < 235:
                returned = BFR4WDserialGUI.sendcommand('H1T-25')
                self.returnEntry.insert(10,returned)
            if event.y >= 235 and event.y < 268:
                returned = BFR4WDserialGUI.sendcommand('H1T-50')
                self.returnEntry.insert(10,returned)
            if event.y >= 268 and event.y < 300:
                returned = BFR4WDserialGUI.sendcommand('H1T-75')
                self.returnEntry.insert(10,returned)
        #Head pan ACW clicked
        if event.y > 134 and event.y < 172:
            if event.x >= 5 and event.x < 38:
                returned = BFR4WDserialGUI.sendcommand('H1P-75')
                self.returnEntry.insert(10,returned)
            if event.x >= 38 and event.x < 70:
                returned = BFR4WDserialGUI.sendcommand('H1P-50')
                self.returnEntry.insert(10,returned)
            if event.x >= 70 and event.x < 102:
                returned = BFR4WDserialGUI.sendcommand('H1P-25')
                self.returnEntry.insert(10,returned)
            if event.x >= 102 and event.x < 133:
                returned = BFR4WDserialGUI.sendcommand('H1P-10')
                self.returnEntry.insert(10,returned)
        #Head pan CW clicked
            if event.x >= 170 and event.x < 204:
                returned = BFR4WDserialGUI.sendcommand('H1P10')
                self.returnEntry.insert(10,returned)
            if event.x >= 204 and event.x < 235:
                returned = BFR4WDserialGUI.sendcommand('H1P25')
                self.returnEntry.insert(10,returned)
            if event.x >= 235 and event.x < 268:
                returned = BFR4WDserialGUI.sendcommand('H1P50')
                self.returnEntry.insert(10,returned)
            if event.x >= 268 and event.x < 300:
                returned = BFR4WDserialGUI.sendcommand('H1P75')
                self.returnEntry.insert(10,returned)



    def TurnToHeading(self,event):
        self.returnEntry.delete(0,END)
        self.returnEntry.insert(10,'X = ' + str(event.x))  
        self.returnEntry.insert(10,' Y = ' + str(event.y)) 
        #self.compassControl .create_image(0,0, anchor=NW, image=self.compassImg)
        
        curX, curY = (event.x, event.y)
        self.compassControl.create_line(76, 76, curX, curY, fill="black")






        
    def servoOn(self,event):
        returned = BFR4WDserialGUI.sendcommand('S1V1')
        self.returnEntry.delete(0,END)
        self.returnEntry.insert(10,returned) 

    def servoOff(self,event):
        returned = BFR4WDserialGUI.sendcommand('S1V0')
        self.returnEntry.delete(0,END)
        self.returnEntry.insert(10,returned) 

    def CaptureImage(self):
        self.OpenCVImage = BFR4WDOpenCVGui.ReturnFrameRGB()
        self.OpenCVImage = Image.fromarray(self.OpenCVImage)
        self.OpenCVImage = self.OpenCVImage.resize((320, 240), Image.ANTIALIAS)
	self.OpenCVImage = ImageTk.PhotoImage(self.OpenCVImage)
        self.CamImage .create_image(0,0, anchor=NW, image=self.OpenCVImage)
        



root = Tk()
root.title("BFR4WD")
app = Application(master=root)
app.mainloop()
