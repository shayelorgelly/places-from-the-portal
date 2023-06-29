"""advanced input module"""


def inputv2(question: str, acceptable: list):
    """use advanced input"""
    accepted = False
    while not accepted:
        x = input(question)
        x = x.replace(" ", "").lower()  # remove all spaces and make lowercase
        for z in acceptable:
            if x == z:
                accepted = True
                return x
        if not accepted:
            print("bad input, please try again")
