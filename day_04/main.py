from random import randint


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hands = [rock, paper, scissors]
user_hand = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_hand < 0 or user_hand > len(hands) - 1:
    print("Invalid hand, game over.")
else:
    print(hands[user_hand])

    print("Computer chose:")
    computer_hand = randint(0, len(hands) - 1)
    print(hands[computer_hand])

    if user_hand == 0:
        if computer_hand == 0:
            print("It's a draw.")
        elif computer_hand == 1:
            print("You lose.")
        else:
            print("You win.")
    elif user_hand == 1:
        if computer_hand == 0:
            print("You win.")
        elif computer_hand == 1:
            print("It's a draw.")
        else:
            print("You lose.")
    else: 
        if computer_hand == 0:
            print("You lose.")
        elif computer_hand == 1:
            print("You win.")
        else:
            print("It's a draw.")
