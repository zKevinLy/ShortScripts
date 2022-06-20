import pygetwindow
import pytesseract
import pyautogui
import time
import cv2


# Input Info here
pytesseract.pytesseract.tesseract_cmd = r"K:\PyTesseract\tesseract.exe"
img_location = r"C:\Users\snip.png"

#selecting game window and screen position
progName = "multiplayer" #or Minecraft window name
openPrograms = pygetwindow.getAllTitles()
prog = [prog for prog in openPrograms if progName.lower() in prog.lower()][0]
progSpecs = pygetwindow.getWindowsWithTitle(prog)[0]

x,y,width,height = progSpecs.left,progSpecs.top,progSpecs.width,progSpecs.height
print(progSpecs)

width +=x
height +=y


#select how many pixels to crop (for subtitle)
portionSize = 250
fishCaught = 1

while(1):
    #take screenshot
    pyautogui.screenshot(img_location, region = (width-portionSize,height-portionSize,portionSize,portionSize))

    #read for text
    img = cv2.imread(img_location)
    text = pytesseract.image_to_string(img)
    text = " ".join([i for i in text.split()]).lower()
    # print(text)
    if "splashes"in text:
        pyautogui.click(button = "right")
        time.sleep(0.5)
        pyautogui.click(button = "right")
        # print(fishCaught, text)
        fishCaught +=1
        time.sleep(2)