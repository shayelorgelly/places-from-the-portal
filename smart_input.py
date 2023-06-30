"""Made by Shaye Lorgelly"""


def smart_input(question: str, acceptable: list):  # input func that prevents crashing
    """use advanced input"""
    accepted = False
    while not accepted:
        x = input(question + ">")
        x = x.replace(" ", "").lower()  # remove all spaces and make lowercase
        for z in acceptable:
            if x == z:
                accepted = True  # ignore unused, because it is used...
                return x
        if not accepted:
            print("That's not a option, please try again.")
