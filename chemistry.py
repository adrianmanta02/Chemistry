from tkinter import *
from PIL import Image, ImageTk

BACKGROUND_COLOR = "#bec3e6"
VOLTMETER = "voltmeter.png"
BOTTLE = "bottle.png"
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
bottle_image = Image.open(BOTTLE)
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
flag = False

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
bottle_naoh = displayImage(xAxis = 1080, yAxis = 180, imageToResize = bottle_image, scale = 0.5)
bottle_h2so4 = displayImage(xAxis = 1180, yAxis = 180, imageToResize = bottle_image, scale = 0.5)
bottle_nacl = displayImage(xAxis = 1280, yAxis = 180, imageToResize = bottle_image, scale = 0.5)
tray = displayImage(xAxis = 550, yAxis = 550, imageToResize = tray_image, scale = 0.9)
iron = displayImage(xAxis = 600, yAxis = 600, imageToResize = FE_image, scale = 0.4)
copper = displayImage(xAxis = 700, yAxis = 600, imageToResize = CU_image, scale = 0.3)
zinc = displayImage(xAxis = 750, yAxis = 600, imageToResize = ZN_image, scale = 0.4)
alluminium = displayImage(xAxis = 880, yAxis = 600, imageToResize = AL_image, scale = 0.4)

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

label_startWarning = Label(text = """Nu putem începe! Asigurați-vă că ați folosit șmirghelul pentru a curăța plăcuțele. 
                        Studenții de dinainte au uitat!""", font=('Times', 14), fg="red", bg=BACKGROUND_COLOR)

def is_any_metal_unclean():
    return any(not clean for clean in metal_clean_status.values())

def unclean():
    return [key for key, clean in metal_clean_status.items() if not clean]

def select_environment(env):
    # if flag == False: 
    #     label_startWarning.place(x= 500, y = 100)
    # else:
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
    if environment == "NaOH":
        bottle = bottle_naoh
    elif environment == "NaCl":
        bottle = bottle_nacl
    else:
        bottle = bottle_h2so4
    pour_solution(bottle_to_pour= bottle)

def select_metal1(metal_input):
    if flag == False: 
        label_startWarning.place(x= 500, y = 100)
    else:   
        global metal1
        metal1 = metal_input
        metal_clean_status[metal1] = False
        if metal1 not in unclean_metals:
            unclean_metals.append(metal1)
        label_metal1.config(text=f"Primul metal selectat: {metal1}")
        label_clean.config(text="Plăcuță de Fe selectată.\nCurăță la schimbarea mediului coroziv!", fg="red")

def select_metal2(metal_input):
    if flag == False: 
        label_startWarning.place(x= 500, y = 100)
    else:   
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
    if flag == False: 
        label_startWarning.place(x= 500, y = 100)
    else:   
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
    if flag == False: 
        label_startWarning.place(x= 500, y = 100)
    else:   
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

import time

def oscillation(image, x, y, offset=20, count=4):
    original_y = y #initial y coordinate
    
    for i in range(count): # doing the up-down movement 'count' times
        y_start = original_y
        y_end = original_y - offset #move the image with a certain number of pixels upper
        
        # start of the animation for going up
        for step in range(21): 
            progress = step / 20
            current_y = y_start + (y_end - y_start) * progress #tracking the current y coordinate
            main_canvas.coords(image, x, current_y) #updating image's position in real time
            window.update() # displaying the changes
            time.sleep(0.02) 
        
        # the image arrived up, now we are setting it to do the same animation on the road down. 
        y_start = original_y - offset
        y_end = original_y
        
        for step in range(21): 
            progress = step / 20
            current_y = y_start + (y_end - y_start) * progress
            main_canvas.coords(image, x, current_y)
            window.update()
            time.sleep(0.02) 

def move_image_smoothly(image, x_start, y_start, x_end, y_end, duration=1.0):
    steps = 50 
    
    for step in range(steps + 1):
        progress = step / steps
        current_x = x_start + (x_end - x_start) * progress
        current_y = y_start + (y_end - y_start) * progress
        
        main_canvas.coords(image, current_x, current_y)
        window.update()
        time.sleep(duration / steps)
     

metals = {
    copper: [700, 600],
    zinc: [750, 600],
    alluminium: [880, 600]
}
def sand():
    global flag
    flag = True
    label_startWarning.config(text="")

    for metal in metals:
        # move the metal on the sandpaper 
        move_image_smoothly(metal, metals[metal][0], metals[metal][1], 600, 600)

        # make the metal move up and down to give the cleaning effect
        oscillation(metal, 20, 650)
    
        # move the metal back on the plate
        move_image_smoothly(metal, 600, 600, metals[metal][0], metals[metal][1])
    
bottles = {
    bottle_h2so4: [1180, 180, 600],
    bottle_naoh: [1080, 180, 440],
    bottle_nacl: [1280, 180, 740]
}   

def rotate_image(image): 
    image_opened = Image.open(image)
    rotated_image = image_opened.rotate(90, expand=True)
    tk_rotated = ImageTk.PhotoImage(rotated_image)
    imagesList.append(tk_rotated) 

    main_canvas.itemconfig(image, image=tk_rotated)

def pour_solution(bottle_to_pour):
    move_image_smoothly(bottle_to_pour, bottles[bottle_to_pour][0], bottles[bottle_to_pour][1], bottles[bottle_to_pour][2], 100)
    rotate_image(BOTTLE)
    window.update()
    
# Buttons

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

Button(text= "Șmirgheluire", font=('times 13 bold'), command=sand).place(x=0, y=600)

window.mainloop()