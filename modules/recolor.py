#color module made for the people using python :)
def colorText(message,rgbarray):
    return f'\x1b[38;2;{";".join(map(str, rgbarray))}m{message}\x1b[0m'
def colorLog(message,rgbarray):
    print(f'\x1b[38;2;{";".join(map(str, rgbarray))}m{message}\x1b[0m')
# import recolor
# colorLog("hello", [0,255,0]) #green
# colorText("Hello World!", [255,0,0]) #red