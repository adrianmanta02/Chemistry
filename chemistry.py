from tkinter import *
from PIL import Image, ImageTk #used for scaling images
# import pandas

BACKGROUND_COLOR = "#bec3e6"
VOLTMETER = "voltmeter.png"
BOTTLES = "bottles.png"
FE = "FE.png"
ZN = "ZN.png"
AL = "AL.png"
CU = "CU.png"

window = Tk()
window.minsize(width = 1920, height = 1080)
window.title("Protecția catodică cu anozi de sacrificiu")
window.config(bg = BACKGROUND_COLOR)

imagesList = []
voltmeter_image = Image.open(VOLTMETER)
bottles_image = Image.open(BOTTLES)
FE_image = Image.open(FE)
CU_image = Image.open(CU)
ZN_image = Image.open(ZN)
AL_image = Image.open(AL)

def ResizeImage(imageToResize, scale):
    width = int(imageToResize.width * scale)
    height = int(imageToResize.height * scale)
    resized_image = imageToResize.resize((width, height))
    list = [resized_image, width, height]
    return list

def displayImage(canvWid, canvHei, xAxis, yAxis, imageToResize, scale):
    image_list = ResizeImage(imageToResize, scale)
    imageToDisplay = ImageTk.PhotoImage(image_list[0])
    
    imagesList.append(imageToDisplay)

    canvas_image = Canvas(width = canvWid, height = canvHei)
    canvas_image.create_image(image_list[1] // 2 , image_list[2] // 2 , image = imageToDisplay)
    canvas_image.config(bg = BACKGROUND_COLOR, highlightthickness = 0)
    canvas_image.place(x = xAxis, y = yAxis)

displayImage(canvWid = 200, canvHei= 400, xAxis= 0, yAxis= 300, imageToResize = voltmeter_image, scale = 0.3)
displayImage(canvWid = 400, canvHei= 500, xAxis = 200, yAxis = 300, imageToResize = bottles_image, scale = 0.6)
displayImage(canvWid = 200, canvHei= 400, xAxis = 600, yAxis = 300, imageToResize = FE_image, scale = 0.4)
displayImage(canvWid = 200, canvHei= 400, xAxis = 700, yAxis = 300, imageToResize = CU_image, scale = 0.3)
displayImage(canvWid = 200, canvHei= 400, xAxis = 800, yAxis = 300, imageToResize = ZN_image, scale = 0.4)
displayImage(canvWid = 200, canvHei= 400, xAxis = 900, yAxis = 300, imageToResize = AL_image, scale = 0.4)

def action():
    pass 

def button(button, action):
    pass

window.mainloop()