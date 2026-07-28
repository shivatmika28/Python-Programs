# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 12:08:55 2026

@author: ASUS
"""
# finding the maximuma and minimum
numbers = list(int(input("Enter numbers: ")))

maximum = numbers[0]
minimum = numbers[0]

for i in numbers:
    if i > maximum:
        maximum = i

    if i < minimum:
        minimum = i

print("Maximum =", maximum)
print("Minimum =", minimum)
    


#count how many numbers are graeter than 75
numbers = list(int(input("Enter numbers: ")))
count=0
for i in numbers:
    if i>75:
        count+=1
print("The total numbers greates than 75 are:",count)





#gaming murder mystry 
import random

# List of suspects
suspects = [
    {
        "name": "Alice",
        "clue": "I was reading a book in the library."
    },
    {
        "name": "Bob",
        "clue": "I was fixing my car in the garage."
    },
    {
        "name": "Charlie",
        "clue": "I was taking a walk in the garden."
    }
]

# Randomly choose the murderer
murderer = random.choice(suspects)["name"]


def show_suspects():
    print("\nSuspects:")
    for suspect in suspects:
        print("-", suspect["name"])


def interrogate():
    print("\nWho would you like to interrogate?")
    name = input("Enter suspect name: ").title()

    found = False

    for suspect in suspects:
        if suspect["name"] == name:
            print("\n", suspect["name"], "says:")
            print('"', suspect["clue"], '"')
            found = True
            break

    if not found:
        print("Suspect not found!")


def accuse():
    guess = input("\nWho is the murderer? ").title()

    if guess == murderer:
        print("\n🎉 Congratulations! You solved the case!")
    else:
        print("\n❌ Wrong accusation!")
        print("The real murderer was", murderer)
    return True


def main():
    print("🔍 WELCOME TO THE MURDER MYSTERY GAME 🔍")

    while True:
        print("\n1. View Suspects")
        print("2. Interrogate Suspect")
        print("3. Accuse Suspect")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_suspects()

        elif choice == "2":
            interrogate()

        elif choice == "3":
            game_over = accuse()
            if game_over:
                break

        elif choice == "4":
            print("Goodbye Detective!")
            break

        else:
            print("Invalid choice!")


main()
















































