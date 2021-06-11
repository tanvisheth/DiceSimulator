import random
print(" This is Dice Simualtor Using Python ")
x="y"

while x=="y":
    num=random.randint(1,6)

    if num==1:
        print(" ----------- ")
        print(" |         | ")
        print(" |         | ")
        print(" |    O    | ")
        print(" |         | ")
        print(" |         | ")
        print(" ----------- ")

    if num==2:
        print(" ----------- ")
        print(" |         | ")
        print(" |         | ")
        print(" | O     O | ")
        print(" |         | ")
        print(" |         | ")
        print(" ----------- ")

    if num==3:
        print(" ----------- ")
        print(" |         | ")
        print(" |    O    | ")
        print(" |    O    | ")
        print(" |    O    | ")
        print(" |         | ")
        print(" ----------- ")

    if num==4:
        print(" ----------- ")
        print(" |         | ")
        print(" | O     O | ")
        print(" |         | ")
        print(" | O     O | ")
        print(" |         | ")
        print(" ----------- ")

    if num==5:
        print(" ----------- ")
        print(" |         | ")
        print(" | O     O | ")
        print(" |    O    | ")
        print(" | O     O | ")
        print(" |         | ")
        print(" ----------- ")


    if num==6:
        print(" ----------- ")
        print(" |         | ")
        print(" | O     O | ")
        print(" | O     O | ")
        print(" | O     O | ")
        print(" |         | ")
        print(" ----------- ")

    x=input(" Do you want to roll Dice again ! ")
