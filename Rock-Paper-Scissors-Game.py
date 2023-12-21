from random import randint

print("Welcome to Rock Paper Scissors Game")
print("*" * 35)

players_name = input("Please Enter Your Name: ")

player_score = 0
computer_score = 0
rounds_to_win = 3 

while player_score < rounds_to_win and computer_score < rounds_to_win:
    Rock = """
        _______
    ----' _____)
          (_____)
          (_____)
          (____)
    ----'__(__)
    """
    Paper = """
        _________
    ----' _______)____
          (___________)
          (_____________)
          (___________)
    ----' (_________)
    """
    Scissors = """
        _______
    ----' _____)_____
          (__________)
          (____________)
          (____)
    ----' (____)
    """

    num = randint(1, 3)
    if num == 1:
        Comp_move = "Rock"
    elif num == 2:
        Comp_move = "Paper"
    elif num == 3:
        Comp_move = "Scissors"

    Player_move = input(f"{players_name}, please enter your move (Rock, Paper, or Scissors):\n")
    print(f"{players_name}'s Move")
    if Player_move == "Rock":
        print(Rock)
        print("Rock")
    elif Player_move == "Paper":
        print(Paper)
        print("Paper")
    elif Player_move == "Scissors":
        print(Scissors)
        print("Scissors")

    print("This Is Computer's Move")
    if Comp_move == "Rock":
        print(Rock)
        print("Rock")
    elif Comp_move == "Paper":
        print(Paper)
        print("Paper")
    elif Comp_move == "Scissors":
        print(Scissors)
        print("Scissors")

    if Comp_move == Player_move:
        print("It's a TIE")
    elif Player_move == "Scissors" and Comp_move == "Paper":
        print(f"Wow!!! {players_name} Won :)")
        player_score += 1
    elif Player_move == "Rock" and Comp_move == "Scissors":
        print(f"Wow!!! {players_name} Won :)")
        player_score += 1
    elif Player_move == "Paper" and Comp_move == "Rock":
        print(f"Wow!!! {players_name} Won :)")
        player_score += 1
    else:
        print("Computer Won and You Lose :(")
        computer_score += 1

    print(f"\nCurrent Score - {players_name}: {player_score}, Computer: {computer_score}\n")

if player_score > computer_score:
    print(f"Congratulations! {players_name} Wins the Game!")
elif computer_score > player_score:
    print("Computer Wins the Game. Better luck next time.")
else:
    print("It's a Tie. Good game!")
