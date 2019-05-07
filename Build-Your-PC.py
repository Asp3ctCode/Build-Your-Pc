'''Tyler Goodrich
3/13/19
This program will take your budget and it will give you the specs of what pc you should build.'''
import pygame
import pygame.freetype
from pygame.locals import *

pygame.init()
xres = 1024
yres = 768
gameDisplay = pygame.display.set_mode((xres, yres))
pygame.display.set_caption('Idle Shooter')
pause = False
gameExit = False

gray = (200, 200, 200)
black = (0, 0, 0)
white = (255, 255, 255)
peach = (224, 134, 81)
red = (200, 0, 0)
green = (0, 200, 0)
orange = (200,100,50)
trans = (1,1,1)
brown = (139,69,19)


dark_gray = (100,100,100)
darkish_peach = (210,110,61)
dark_peach = (204, 104, 51)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)


fontsmall = pygame.freetype.Font(None, 24)
fontlarge = pygame.freetype.Font(None, 100)
game_font = pygame.freetype.Font(None, 24)

# If they print something else it says there budget is too low.

price = True

while price:
    print("Congrats!!")
    break
# Prints Congrats after specs.

def text_objects(text, font):
    textSurface = font.render(str(text), True, black)
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, ic, ac, action=None, bordercolor = None):
    # this gets the mouse's position
    mouse = pygame.mouse.get_pos()
    # This gets when the mouse clicks, it makes a list like this: [1,1,1]
    # left, middle, right, 1 is active, 0 is inactive
    click = pygame.mouse.get_pressed()

    # If mouse[0] or left click is between the box then draw the active color
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        # If the click is left then do the action that is called
        if click[0] == 1 and action != None:
            action()
    # If not draw the box with  the inactive color.
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

   # This calls a small text. It goes the font then font size
    smallText = pygame.font.Font("freesansbold.ttf", 20)

    # no clue just do it
    textSurf, textRect = text_objects(msg, smallText)
    # This makes the text in the center of the button
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    # Draws something on screen
    gameDisplay.blit(textSurf, textRect)
    if bordercolor != None:
        pygame.draw.rect(gameDisplay,bordercolor,(x,y,w,h),2)
clock = pygame.time.Clock()


def get_key():
    while 1:
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            return event.key
        else:
            pass


def changeVal(keyIndex):
    global valList
    tempstr = str(valList[keyIndex])
    while True:
        inkey = get_key()
        if inkey == K_BACKSPACE:
            tempstr = tempstr[:-1]

        elif inkey == K_RETURN:
            game_intro()
        elif inkey > 47 and inkey < 58:
            tempstr += chr(inkey)
        try:
            valList[keyIndex] = int(tempstr)
        except ValueError:
            valList[keyIndex]= 0
        buttonList()

def changeValLetter(keyIndex):
    global valList
    tempstr = str(valList[keyIndex])
    while True:
        inkey = get_key()
        if inkey == K_BACKSPACE:
            tempstr = tempstr[:-1]

        elif inkey == K_RETURN:
            game_intro()
        elif inkey > 47 and inkey <58:
            tempstr += chr(inkey)
        try:
            valList[keyIndex] = int(tempstr)
        except ValueError:
            valList[keyIndex]= 0
        buttonList()
valList = [0,0,0,0,0]
def changeBudget():
    changeVal(0)
def changeFavorite():
    changeValLetter(1)
def game_intro():
    global gamemode
    # This is needed for the while loop
    intro = True
    gamemode = 'game_intro'
    while intro:
        # Always put this so they can exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()

        # This makes the game gray
        gameDisplay.fill(gray)
        # fontsmall.render_to(gameDisplay, (100, 200), var, (black))


        # The two buttons on this page, remember not to put the () in the function being called





        # Needed for the game to run
        buttonList()
        clock.tick(15)
def buttonList():
    button("Budget: "+ str(valList[0]), 320, 450, 230, 60, green, bright_green, changeBudget)
    button("Favorite Games: " + str(valList[1]),320, 550, 230, 60, green, bright_green,changeFavorite)
    pygame.display.update()

