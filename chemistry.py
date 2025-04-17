from tkinter import *
from PIL import Image, ImageTk

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
window.minsize(width=1920, height=1080)
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
    "FE": {"NaOH": 0.42, "NaCl": 0.512, "H2SO4": 0.482},
    "CU": {"NaOH": 0.238, "NaCl": 0.483, "H2SO4": 0.477},
    "ZN": {"NaOH": 0.516, "NaCl": 0.936, "H2SO4": 0.796},
    "AL": {"NaOH": 1.11, "NaCl": 0.658, "H2SO4": 0.622}
}

metal_clean_status = {
    "FE": True,
    "CU": True,
    "ZN": True,
    "AL": True
}

unclean_metals = []
environment = None
metal1 = None
metal2 = None

def ResizeImage(imageToResize, scale):
    width = int(imageToResize.width * scale)
    height = int(imageToResize.height * scale)
    resized_image = imageToResize.resize((width, height))
    return [resized_image, width, height]

def displayImage(xAxis, yAxis, imageToResize, scale):
    image_list = ResizeImage(imageToResize, scale)
    imageToDisplay = ImageTk.PhotoImage(image_list[0])
    imagesList.append(imageToDisplay)
    image = main_canvas.create_image(xAxis, yAxis, image=imageToDisplay, anchor="nw")
    return image

water = displayImage(xAxis = 1150, yAxis = 600, imageToResize = distillerWater_image, scale = 0.6)
sandpaper = displayImage(xAxis = 0, yAxis= 600, imageToResize = sandpaper_image, scale = 0.6)
container1 = displayImage(xAxis = 300, yAxis= 300, imageToResize = container_image, scale = 0.4)
container2 = displayImage(xAxis = 500, yAxis= 300, imageToResize = container_image, scale = 0.4)
container3 = displayImage(xAxis = 700, yAxis= 300, imageToResize = container_image, scale = 0.4)
voltmeter = displayImage(xAxis = 50, yAxis= 200, imageToResize = voltmeter_image, scale = 0.45)
bottles = displayImage(xAxis = 1050, yAxis = 150, imageToResize = bottles_image, scale = 0.6)
tray = displayImage(xAxis = 550, yAxis = 550, imageToResize = tray_image, scale = 0.9)
iron = displayImage(xAxis = 600, yAxis = 600, imageToResize = FE_image, scale = 0.4)
copper = displayImage(xAxis = 700, yAxis = 600, imageToResize = CU_image, scale = 0.3)
zinc = displayImage(xAxis = 750, yAxis = 600, imageToResize = ZN_image, scale = 0.4)
alluminium = displayImage(xAxis = 900, yAxis = 600, imageToResize = AL_image, scale = 0.4)

label_env = Label(text="Mediu coroziv selectat: N/A", font=('Times', 14), bg=BACKGROUND_COLOR)
label_env.place(x=1140, y=400)

label_metal1 = Label(text="Primul metal selectat: N/A", font=('Times', 14), bg=BACKGROUND_COLOR)
label_metal1.place(x=300, y=700)

label_metal2 = Label(text="Al doilea metal selectat: N/A", font=('Times', 14), bg=BACKGROUND_COLOR)
label_metal2.place(x=300, y=800)

label_clean = Label(text="Plăcutele sunt curate.", font=('Times', 14), fg="green", bg=BACKGROUND_COLOR)
label_clean.place(x=500, y=100)

label_voltage = Label(text= "Ultima tensiune măsurată: ", font=('Times', 14), bg=BACKGROUND_COLOR)
label_voltage.place(x=500, y=200)

label_clean.place(x=1000, y=510)
label_voltage.place(x=450, y=505)


def is_any_metal_unclean():
    return any(not clean for clean in metal_clean_status.values())

def unclean():
    return [key for key, clean in metal_clean_status.items() if not clean]

def select_environment(env):
    global environment
    if environment is not None and env != environment and is_any_metal_unclean():
        label_clean.config(
            text=f"Curăță toate plăcuțele înainte de a schimba mediul!\nPlăcuțe necurățate: {', '.join(unclean())}",
            fg="red"
        )
        return
    environment = env
    label_env.config(text=f"Mediu coroziv selectat: {environment}")
    label_clean.config(text="Plăcutele sunt curate.", fg="green")

def select_metal1(metal_input):
    global metal1
    metal1 = metal_input
    metal_clean_status[metal1] = False
    if metal1 not in unclean_metals:
        unclean_metals.append(metal1)
    label_metal1.config(text=f"Primul metal selectat: {metal1}")
    label_clean.config(text="Plăcuță de Fe selectată.\nCurăță la schimbarea mediului coroziv!", fg="red")

