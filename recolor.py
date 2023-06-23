#color module made for the people using python :)
def color_text(message,rgbarray):
    return f'\x1b[38;2;{";".join(map(str, rgbarray))}m{message}\x1b[0m' #return text for regular printing
def color_log(message,rgbarray):
    print(f'\x1b[38;2;{";".join(map(str, rgbarray))}m{message}\x1b[0m') #print text for you
# import recolor
# colorLog("hello", [0,255,0]) #green
# colorText("Hello World!", [255,0,0]) #red
color_log("Colors Loaded :D", [255,0,0])
