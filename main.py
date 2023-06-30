"""Made by Shaye Lorgelly"""
from functions import *
from scanner import scan  # extra function, so I don't need to type it all
from smart_input import smart_input  # smarter input function

# after finished importing and functions
sleep(500)  # wait a sec
clear_console()
skip_loading = False
if not skip_loading:  # this is the loading screen of my game
    type_writer_color("Places From The Portal", [255, 255, 0], defaultDelay * 1.5)
    type_writer_color("...", [255, 255, 0], 500)
    sleep(500)
    clear_console()


def greet():
    greetings = ["Hey, ", "Welcome back, to the lab,    ",
                 "Howdy, "]  # didn't get time to make random greeting function
    items = []

    jstypec(greetings[1] + "Jim Johnson\n", [255, 255, 255], defaultDelay / 2)
    sleep(2000)
    jstypec("The portal is nearly done", white, defaultDelay)
    type_writer_color("...", white, 500)
    type_writer_color("  we just need to make one more component\n", white, defaultDelay)


def portal_room():
    """takes you to the same or different function based on input"""
    x = smart_input("Travel[1] Talk to John Smith[2]", ["travel", "1", "talk", "2"])
    if match_from_array(x, ["travel", "1"]):
        # if travelling
        type_writer_color("Where would you like to go?\n", [255, 255, 255], defaultDelay)
        x = smart_input("Enter the portal[1] Back to the portal room[2]", ["portal", "1", "back", "2"])
        if match_from_array(x, ["portal", "1"]):
            enter_portal("desert")
            return
        else:
            portal_room()
            return
    elif match_from_array(x, ["talk", "2"]):
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
    type_writer_color("A unknown creature wanders in-front of you, standing on its tall, furred legs\n", white,
                      defaultDelay * 3)
    sleep(6000)
    type_writer_color("The creature begins to approach you\n", [255, 100, 100], defaultDelay * 6)
    sleep(1000)
    type_writer_color("Press ", white, defaultDelay)
    type_writer_color("enter", [255, 255, 0], defaultDelay)
    type_writer_color(" to scan the creature\n", white, defaultDelay)
    input()  # press enter to continue
    type_writer_color("You pull out your ", [100, 100, 100], defaultDelay * 2)
    type_writer_color("Advanced Scanner Device ", [255, 0, 255], defaultDelay * 2)
    type_writer_color("and begin to scan the creature\n", [100, 100, 100], defaultDelay * 2)
    sleep(750)  # 750ms
    scan("Ooragnak")
    ans = smart_input('Do you wish to fight the "Ooragnak"? [yes] [no]', ["yes", "no", "y", "n"])
    if ans == "yes" or ans == "y":
        # fighting
        clear_console()
        type_writer_color("You attempt to punch the Ooragnak\n", [0, 200, 200], defaultDelay)
        sleep(2000)
        clear_console()
        type_writer_color("The Ooragnak jumps and kicks you in the head\n", [0, 200, 200], defaultDelay)
        sleep(2000)  # 2000 milliseconds
        death('You collapse to the ground and all feeling and thoughts fade away')
    elif ans == "no" or ans == "n":  # if player don't want to fight
        type_writer_color("You begin to run away from the Ooragnak, but it follows\n", [255, 255, 255], defaultDelay)
        sleep(1000)
        type_writer_color(  # split because 120 char limit on a line
            "The Ooragnak has lost you, but you find yourself in a completely different terrain\n",
            [255, 255, 255],
            defaultDelay
        )
        sleep(1000)
        type_writer_color("You look around and see a ", [255, 255, 255], defaultDelay)
        type_writer_color("Building", [255, 0, 255], defaultDelay)
        type_writer_color(" in the distance on your left\n", [255, 255, 255], defaultDelay)
        sleep(1000)
        ans_ = smart_input("What direction do you want to go? [left] [right]", ["left", "right", "l", "r"])
        if ans_ == "left" or ans_ == "l":
            type_writer_color("You walk towards the building\n", [255, 255, 255], defaultDelay)
            sleep(1000)
            clear_console()
            type_writer_color("You hear a rumbling noise\n", [255, 255, 255], defaultDelay)
            type_writer_color("The ground collapses beneath you\n", [255, 255, 255], defaultDelay)
            sleep(1000)
            type_writer_color("You fall into a cave\n", [255, 255, 255], defaultDelay)
            sleep(1000)
            type_writer_color("it is too dark to see anything\n", [255, 255, 255], defaultDelay)
            sleep(1000)
            type_writer_color("You hear a noise behind you\n", [255, 255, 255], defaultDelay)
            sleep(1000)
            type_writer_color("You turn around and see a pair of ", [255, 255, 255], defaultDelay)
            type_writer_color("glowing eyes\n", [255, 0, 0], defaultDelay)
            sleep(1000)
            ans = smart_input("Do you want to try and run through the darkness? [yes] [no]", ["yes", "no", "y", "n"])
            if ans == "yes" or ans == "y":
                type_writer_color("You run through the darkness\n", [255, 255, 255], defaultDelay)
                sleep(1000)
                type_writer_color("You trip and fall\n", [255, 255, 255], defaultDelay)
                sleep(1000)
                type_writer_color("You hear a loud noise\n", [255, 255, 255], defaultDelay)
                sleep(1000)
                type_writer_color("You feel a sharp pain in your back\n", [255, 255, 255], defaultDelay)
                sleep(1000)
                type_writer_color("You fall to the ground\n", [255, 255, 255], defaultDelay)
                sleep(1000)
                death("You feel your life fading away")
            elif ans == "no" or ans == "n":
                # its just a traveler
                type_writer_color("You stand still and wait for the eyes to get closer\n", [255, 255, 255],
                                  defaultDelay)
                sleep(1000)
                type_writer_color("You see a ", [255, 255, 255], defaultDelay)
                type_writer_color("traveller ", [255, 0, 255], defaultDelay)
                type_writer_color("approach you\n", [255, 255, 255], defaultDelay)
                sleep(1000)
                type_writer_color("The traveller ignites his lantern\n", [255, 255, 255], defaultDelay)
                sleep(1000)
                type_writer_color("The traveller offers to take you back to America\n", [255, 255, 255], defaultDelay)
                a = smart_input("Do you want to go back to accept his offer? [yes] [no]", ["yes", "no", "y", "n"])
                if a == "yes" or a == "y":
                    # he presses a button uses a mysterious watch, and you are instantly transported back to america
                    type_writer_color("You accept his offer\n", [255, 255, 255], defaultDelay)
                    sleep(1000)
                    type_writer_color("He presses a button on his watch\n", [255, 255, 255], defaultDelay)
                    sleep(1000)
                    # fades tgo black
                    type_writer_color("You wake up in a hospital bed\n", [255, 255, 255], defaultDelay)
                    sleep(1000)
                    type_writer_color("You see a doctor walk in\n", [255, 255, 255], defaultDelay)
                    sleep(1000)
                    type_writer_color("Doctor: ", [100, 255, 100], defaultDelay)
                    type_writer_color("You were in a coma for 2 years\n", [255, 255, 255], defaultDelay)
                    sleep(1000)
                    jstypec("How did i get here:", white, defaultDelay)
                    sleep(1000)
                    type_writer_color("Doctor: ", [100, 255, 100], defaultDelay)
                    type_writer_color("You were found in a cave in the middle of the desert\n", [255, 255, 255],
                                      defaultDelay)
                    sleep(1000)
                    type_writer_color("Doctor: ", [100, 255, 100], defaultDelay)
                    type_writer_color(
                        "There were cuts all along your body and it appears you were bit by a giant spider\n",
                        [255, 255, 255],
                        defaultDelay
                    )
                    sleep(1000)
                    type_writer_color("Doctor: ", [100, 255, 100], defaultDelay)
                    type_writer_color("You are lucky to be alive\n", [255, 255, 255], defaultDelay)
                    sleep(2000)
                    type_writer_color("You are discharged from the hospital\n", [255, 255, 255], defaultDelay)
                    sleep(1000)
                    credits()
                if a == "no" or a == "n":
                    type_writer_color("The travellers lantern suddenly goes out, and you hear a rush of wind\n", white,
                                      defaultDelay * 2)
                    sleep(2000)
                    type_writer_color("More glowing eyes appear around you\n", [255, 255, 0], defaultDelay * 4)
                    sleep(1000)
                    type_writer_color("All of the eyes charge at you\n", [255, 0, 0], defaultDelay * 2)
                    sleep(1000)
                    type_writer_color("They begin to draw your life away from you\n", white, defaultDelay * 2)
                    sleep(1000)
                    type_writer_color("in a way you couldn't begin to understand\n", [], defaultDelay)
                    sleep(1000)
                    death("Your life gets sucked away by entities that shouldn't exist")

        if ans_ == "right" or ans_ == "r":
            # other way
            type_writer_color("You walk the other way\n", [255, 255, 255], defaultDelay)
            sleep(1000)
            type_writer_color("You see a ", [255, 255, 255], defaultDelay)
            type_writer_color("abandoned aircraft\n", [255, 0, 0], defaultDelay)
            sleep(1000)
            type_writer_color("in the distance\n", [255, 255, 255], defaultDelay)
            sleep(1000)
            klk = smart_input("Do you want to go to the aircraft? [yes] [no]", ["yes", "no", "y", "n"])
            if klk == "yes" or klk == "y":
                type_writer_color("You walk to the aircraft\n", [255, 255, 255], defaultDelay)
                sleep(1000)
                # as you get closer you notice that its leaking gas
                type_writer_color("You notice that the aircraft is leaking gas\n", [255, 255, 255], defaultDelay)
                sleep(1000)
                type_writer_color("sparks fly from the engine\n", [255, 255, 255], defaultDelay)
                sleep(1000)
                type_writer_color("you become engulfed in flames\n", [255, 255, 255], defaultDelay)
                sleep(1000)
                death("All of your thoughts are consumed by the flames")
            elif klk == "no" or klk == "n":
                type_writer_color(
                    "You walk past the abandoned aircraft, noticing the gas leaking out of its fuel tank\n",
                    [255, 255, 255], defaultDelay)
                sleep(1000)
                type_writer_color("The aircraft suddenly bursts into flames\n", [255, 255, 255], defaultDelay)
                sleep(1000)
                ol = smart_input("Do you want to put your cool sunglasses on?", ["yes", "no", "y", "n"])
                if ol == "yes" or ol == "y":
                    type_writer_color("You put your cool looking sunglasses and walk away from the burning aircraft\n",
                                      [255, 255, 255], defaultDelay)
                    sleep(1000)
                if ol == "no" or ol == "n":
                    type_writer_color("You walk away from the burning aircraft but dont look as cool\n",
                                      [255, 255, 255], defaultDelay)
                    sleep(1000)
                type_writer_color("You finally see a oil sample in the ground\n", [255, 255, 255], defaultDelay)
                sleep(1000)
                type_writer_color("You get a sample of the oil\n", [255, 255, 255], defaultDelay)
                sleep(1000)
                type_writer_color(
                    "You enable the recall device and feel as though your position is being pulled away from you\n",
                    [255, 255, 255], defaultDelay)
                sleep(1000)
                type_writer_color("Its a terrible feeling\n", [255, 255, 255], defaultDelay)
                sleep(1000)
                type_writer_color(
                    "The device beeps and you are flung through the fourth dimension back to the portal room",
                    [255, 255, 255], defaultDelay)
                sleep(1000)
                type_writer_color("Back in the portal room, you talk to John Smith about your findings\n",
                                  [255, 255, 255], defaultDelay)
                jstypec("Well done, you have found the oil sample\n", white, defaultDelay)
                sleep(1000)
                jstypec("Boss, this sample looks really promising, was there anything else in that desert?\n", white,
                        defaultDelay)
                sleep(1000)
                smart_input("Do you want to tell John about the aircraft?", ["yes", "no", "y", "n"])
                sleep(1000)
                jstypec("That's odd, the scanner we sent through said that its no where near earth", white,
                        defaultDelay)
                sleep(1000)
                jstypec("I wonder if its a alien aircraft or something\n", white, defaultDelay)
                sleep(1000)
                jstypec("Anyway, we need to get this sample back to the lab\n", white, defaultDelay)
                sleep(1000)
                jstypec("You are dismissed\n", white, defaultDelay)
                sleep(10000)
                type_writer_color("|        [LAB RESULT REPORT]        |\n", [255, 25, 170], defaultDelay * 6)
                sleep(1000)
                type_writer_color("|-----------------------------------|\n", [255, 255, 255], defaultDelay * 6)
                sleep(1000)
                type_writer_color("|  Oil Sample: Alien Oil            |\n", [255, 255, 255], defaultDelay * 6)
                sleep(1000)
                type_writer_color("|  Results:                         |\n", [255, 255, 255], defaultDelay * 6)
                sleep(1000)
                type_writer_color("|  Oil contains alien life          |\n", [255, 255, 255], defaultDelay * 6)
                sleep(1000)
                type_writer_color("|  Oil is highly flammable          |\n", [255, 255, 255], defaultDelay * 6)
                sleep(1000)
                type_writer_color("|  Oil will work in a generator       |\n", [255, 255, 255], defaultDelay * 6)
                sleep(1000)
                game_credits()


