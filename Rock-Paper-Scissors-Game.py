from random import randint
print("Welcome to Rock Paper Scissors Game")
print("*"*35)
players_name = input("Please Enter Your Name")
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
num = randint(1,3)
if num==1:
    Comp_move="Rock"
elif num==2:
    Comp_move="Paper"
elif num==3:
    Comp_move="Scissors"

Player_move = input(f"{players_name} please enter your move (Rock, Paper, or Secissors):\n")
print(f"{players_name}'s Move")
if Player_move== "Rock":
    print(Rock)
    print("Rock")
elif Player_move == "Paper":
    print(Paper)
    print("Paper")
elif Player_move == "Scissors":
    print(Scissors)
    print("Scissors")

print("This Is Computer's Move")
if Comp_move== "Rock":
    print(Rock)
    print("Rock")
elif Comp_move == "Paper":
    print(Paper)
    print("Paper")
elif Comp_move == "Scissors":
    print(Scissors)
    print("Scissors")

if Comp_move==Player_move:
    print("It's a TIE")
elif Player_move == "Scissors" and Comp_move == "Paper":
    print(f"Wow!!! {players_name} Won :)")
elif Player_move == "Rock" and Comp_move == "Scissors":
    print(f"Wow!!! {players_name} Won :)")
elif Player_move == "Paper" and Comp_move == "Rock":
    print(f"Wow!!! {players_name} Won :)")
else:
    print("Computer Won and You Lose :(\n Try Next Time")