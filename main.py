import random
from time import sleep

botC = random.randint(1,3)
lives = 3

print("Hi Welcome To The Rock Paper Scissors!")

while lives > 0:
    choise = input("Please Write Your Choise: ")
    match choise:
        case "rock":
            match botC:
                case 1:
                    print("Equal")
                case 2:
                    lives -= 1
                    print("Bot Got Point") 
                case 3:
                    lives += 1
                    print("You Got Point")
        case "paper":
            match botC:
                case 1:
                    lives += 1
                    print("You Got Point")
                case 2:
                    print("Equal")
                case 3:
                    lives -= 1
                    print("Bot Got Point")
        case "scissors":
            match botC:
                case 1:
                    lives -= 1
                    print("Bot Got Point")
                case 2:
                    lives += 1
                    print("You Got Point")
                case 3:
                    print("Equal")
