import random

playerPoints = 0
compPoints = 0
goalPoints = 21
diceRolled = 0


def Game():
    print()
    global playerPoints, compPoints
    EndGame = False
    currentPlayer = "Player"

    while not EndGame:

        if currentPlayer == "Player":
            diceRolled = int(
                input("Da li zelis da bacic 1 ili 2 kockice? (upisi broj 1 ili 2)\n"))

            playerPoints += DiceRoll(diceRolled)
            print("Vasi ukupni poeni su: " + str(playerPoints))
            print()

            if Win(playerPoints):
                print("Pobedili ste! 🥳")
                EndGame = True
            elif playerPoints > goalPoints:
                print("Izgubili ste 😭")
                EndGame = True
            else:
                currentPlayer = "Computer"

        else:
            Strategy(compPoints)
            print("Ukupni poeni kompjutera su: " + str(compPoints))
            print()
            print()

            if Win(compPoints):
                print("Kompjuter vas je pobedio 😭")
                EndGame = True
            elif compPoints > goalPoints:
                print("Kompjuter je izgubio, pobeda je vasa! 🥳")
                EndGame = True
            else:
                currentPlayer = "Player"


def DiceRoll(rolled):
    if rolled == 1:
        points = random.randint(1, 6)
        print("Izabrali ste 1 kockicu: " + str(points))
        return points

    elif rolled == 2:
        points1 = random.randint(1, 6)
        points2 = random.randint(1, 6)
        points = points1 + points2
        print("Izabrali ste 2 kockice: " + str(points1) +
              " + " + str(points2) + " = " + str(points))
        return points

    else:
        print("Izabrali ste nemoguc broj kockica (izaberite 1 ili 2)")
        return Game()


def Strategy(compP):
    global compPoints
    if compP > 12:
        pts = random.randint(1, 6)
        compPoints += pts
        print("Kompjuter je izabrao 1 kockicu: " + str(pts))
    else:
        pts1 = random.randint(1, 6)
        pts2 = random.randint(1, 6)
        pts = pts1 + pts2
        compPoints += pts
        print("Kompjuter je izabrao 2 kockice: " + str(pts1) +
              " + " + str(pts2) + " = " + str(pts))


def Win(playerPoints):
    if playerPoints == goalPoints:
        return True
    else:
        return False


Game()