game_intro()
'''
games = 0
if valList[0] >= 450 and valList[0] <= 500:
    print("Perfect Budget and Great Choice of games.")
    print("These are your specs, Mother Board:Processer: Gigabyte B250M-DS3H Intel i3 7100 GPU: Gtx 980  Ram: 4gb ballistix ddr4 Case: Thermaltake CA-1B3-00M1NN-00 Versa")
    print("   ")
    
elif valList[0] >= 501 and valList[0] <= 600:
    print("Perfect Budget and Great Choice of games.")
    print("These are your specs, Mother Board: ASRock Z390 Pro4 LGA 1151 Processer: Intel i5 7700. GPU: Gtx 980. Ram: 4gb ballistix. ddr4 Case:Cooler Master MasterBox Lite 3.1 ")
    print("   ")

# Prints specs of desired budget PC.

elif valList[0] >= 601 and valList[0] <= 700:
    print("Perfect Budget and Great Choice of games.")
    print("These are your specs, Mother Board: ASRock Z390 Pro4 LGA 1151  Processer: Intel i5 7700. GPU: GTX 1050 Ti. Ram: 8gb ballistix ddr4. Case: NZXT H500 – Compact ATX Mid-Tower Case ")
    print("   ")

elif valList[0] >= 701 and valList[0] <= 900:
    print("Perfect Budget and Great Choice of games.")
    print("These are your specs, Mother Board: Processer: ASRock Z390 Pro4 LGA 1151 Intel i5 7700. GPU: GTX 1060 3gb. Ram: 8gb ballistix ddr4. Case: NZXT H500 – Compact ATX Mid-Tower Case ")
    print("   ")

elif valList[0] >= 901 and valList[0] <= 1100:
    print("Perfect Budget and Great Choice of games.")
    print("These are your specs, Mother Board: ASRock Z390 Pro4 LGA 1151 Processer: Intel i5 7700. GPU: GTX 1060 8gb. Ram: 8gb ballistix ddr4. Case: Phanteks Eclipse Steel ATX Mid Tower ")
    print("   ")

elif valList[0] >= 1101 and valList[0] <= 1400:
    print("Perfect Budget and Great Choice of games.")
    print("These are your specs, Mother Board: ASRock Z390 Pro4 LGA 1151 Processer: Intel i5 7700k. GPU: GTX 1060 Ti. Ram: 16gb ballistix ddr4. Case: Phanteks Eclipse Steel ATX Mid Tower ")
    print("   ")

elif valList[0] >= 1401 and valList[0] <= 1600:
    print("Perfect Budget and Great Choice of games.")
    print("These are your specs, Mother Board: ASUS ROG Strix Z390-E Gaming   Processer: Intel i7. GPU: GTX 1070 Ti. Ram: 16gb ballistix ddr4. Case: CORSAIR Carbide 275R Mid-Tower Gaming Case ")
    print("  ")

elif valList[0] >= 1601 and valList[0] <= 2000:
    print("Perfect Budget and Great Choice of games.")
    print("These are your specs, Mother Board: ASUS ROG Strix Z390-E Gaming   Processer: Intel i7. GPU: GTX 1070 Ti. Ram: 16gb ballistix ddr4. Case: CORSAIR Carbide 275R Mid-Tower Gaming Case ")
    print("  ")

elif valList[0] >= 2001 and valList[0] <= 2500:
     print("Perfect Budget and Great Choice of games.")
     print("These are your specs, Mother Board: B360 AORUS GAMING 3 Processer: Intel i7. GPU: GTX 1080 Ti. Ram: 16gb ballistix ddr4. Case: NZXT H500i Compact ATX PC Gaming Case - RGB LED - White/Black ")
     print("  ")

elif valList[0] >= 2501 and valList[0] <= 3000:
    print("Perfect Budget and Great Choice of games.")
    print("These are your specs, Mother Board:Intel Z390 Processer: Intel i9. GPU: GTX 2080 Ti. Ram: 32gb ballistix ddr4. Case: NZXT H700 - ATX PC Gaming Case ")
    print("  ")

else:
    print('Budget too low.')
    print("   ")
'''
