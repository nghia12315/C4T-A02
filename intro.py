# Ma trận 5*  

#     for i in range(5):
#         for j in range(5):
#             print(" * ", end=" ")
        # print()



# Ma trận tùy side có player
playerX = 6
playerY = 5

def printMap(side):
    for i in range(side):
        for j in range(side):
            if i == playerY and j== playerX:
                print("p", end=" ")
            else:
                print("*", end=" ")
        print()


def run():
    global playerX, playerY
    direct = input("Your move: ")
    if direct == "w": 
        if playerY > 0:
            playerY -=1
        else:
            print("False, please move again! ")
    elif direct == "s":
        if playerY < 6:
            playerY +=1
        else:
            print("False, please move again! ")
    elif direct == "a":
        if playerX  > 0:
            playerX -=1
        else:
            print("False, please move again! ")
    elif direct == "d":
        if playerX < 6:
            playerX +=1
        else:
            print("False, please move again! ")
printMap(7)
while True:
    print(chr(27) + "[23]")
    printMap(7)
    run()