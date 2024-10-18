print("Welcome to the Tresure Island, Your mission is to find the treasure Island!")
direction = input("Which direction do you want to go? Left or Right? : ").lower()


if direction == "left":
    print("You live to see another day and you will reach next task!")
    direction2 = input("Which means you want to go? Swim or Wait? : ").lower()
    if direction2 == "wait":
        print("Thank god you reached the next level, there are 3 doors! ")
        direction3 = input("please choose one door, only the right door will save you!").lower()
        if direction3 == "red":
            print("you were eaten by lion, so Game over!")
        elif direction3 == "blue":
            print("you were thrown to fire, so game over!")
        else:
            print("You reach the final level and won treasure along with way to home!!!")
    else:
        print("you were eaten by uncle croc!")



else:
    print("GameOver!")