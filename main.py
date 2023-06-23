"""yes."""
from functions import *
from scanner import scan  # extra function so i dont need to type it all
from inputv2 import inputv2

# after finished importing and functions
sleep(500)  # wait a sec
clearConsole()
skip_loading = True
if not skip_loading:  # if skiploading is false
    type_writer_color("Places From The Portal", [255, 255, 0], defaultDelay * 1.5)
    type_writer_color("...", [255, 255, 0], 500)
    sleep(500)
    clearConsole()

greetings = ["Hey, ", "Welcome back, ", "Howdy, "]
items = []
jstypec(greetings[1] + "Jim Johnson\n", [255, 255, 255], defaultDelay / 2)
sleep(2000)
jstypec("The portal is nearly done", white, defaultDelay)
type_writer_color("...", white, 500)
type_writer_color("  we just need to make one more component\n", white, defaultDelay)
def portal_room():
    """takes you to the same or different function based on input"""
    x = inputv2("[Travel] [Talk to John Smith]", ["travel", "1", "talk", "2"])
    if matchFromArray(x, ["travel", "1"]):
        # if travelling
        type_writer_color("Where would you like to go?\n", [255, 255, 255], defaultDelay)
        x = inputv2("[Enter the portal] [Back to the portal room]", ["portal", "1", "back", "2"])
        if matchFromArray(x, ["portal", "1"]):
            enterPortal("desert")
            return
        else:
            portal_room()
            return
    elif matchFromArray(x, ["talk", "2"]):
        # talking to npc
        if "Quantum Fabrication Device" in items:
            jstypec("Hey Jim Johnson, you should go and see if the portal works\n", white, defaultDelay)
            portal_room()
            return 
        jstypec("Ive finished making the component, here you go\n", [255, 255, 255], defaultDelay)
        type_writer_color("John Smith has given you a ", [100, 100, 100], defaultDelay)
        type_writer_color('"Quantum Fabrication Device"\n', [255, 0, 255], defaultDelay)
        items.append("Quantum Fabrication Device")
        portal_room()
        return
def desert():
    type_writer_color("You take a look around this unexplored terrain, \n", white, defaultDelay * 2)
    sleep(2000)
    type_writer_color("A hot, dry desert filled with bushes and red sand.\n", white, defaultDelay * 2)
    sleep(2000)
    type_writer_color("A unknown creature wanders infront of you, standing on its tall, furred legs\n", white, defaultDelay * 3)
    sleep(6000)
    type_writer_color("The creature begins to approach you\n", [255, 100, 100], defaultDelay * 6)
    sleep(1000)
    type_writer_color("You pull out your ", [100, 100, 100], defaultDelay * 2)
    type_writer_color("Advanced Scanner Device ", [255, 0, 255], defaultDelay * 2)
    type_writer_color("and begin to scan the creature\n", [100, 100, 100], defaultDelay * 2)
    sleep(750) # 750ms
    scan("Ooragnak")
    ans = inputv2('Do you wish to fight the "Ooragnak"?', ["yes", "no", "y", "n"])
    if ans == "yes" or ans == "y":
        # fighing
        clearConsole()
        type_writer_color("You attempt to punch the Ooragnak", [0, 200, 200], defaultDelay)
        sleep(2000)
        clearConsole()
        type_writer_color("The Ooragnak jumps and kicks you in the head", [0, 200, 200], defaultDelay)
        death()


    elif ans == "no" or ans == "n":
        print('Hi')




def death():
    quit()
def enterPortal(e):
    if "Quantum Fabrication Device" not in items:  #if player doesnt have the item
        # player doesnt have the thing, error report goes here
        type_writer_color("\n...\n", [40, 40, 40], defaultDelay * 16)
        type_writer_color("Portal Activation Sequence Failed\n", [255, 0, 0], defaultDelay * 2)
        type_writer_color("Generating diagnostic report, please wait", [200, 200, 200], defaultDelay * 2)
        sleep(2000)

        type_writer_color('\nComponent Missing: "Quantum Fabrication Device"\n', [25, 200, 255], defaultDelay * 4)  # here we use '' to put the "" in without breaking the code
        portal_room()
        return
    clear()
    type_writer_color("as you awaken, you find yourself adrift in a vast, empty void...", [255, 0, 0], defaultDelay * 4)
    type_writer_color("...\n", [255,0,0], defaultDelay * 8)
    type_writer_color("you experience a sudden rush of air as the space around you begins to collapse\n", [255, 0, 0], defaultDelay * 4)
    type_writer_color("it feels as though the very fabric of space itself is closing in...\n", [255, 0, 0], defaultDelay * 4)
    type_writer_color("the darkness around you begins to swirl and churn...\n", [255, 0, 0], defaultDelay * 4)
    type_writer_color("you feel a sense of impending doom as the void threatens to consume you...\n", [255, 0, 0], defaultDelay * 4)
    sleep(2000)
    clear()
    type_writer_color("*fades to black*", [1, 1, 1], defaultDelay * 4)  # hard to see
    sleep(2000)
    clear()
    type_writer_color("you awaken again, and find yourself in a new location...\n", [255, 0, 0], defaultDelay * 4)
    if e == "desert":
        desert()
    else:
        portal_room()






# start game
# portalRoom()
desert()  # for desert testing