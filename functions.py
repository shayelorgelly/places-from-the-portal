import sys, recolor, os, time
defaultDelay = 35 #ms
#defaultDelay = 0
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

def clearConsole():
    sys.stdout.write("\033c")

def type_writer_color(text, color, delay):
    assert text, "text missing"
    assert color, "color missing..."
    if not delay:
        delay = defaultDelay
    for char in text:
        sleep(delay)
        sys.stdout.write(recolor.colorText(char, color))
        sys.stdout.flush()
def jstypec(words, color, delay): #john smith type
    type_writer_c("John Smith: ", [255,200,], defaultDelay)
    type_writer_c(words, color, delay)
def matchFromArray(str, array):
    out = False
    for x in array:
        if x == str:
            out = True
    if out:
        return True
    else:
        return False
def clear():
    os.system("cls")
    #print("\033c")