import random
import time
wins = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

def computer_choice():
    return random.choice(list(wins))

def art(option):
    match option:
        case "rock":
            print("""
    _______
---'   ____)
      (_____ )
      (_____ )
      (____)
---.__(___)
""")
        case "paper":
            print("""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""")
        case "scissors":
            print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

def main():
    isplaying = True
    winnings = 0
    losses = 0
    ties = 0
    score = 0
    print("----------------Rock Paper Scissors---------------")
    print("Win a round to increase the score. Lose a round and your score decreases")
    while isplaying:
        user = input("Enter your choice: ").lower().strip()
        if user not in wins:
            print("Only enter out of these options(rock,paper,scissors): ")
            continue
        print(f"Computer choosing... ")
        time.sleep(1)
        comp = computer_choice()
        print(f"Your choice: {user}")
        art(user)
        print(f"Computer choice: {comp}")
        art(comp)
        if user == comp:
            print("It's a tie!")
            ties += 1
        elif wins[user] == comp:
            print("You won!")
            score += 1
            winnings += 1
        else:
            print("You lost!")
            score -= 1
            losses += 1
        print(f"---------------- Your score is: {score} --------------------")
        while True:
            play = input("Would you like to play another round(Y/N): ").upper().strip()
            if play in ("Y", "N"):
                break
            print("Enter either 'Y'/'N': ")
        if play == "N":
            print(f"-------------------------- Final Results -------------------------\nScore: {score}")
            print(f"Wins: {winnings}\nLosses: {losses}\nTies: {ties}")
            print("-----------------------Thank you for playing-----------------------")
            isplaying = False

if __name__ == "__main__":
    main()
