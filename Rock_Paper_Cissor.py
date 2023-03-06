import random

def game(player_1, player_2):
    if (player_1 == "rock" and player_2 == "rock"):
        print("Draw")
    elif (player_1 == "paper" and player_2 == "paper"):
        print("Draw")
    elif (player_1 == "scissor" and player_2 == "scissor"):
        print("Draw")
    elif player_1 == "rock" and player_2 == "paper":
        print("You Lose")
    elif player_1 == "rock" and player_2 == "scissor":
        print("You Win")
    elif player_1 == "paper" and player_2 == "rock":
        print("You Win")
    elif player_1 == "paper" and player_2 == "scissor":
        print("You Lose")
    elif player_1 == "scissor" and player_2 == "rock":
        print("You Lose")
    elif player_1 == "scissor" and player_2 == "paper":
        print("You Win")

if __name__ == "__main__":
    print("Choose one of three: rock, paper or scissor")
    
    while True:
        # computer
        computer = {
            1: "rock",
            2: "paper",
            3: "scissor"
        }
        num = random.randint(1,3)
        com_player = computer[num]

        you = str(input())
        game(you, com_player)
