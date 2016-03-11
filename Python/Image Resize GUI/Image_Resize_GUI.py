#!/usr/bin/python3
#Python Final Practical
#This is a GUI to resize images for The Tech Academy

from tkinter import *
from tkinter import ttk, filedialog
from PIL import ImageTk, Image


class GUIwindow():
    def __init__(self, master):
        #grab screen size
        self.screenWidth, self.screenHeight = master.winfo_screenwidth(), master.winfo_screenheight()
        #title, size, and color window
        master.title("Image Resize GUI")
        master.geometry("{}x{}".format(self.screenWidth, self.screenHeight))
        master.configure(background = 'SteelBlue1')
        #create user interface
        self.createUI(master)


    def createUI(self,master):
        #create style object
        self.style = ttk.Style()
        #configure widget styles
        self.style.configure('TFrame', background = 'SteelBlue1')
        self.style.configure('TButton', background = 'SteelBlue1', font = ('Verdana', 10))
        self.style.configure('TLabel', background = 'SteelBlue1', font = ('Verdana', 10))
        self.style.configure('TScale', background = 'SteelBlue1')

        #create master frame
        self.masterFrame = ttk.Frame(master)
        self.masterFrame.pack()
        #create image frame
        self.imageFrame = ttk.Frame(self.masterFrame)
        self.imageFrame.pack(pady = 5)
        #create control frame
        self.controlFrame = ttk.Frame(self.masterFrame)
        self.controlFrame.pack()

        #create width and height variables for scalebars
        self.widthVar = IntVar()
        self.heightVar = IntVar()

        #create scale labels and scalebars
        self.widthLabel = ttk.Label(self.controlFrame, text = 'Width:')
        self.widthLabel.grid(row = 0, column = 0)
        self.widthScale = ttk.Scale(self.controlFrame, orient = HORIZONTAL, from_ = 1, to_ = self.screenWidth - 200, \
            length = 1024, variable = self.widthVar, command = self.changeWidth)
        self.widthScale.grid(row = 0, column = 1, columnspan = 9, pady = 5)

        self.heightLabel = ttk.Label(self.controlFrame, text = 'Height:')
        self.heightLabel.grid(row = 1, column = 0)
        self.heightScale = ttk.Scale(self.controlFrame, orient = HORIZONTAL, from_ = 1, to_ = self.screenHeight - 200, \
            length = 1024, variable = self.heightVar, command = self.changeHeight)
        self.heightScale.grid(row = 1, column = 1, columnspan = 9, pady = 5)

        #create scale pixel labels
        self.widthPixels = ttk.Label(self.controlFrame, text = self.widthVar.get())
        self.widthPixels.grid(row = 0, column = 10)
        self.heightPixels = ttk.Label(self.controlFrame, text = self.heightVar.get())
        self.heightPixels.grid(row = 1, column = 10)
        
        #create open and save buttons
        self.openButton = ttk.Button(self.controlFrame, text = 'Open Image', command = self.openImage)
        self.openButton.grid(row = 2, column = 4, pady = 5)
        self.saveButton = ttk.Button(self.controlFrame, text = 'Save Image', comman = self.saveImage)
        self.saveButton.grid(row = 2, column = 6, pady = 5)

        #set image present variable to off (0)
        self.imagePresent = 0

        #set number of saves to 1
        self.saveNum = 1
        
       
    def changeWidth(self, value):
        #check to make sure width isn't 0
        if value != 0:
            #grabs value from widthScale and rounds it
            self.newWidth = round(float(value))
            #create text for widthPixels label
            self.newWidthText = str(self.newWidth) + ' px'
            #update widthPixels label
            self.widthPixels.configure(text = self.newWidthText)
            #get current width and height as integers
            self.currentWidth = int(self.newWidth)
            self.currentHeight = int(self.heightScale.get())
            #check to make sure height isn't 0
            if self.currentHeight != 0 and self.imagePresent == 1:
                #resize image
                self.newImage = self.openImage.resize((self.currentWidth, self.currentHeight), Image.ANTIALIAS)
                #make resized image object
                self.Image = ImageTk.PhotoImage(self.newImage)
                #update image label
                self.imageLabel.configure(image = self.Image)


    def changeHeight(self, value):
        #check to make sure height isn't 0
        if value != 0:
            #grabs value from heightScale and rounds it
            self.newHeight = round(float(value))
            #create text for heightPixels label
            self.newHeightText = str(self.newHeight) + ' px'
            #update heightPixels label
            self.heightPixels.configure(text = self.newHeightText)
            #get current width and height as integers
            self.currentHeight = int(self.newHeight)
            self.currentWidth = int(self.widthScale.get())
            #make sure width isn't 0
            if self.currentWidth != 0 and self.imagePresent == 1:
                #resize image
                self.newImage = self.openImage.resize((self.currentWidth, self.currentHeight), Image.ANTIALIAS)
                #create resized image object
                self.Image = ImageTk.PhotoImage(self.newImage)
                #update image label
                self.imageLabel.configure(image = self.Image)


    def openImage(self):
        #create file dialog to open image
        self.imgName = filedialog.askopenfilename()
        #open image
        self.openImage = Image.open(self.imgName)
        #get image file type
        self.imgType = str(self.openImage.format)

        #get image size
        self.imageWidth, self.imageHeight = self.openImage.size
        #if image proportions are too big, shrink them to max
        if self.imageWidth > self.screenWidth:
            self.imageWidth = self.screenWidth - 200
        if self.imageHeight > self.screenHeight:
            self.imageHeight = self.screenHeight - 200

        #create default image object for label
        self.Image = ImageTk.PhotoImage(self.openImage)
        #create  image label
        self.imageLabel = ttk.Label(self.imageFrame, image = self.Image)
        self.imageLabel.grid(row = 0, column = 0)

        #set scalebars to default image size
        self.widthScale.set(self.imageWidth)
        self.heightScale.set(self.imageHeight)

        #set image present variable to on (1)
        self.imagePresent = 1



    def saveImage(self):
        #check to see if image has been resized before allowing saving
        if self.newImage:
            #set image name to save based on number of saves and file type
            self.saveImageName = 'resized image' + str(self.saveNum) + '.' + self.imgType
            #save image
            self.newImage.save(self.saveImageName, quality = 100)
            #increase number of saves
            self.saveNum += 1
        else:
            pass


def main():
    root = Tk()
    window = GUIwindow(root)
    root.mainloop()

if __name__ == "__main__": main()