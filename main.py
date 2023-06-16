import recolor, time, sys, os
from inputv2 import inputv2
def clear():
    os.system("cls")
    #print("\033c")
skipLoading = True
defaultDelay = 35 #ms
defaultDelay = 0
white = [255,255,255]
def sleep(ms):
    time.sleep(ms/1000)
def wait(ms):
    sleep(ms)
def delay(ms):
    sleep(ms)
def typeWriter(text, delay):
    assert text, "text missing"
    if not delay:
        delay = defaultDelay
    for char in text:
        sys.stdout.write(char)
        sleep(delay)
def typeWriterC(text, color, delay):
    assert text, "text missing"
    assert color, "color missing..."
    if not delay:
        delay = defaultDelay
    for char in text:
        sleep(delay)
        sys.stdout.write(recolor.colorText(char, color))
        sys.stdout.flush()

def clearConsole():
    sys.stdout.write("\033c")
# after finished importing and functions
sleep(500) #wait a sec
clearConsole()
if not skipLoading: #if skiploading is false
    typeWriterC("Places From The Portal", [255,255,0], defaultDelay * 1.5)# 1.5x slower
    typeWriterC("...", [255,255,0], 500)
    sleep(500)
    clearConsole()
def jstypec(words, color, delay): #john smith type
    typeWriterC("John Smith: ", [255,200,], defaultDelay)
    typeWriterC(words, color, delay)
def matchFromArray(str, array):
    out = False
    for x in array:
        if x == str:
            out = True
    if out:
        return True
    else:
        return False
greetings = ["Hey, ", "Welcome back, ", "Howdy, "]
items = []
jstypec(greetings[1] + "Jim Johnson\n", [255,255,255], defaultDelay /2 )
sleep(2000)
jstypec("The portal is nearly done", white, defaultDelay)
typeWriterC("...", white, 500)
typeWriterC("  we just need to make one more component\n", white, defaultDelay)
def portalRoom():
    x = inputv2("[Travel] [Talk to John Smith]", ["travel", "1", "talk", "2"])
    if matchFromArray(x, ["travel", "1"]):
        #if travelling
        typeWriterC("Where would you like to go?\n", [255,255,255], defaultDelay)
        x = inputv2("[Enter the portal] [Back to the portal room]", ["portal", "1", "back", "2"])
        if matchFromArray(x, ["portal", "1"]):
            enterPortal("desert")
            return
        else:
            portalRoom()
            return
    elif matchFromArray(x, ["talk", "2"]):
        #talking to npc
        if "Quantum Fabrication Device" in items:
            jstypec("Hey Jim Johnson, you should go and see if the portal works\n", white, defaultDelay)
            portalRoom()
            return 
        jstypec("Ive finished making the component, here you go\n", [255,255,255], defaultDelay)
        typeWriterC("John Smith has given you a ", [100,100,100], defaultDelay)
        typeWriterC('"Quantum Fabrication Device"\n', [255,0,255], defaultDelay)
        items.append("Quantum Fabrication Device")
        portalRoom()
        return
def desert():
    print("haiii")
def enterPortal(e):
    if "Quantum Fabrication Device" not in items:# if player doesnt have the item
        # player doesnt have the thing, error report goes here
        typeWriterC("\n...\n", [40,40,40], defaultDelay * 16)
        typeWriterC("Portal Activation Sequence Failed\n", [255,0,0], defaultDelay * 2)
        typeWriterC("Generating diagnostic report, please wait", [200,200,200], defaultDelay * 2)
        sleep(2000)

        typeWriterC('\nComponent Missing: "Quantum Fabrication Device"\n', [25,200,255], defaultDelay * 4)# here we use '' to put the "" in without breaking the code
        portalRoom()
        return
    clear()
    typeWriterC("as you awaken, you find yourself adrift in a vast, empty void...", [255,0,0], defaultDelay * 4)
    typeWriterC("...\n", [255,0,0], defaultDelay * 8)
    typeWriterC("you experience a sudden rush of air as the space around you begins to collapse in on itself.\n", [255,0,0], defaultDelay * 4)
    typeWriterC("it feels as though the very fabric of space itself is closing in...\n", [255,0,0], defaultDelay * 4)
    typeWriterC("the darkness around you starts to swirl and churn...\n", [255,0,0], defaultDelay * 4)
    typeWriterC("you feel a sense of impending doom as the void threatens to consume you...\n", [255,0,0], defaultDelay * 4)
    sleep(2000)
    clearConsole()
    sleep(2000)
    typeWriterC("you awaken again, and find yourself in a new location...\n", [255,0,0], defaultDelay * 4)
    if e == "desert":
        desert()
    else:
        portalRoom()






# start game
portalRoom()