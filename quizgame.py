from tkinter.messagebox import QUESTION
from questions import quiz

print("Welcome to the Blackburn Rovers advent calendar quiz!")

playing = input("Are you ready to start the game? Y/N").lower()

if playing != "y":
    print("Okay, maybe another time then?")
    quit()

print("Okay! Let's play!")
print("You will be given the shirt number from 1-31,\nand the year or years that they wore that number.\nSimply enter the surname of the player that matches with the number")

def check_answer(question, ans, tries):
    if quiz[question]['answer'].lower() == ans.lower():
        print("Correct! Well done. ")
        return True
    else:
        print("Incorrect, try again... ")
        return False

def main():
    score = 0
    for question in quiz:
        tries = 5
        while tries > 0:
            print(quiz[question]['question'])
            answer = input("Enter Answer: ")
            check = check_answer(question, answer, tries)
            if check == True:
                score += 1
                break
            else:
                tries -= 1
            pass
        else:
            print(f"You used all your attempts. The correct answer was ", quiz[question]['answer'])
    percentage = score / 31 * 100
    return print(f"You scored ", score, "out of 31. ", int(percentage), "% - not too bad.")



main()