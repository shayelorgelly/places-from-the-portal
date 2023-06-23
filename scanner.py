from functions import typeWriterC, sleep, defaultDelay
def scan(creature_name):
    typeWriterC("Scanning Creature", [255,255,0], defaultDelay * 2)
    typeWriterC("......\n", [255, 255,0], 750)# 750 miliseconds
    sleep(1000)
    typeWriterC("....Scanner Results.....\n", [150,0,255], defaultDelay * 2)
    typeWriterC("Species: ", [255,255,255], defaultDelay * 2)
    typeWriterC("       " + creature_name, [255,255,255], defaultDelay * 2)
    print("\n")

