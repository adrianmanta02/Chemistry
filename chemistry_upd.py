from tkinter import *
from PIL import Image, ImageTk  # used for scaling images

# import pandas

BACKGROUND_COLOR = "#bec3e6"
VOLTMETER = "voltmeter.png"
BOTTLES = "bottles.png"
FE = "FE.png"
ZN = "ZN.png"
AL = "AL.png"
CU = "CU.png"
tray = "tray.png"
container = "container.png"
distillerWater = "distilledWater.png"
sandpaper = "sandpaper.png"

window = Tk()
window.minsize(width=1280, height=1440)
window.title("Protecția catodică cu anozi de sacrificiu")
window.config(bg=BACKGROUND_COLOR)

imagesList = []
voltmeter_image = Image.open(VOLTMETER)
bottles_image = Image.open(BOTTLES)
FE_image = Image.open(FE)
CU_image = Image.open(CU)
ZN_image = Image.open(ZN)
AL_image = Image.open(AL)
tray_image = Image.open(tray)
container_image = Image.open(container)
distillerWater_image = Image.open(distillerWater)
sandpaper_image = Image.open(sandpaper)

main_canvas = Canvas(window, width=1920, height=1080, bg=BACKGROUND_COLOR, highlightthickness=0)
main_canvas.place(x=0, y=0)

dictionary = {
    "NaCl":
        {
            "FE": 0.512,
            "CU": 0.483,
            "ZN": 0.936,
            "AL": 0.658
        },
    "H2SO4":
        {
            "FE": 0.482,
            "CU": 0.477,
            "ZN": 0.796,
            "AL": 0.622
        },
    "NaOH":
        {
            "FE": 0.420,
            "CU": 0.238,
            "ZN": 0.516,
            "AL": 1.110
        }
}


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
    main_canvas.create_image(xAxis, yAxis, image=imageToDisplay, anchor="nw")

    # canvas_image = Canvas(width=canvWid, height=canvHei)
    # canvas_image.create_image(image_list[1] // 2, image_list[2] // 2, image=imageToDisplay)
    # canvas_image.config(bg=BACKGROUND_COLOR, highlightthickness=0)
    # canvas_image.place(x=xAxis, y=yAxis)


displayImage(canvWid = 400, canvHei= 500, xAxis = 1150, yAxis = 600, imageToResize = distillerWater_image, scale = 0.6)
displayImage(canvWid = 200, canvHei= 400, xAxis = 0, yAxis= 600, imageToResize = sandpaper_image, scale = 0.6)
displayImage(canvWid = 200, canvHei= 400, xAxis = 300, yAxis= 300, imageToResize = container_image, scale = 0.4)
displayImage(canvWid = 200, canvHei= 400, xAxis = 500, yAxis= 300, imageToResize = container_image, scale = 0.4)
displayImage(canvWid = 200, canvHei= 400, xAxis = 700, yAxis= 300, imageToResize = container_image, scale = 0.4)
displayImage(canvWid = 200, canvHei= 400, xAxis = 50, yAxis= 200, imageToResize = voltmeter_image, scale = 0.45)
displayImage(canvWid = 400, canvHei= 500, xAxis = 1050, yAxis = 150, imageToResize = bottles_image, scale = 0.6)
displayImage(canvWid = 600, canvHei= 400, xAxis = 550, yAxis = 550, imageToResize = tray_image, scale = 0.9)
displayImage(canvWid = 200, canvHei= 400, xAxis = 600, yAxis = 600, imageToResize = FE_image, scale = 0.4)
displayImage(canvWid = 200, canvHei= 400, xAxis = 700, yAxis = 600, imageToResize = CU_image, scale = 0.3)
displayImage(canvWid = 200, canvHei= 400, xAxis = 750, yAxis = 600, imageToResize = ZN_image, scale = 0.4)
displayImage(canvWid = 200, canvHei= 400, xAxis = 900, yAxis = 600, imageToResize = AL_image, scale = 0.4)

