import pyqrcode
from tkinter import *
from tkinter import messagebox

def generateQR():
    inputString = enterTextField.get()
    scale = enterScaleField.get()
    if len(scale) :
        try :
            scale = int(scale)
        except :
            messagebox.showerror("error",
            "Scale should be integer value ex: 1, 2, 3 ..")
            return
    else :
        scale = 5
    if len(inputString) :
        qrCode = pyqrcode.create(inputString)
        savePath = "/Users/adriantrojanowski/Desktop/QR" + inputString + "_" + str(scale)
        qrCode.svg(SavePath + ".svg", scale = scale)
        qrCode.png(SavePath + ".png", scale = scale)
        messagebox.showInfo('Success', "Your QR code is generated and saved at this path: " + savePath + ".png/.svg")
    else :
        messagebox.showerror("Error", "Text field is empty")