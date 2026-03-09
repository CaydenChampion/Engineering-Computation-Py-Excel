"""
    Title: Adventure Game
    Author: Cayden Champio
    Date: 3/6/26
    Class: Engineering computation
"""

print("You are exploring an old forest and come across a mysterious cave.")
choice1 = input("Do you ENTER the cave or WALK away? ").lower()

if choice1 == "enter":
    print("\nYou step inside the cave and hear a strange noise deeper inside.")
    choice2 = input("Do you FOLLOW the noise or LEAVE the cave? ").lower()

    if choice2 == "follow":
        print("\nYou walk deeper into the cave and find a sleeping dragon!")
        choice3 = input("Do you SNEAK past the dragon or RUN away? ").lower()

        if choice3 == "sneak":
            print("\nYou successfully sneak past the dragon and find a treasure chest. You win!")
        elif choice3 == "run":
            print("\nThe dragon wakes up and chases you out of the cave. You escape safely!")
        else:
            print("Invalid option. Please choose one of the available choices.")

    elif choice2 == "leave":
        print("\nAs you leave the cave, you find a hidden path outside.")
        choice3 = input("Do you FOLLOW the path or RETURN to the forest? ").lower()

        if choice3 == "follow":
            print("\nThe path leads to a beautiful waterfall. You discovered a secret place!")
        elif choice3 == "return":
            print("\nYou return safely to the forest and continue your journey.")
        else:
            print("Invalid option. Please choose one of the available choices.")

    else:
        print("Invalid option. Please choose one of the available choices.")

elif choice1 == "walk":
    print("\nYou walk away from the cave and find a small village.")
    choice2 = input("Do you VISIT the village or KEEP walking? ").lower()

    if choice2 == "visit":
        print("\nThe villagers welcome you warmly.")
        choice3 = input("Do you STAY for dinner or LEAVE the village? ").lower()

        if choice3 == "stay":
            print("\nYou enjoy a great meal and make new friends.")
        elif choice3 == "leave":
            print("\nYou politely leave and continue your adventure.")
        else:
            print("Invalid option. Please choose one of the available choices.")

    elif choice2 == "keep":
        print("\nYou continue walking and reach a river.")
        choice3 = input("Do you SWIM across or BUILD a raft? ").lower()

        if choice3 == "swim":
            print("\nYou swim across safely and find a new land to explore.")
        elif choice3 == "build":
            print("\nYour raft works perfectly and you sail downstream.")
        else:
            print("Invalid option. Please choose one of the available choices.")

    else:
        print("Invalid option. Please choose one of the available choices.")

else:
    print("Invalid option. Please choose one of the available choices.")