label_env = Label(text="Mediu coroziv selectat: N/A", font=('Times', 14), bg=BACKGROUND_COLOR)
label_env.place(x=1140, y=400)

label_metal1 = Label(text="Primul metal selectat: N/A", font=('Times', 14), bg=BACKGROUND_COLOR)
label_metal1.place(x=300, y=700)

label_metal2 = Label(text="Al doilea metal selectat: N/A", font=('Times', 14), bg=BACKGROUND_COLOR)
label_metal2.place(x=300, y=800)

label_clean = Label(text="Placuta nu trebuie curatata.", font=('Times', 14), bg=BACKGROUND_COLOR)
label_clean.place(x=500, y=100)

environment = None
metal1 = None
metal2 = None


def select_environment(env):
    global environment
    environment = env
    label_env.config(text=f"Mediu coroziv selectat: {environment}")


button_NaCl = Button(text="NaCl 1%", width=10, font=('times 10 bold'), command=lambda: select_environment("NaCl"), borderwidth=0)
button_NaCl.config(activebackground=BACKGROUND_COLOR)
button_NaCl.place(x=1097, y=300)


button_H2SO4 = Button(text="H2SO4 0.1M", width=10, font=('times 10 bold'), command=lambda: select_environment("H2SO4"), borderwidth=0)
button_H2SO4.config(activebackground=BACKGROUND_COLOR)
button_H2SO4.place(x=1200, y=300)

button_NaOH = Button(text="NaOH 0.1M", width=10, font=('times 10 bold'), command=lambda: select_environment("NaOH"), borderwidth=0)
button_NaOH.config(activebackground=BACKGROUND_COLOR)
button_NaOH.place(x=1303, y=300)




def select_metal1(metal_input):
    global metal1
    metal1 = metal_input
    label_metal1.config(text=f"Primul metal selectat: {metal1}")


def select_metal2(metal_input):
    global metal2
    metal2 = metal_input
    label_metal2.config(text=f"Al doilea metal selectat: {metal2}")


def clean(flag):
    global is_cleaned
    is_cleaned = flag
    label_clean.config(text=f"Placuta a fost curatata")


label_clean.place(x=1190, y=510)

button_FE = Button(text="FE", width=7, font=('times 13 bold'), command=lambda: select_metal1("FE"), borderwidth=0)
button_FE.config(activebackground=BACKGROUND_COLOR)
button_FE.place(x=600, y=820)

button_CU = Button(text="CU", width=7, font=('times 13 bold'), command=lambda: select_metal2("CU"), borderwidth=0)
button_CU.config(activebackground=BACKGROUND_COLOR)
button_CU.place(x=700, y=820)

button_ZN = Button(text="ZN", width=7, font=('times 13 bold'), command=lambda: select_metal2("ZN"), borderwidth=0)
button_ZN.config(activebackground=BACKGROUND_COLOR)
button_ZN.place(x=800, y=820)

button_AL = Button(text="AL", width=7, font=('times 13 bold'), command=lambda: select_metal2("AL"), borderwidth=0)
button_AL.config(activebackground=BACKGROUND_COLOR)
button_AL.place(x=900, y=820)

button_clean = Button(text="Curata placuta", width=13, font=('times 13 bold'), command=lambda: clean(1), borderwidth=0)
button_clean.config(activebackground=BACKGROUND_COLOR)
button_clean.place(x=1215, y=570)


def calculate_results():
    if environment is None:
        print("Nu a fost selectat niciun mediu coroziv!")
    elif metal1 is None and metal2 is None:
        print("Selectati cele doua metale (Fe + X), unde X poate fi (Cu, Zn, Al, -)")
    elif metal1 is None:
        print("Selectati Fe ca prim metal!")
    else:
        if metal2 is None:
            print(f"Tensiunea masurata este: {dictionary[environment][metal1]}")
        else:
            print(f"Tensiunea masurata este {dictionary[environment][metal2]}")


buton_calculeaza = Button(text="Calculează", command=calculate_results)
buton_calculeaza.place(x=500, y=600)

window.mainloop()