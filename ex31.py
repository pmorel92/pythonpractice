print("""You enter a dark room and there are two doors.
        Which do you choose?""")

door = input("CHOOSE WISELY >> ")

if door == "1":
    print("THere's a giant bear here eating a cheesecake.")
    print("What do you do?")
    print("1. Take the Cake")
    print("2. Scream at the bear")

    bear = input(">")

    if bear == "1":
        print("The bear eats your face off")

    elif bear == "2":
        print("The bear eats your legs off")

    else:
        print(f"Well done {bear} is probably better")
        print("bear runs away")
elif door == "2":
    print("You stare into the endless abyss of cthulus retina")
    print("1. Blue Berries")
    print(" 2. Yellow nose")
    print("Ooga booga")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("You die")
    else:
        print("you still die")
else:
    print("discretion is the better part of valor")
