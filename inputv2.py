def inputv2(question, acceptable):
    accepted = False
    while not accepted:
        x = input(question)
        for z in acceptable:
            if x == z:
                accepted = True
                return x
        if not accepted:
            print("bad input, please try again")