def death(reason: str):
    """when you die"""
    type_writer_color(reason, [255, 0, 0], 100)  # 100ms
    sleep(3000)

    quit()


def game_credits():
    """print game credits"""
    clear_console()
    type_writer_color("Places from the portal\n", [255, 255, 255], defaultDelay * 4)
    # credits
    type_writer_color("Made by: ", [255, 255, 255], defaultDelay * 4)
    type_writer_color("Shaye Lorgelly, ", [255, 0, 0], defaultDelay * 4)
    quit()


def enter_portal(e):
    """when you try and enter the portal"""
    if "Quantum Fabrication Device" not in items:  # if player doesn't have the item
        # player doesn't have the thing, error report goes here
        type_writer_color("\n...\n", [40, 40, 40], defaultDelay * 16)
        type_writer_color("Portal Activation Sequence Failed\n", [255, 0, 0], defaultDelay * 2)
        type_writer_color("Generating diagnostic report, please wait", [200, 200, 200], defaultDelay * 2)
        sleep(2000)

        type_writer_color('\nComponent Missing: "Quantum Fabrication Device"\n', [25, 200, 255],
                          defaultDelay * 4)  # here we use '' to put the "" in without breaking the code
        portal_room()
        return
    clear_console()
    type_writer_color("as you awaken, you find yourself adrift in a vast, empty void...", [255, 0, 0], defaultDelay * 2)
    type_writer_color("...\n", [255, 0, 0], defaultDelay * 8)
    type_writer_color("you experience a sudden rush of air as the space around you begins to collapse\n", [255, 0, 0],
                      defaultDelay * 2)
    type_writer_color("it feels as though the very fabric of space itself is closing in...\n", [255, 0, 0],
                      defaultDelay * 2)
    type_writer_color("the darkness around you begins to swirl and churn...\n", [255, 0, 0], defaultDelay * 2)
    type_writer_color("you feel a sense of impending doom as the void threatens to consume you...\n", [255, 0, 0],
                      defaultDelay * 2)
    sleep(2000)
    clear_console()
    type_writer_color("*fades to black*", [1, 1, 1], defaultDelay * 2)  # hard to see
    sleep(2000)
    clear_console()
    type_writer_color("you awaken again, and find yourself in a new location...\n", [255, 0, 0], defaultDelay * 4)
    if e == "desert":
        desert()
    else:
        portal_room()  # incase I had extra time to make portal go back to the portal room


greet()  # start greeting thing
portal_room()  # start the game

# game_credits()  # debug prints
# desert()  # for desert testing