def select_metal2(metal_input):
    global metal2
    metal2 = metal_input
    if metal_clean_status[metal2]:
        metal_clean_status[metal2] = False
        if metal2 not in unclean_metals:
            unclean_metals.append(metal2)
        label_metal2.config(text=f"Al doilea metal selectat: {metal2}")
        label_clean.config(text="Plăcuță nouă selectată. Curăță după utilizare!", fg="red")
    else:
        label_metal2.config(text="Al doilea metal selectat: eroare.")
        label_clean.config(text="Plăcuța trebuie curățată mai întâi!", fg="red")

def clean(metal):
    global unclean_metals
    metal_clean_status[metal] = True
    if metal in unclean_metals:
        unclean_metals.remove(metal)
    label_clean.config(text=f"Plăcuța {metal} a fost curățată", fg="green")
    if metal is metal1:
        label_metal1.config(text="Primul metal selectat: N/A")
    elif metal is metal2:
        label_metal2.config(text = "Al doilea metal selectat: N/A")

def calculate_results():
    if environment is None:
        print("Nu a fost selectat niciun mediu coroziv!")
    elif metal1 is None and metal2 is None:
        print("Selectați cele două metale (Fe + X), unde X poate fi (Cu, Zn, Al, -)")
    elif metal1 is None:
        print("Selectați Fe ca prim metal!")
    else:
        if metal2 is None:
            label_voltage.config(text = f"Ultima tensiune măsurată este: {dictionary[metal1][environment]}V")
        else:
            label_voltage.config(text = f"Ultina tensiune măsurată este: {dictionary[metal2][environment]}V")

def reset():
    global metal1, metal2
    metal1 = None
    metal2 = None
    label_metal1.config(text = "Primul metal selectat: N/A")
    label_metal2.config(text = "Al doilea metal selectat: N/A")

def move_image(image, x, y, targetX, targetY): 
    speed = 10

    new_x = x + speed if x < targetX else x - speed if x > targetX else x
    new_y = y + speed if y < targetY else y - speed if y > targetY else y

    if abs(new_x - targetX) < speed:
        new_x = targetX
    if abs(new_y - targetY) < speed:
        new_y = targetY

    main_canvas.coords(image, new_x, new_y)

    if new_x != targetX or new_y != targetY:
        main_canvas.after(20, lambda: move_image(image, new_x, new_y, targetX, targetY))
    else:
        image_opened = Image.open(image)
        rotated_image = image_opened.rotate(90, expand=True)
        tk_rotated = ImageTk.PhotoImage(rotated_image)
        imagesList.append(tk_rotated) 

        main_canvas.itemconfig(image, image=tk_rotated)

move_image(sandpaper, 0,600, 0, 0)

# Butoane

Button(text="NaOH 0.1M", width=10, font=('times 10 bold'), command=lambda: select_environment("NaOH"), borderwidth=0).place(x=1097, y=300)
Button(text="H2SO4 0.1M", width=10, font=('times 10 bold'), command=lambda: select_environment("H2SO4"), borderwidth=0).place(x=1200, y=300)
Button(text="NaCl 1%", width=10, font=('times 10 bold'), command=lambda: select_environment("NaCl"), borderwidth=0).place(x=1303, y=300)

Button(text="FE", width=7, font=('times 13 bold'), command=lambda: select_metal1("FE"), borderwidth=0).place(x=600, y=820)
Button(text="CU", width=7, font=('times 13 bold'), command=lambda: select_metal2("CU"), borderwidth=0).place(x=700, y=820)
Button(text="ZN", width=7, font=('times 13 bold'), command=lambda: select_metal2("ZN"), borderwidth=0).place(x=800, y=820)
Button(text="AL", width=7, font=('times 13 bold'), command=lambda: select_metal2("AL"), borderwidth=0).place(x=900, y=820)

Button(text="Curăță FE", width=10, command=lambda: clean("FE")).place(x=1100, y=650)
Button(text="Curăță CU", width=10, command=lambda: clean("CU")).place(x=1100, y=700)
Button(text="Curăță ZN", width=10, command=lambda: clean("ZN")).place(x=1100, y=750)
Button(text="Curăță AL", width=10, command=lambda: clean("AL")).place(x=1100, y=800)

Button(text="Calculează", font=('times 13 bold'), command=calculate_results).place(x=850, y=480)
Button(text="Resetează", font=('times 13 bold'), command=reset).place(x=850, y=520)

window.mainloop()