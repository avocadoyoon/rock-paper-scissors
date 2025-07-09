import random
hands = {
    1: "✊ Rock",
    2: "✋ Paper",
    3: "✌️ Scissors"
}

print("Let's play Rock, Paper, Scissors!")
print("Choose a number:")
print("1 - ✊ Rock")
print("2 - ✋ Paper")
print("3 - ✌️ Scissors")

try:
    player = int(input("Your choice (1-3): "))
    if player not in [1, 2, 3]:
        raise ValueError("Invalid choice.")
except ValueError:
    print("Oops! Please enter a number between 1 and 3 next time.")
    exit()

computer = random.randint(1, 3)

print(f"\nYou chose: {hands[player]}")
print(f"Computer chose: {hands[computer]}\n")

if player == computer:
    print("It's a draw! 😐")
elif (player == 1 and computer == 3) or \
     (player == 2 and computer == 1) or \
     (player == 3 and computer == 2):
    print("You win! 🎉")
else:
    print("Computer wins! 🤖")

