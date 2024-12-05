import json
import sys
import time
import datetime
import random


class Harpy:
    def __init__(self, func_list):
        # Give an option to load script lists from a JSON file
        self.func_list = func_list
        # Make it go through the list to check for strings or invalid functions

    def act(self):
        while True:
            print("Harpy Script ")
            for count, x in enumerate(self.func_list):
                print(f'[{count}] {x.__name__}')

            func_to_use = get_user_number()
            if -1 < func_to_use < len(self.func_list):
                self.func_list[func_to_use]()
            else:
                print("Error: out of index")


# General use functions
def get_user_number(text="Enter number: ", num_type=int):
    while True:
        try:
            num = num_type(input(text))
            return num
        except ValueError:
            print("Error: Wrong type")
        except EOFError:
            # print(f"Error: No input given, {datetime.datetime.now()}")
            print(f"Error: No fucks given, {datetime.datetime.now()}")
            time.sleep(5)
    #


def dict_to_json(filename, dictionary):
    # This function make stuff go in a json file
    with open(filename, "w", encoding='utf-8') as outfile:
        # json.dump(dictionary, outfile)
        json.dump(dictionary, outfile, indent=1)


def get_from_json(filename, requested_info):
    # This function gets you stuff from a json file
    with open(filename, encoding='utf-8') as json_file:
        data = json.load(json_file)
        if requested_info == "Everything":
            return data
        return data[requested_info]


# |Scripts|-------------------------------------------------------------------------------------------------------------
def time_waster():
    ascii_player = {"Roche": """
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """,
                    "Papier": """
            ________
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """,
                    "Ciseau": """
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """}

    ascii_ai = {"Roche": """
                             _______
                            (____   '---
                           (_____)
                           (_____)
                            (____)
                             (___)__.---
        """,
                "Papier": """
                                ________
                            ___(____    '---
                           (______
                           (_______
                            (_______
                             (__________.---
        """
        , "Ciseau": """
                                 _______
                            ____(____   '---
                           (______
                           (__________
                                (____)
                                 (___)__.---
        """}
    # Score
    total_match = 0
    player_wins = 0
    ai_wins = 0
    ties = 0

    # Keep track of the player inputs
    player_last_choice = ""
    player_past_choices = []
    did_player_won = False
    ai_last_choice = ["Roche", "Papier", "Ciseau"][random.randint(0, 2)]

    # Main game loop
    while True:
        # Get player input
        while True:
            player_choice = input("Roche, Papier, Ciseau: ")

            # Allow some flexibility with the inputs
            if player_choice in ["roche", "r", "R"]:
                player_choice = "Roche"
            if player_choice in ["papier", "p", "P"]:
                player_choice = "Papier"
            if player_choice in ["ciseau", "c", "C"]:
                player_choice = "Ciseau"

            # Check if player input is valid
            if player_choice in ["Roche", "Papier", "Ciseau"]:
                break
            else:
                print("IT WAS A MISS INPUT")
        print(ascii_player[player_choice])

        # AI
        ai_choice = ["Roche", "Papier", "Ciseau"][random.randint(0, 2)]

        # Take what will beat the option that is most likely to be used by the player
        if player_past_choices:
            ai_choice = player_past_choices[random.randint(0, len(player_past_choices) - 1)]
            if ai_choice == "Roche":
                ai_choice = "Papier"
            elif ai_choice == "Papier":
                ai_choice = "Ciseau"
            elif ai_choice == "Ciseau":
                ai_choice = "Roche"

        # Counters the player if they won
        if did_player_won:
            if player_last_choice == "Roche":
                ai_choice = "Papier"
            if player_last_choice == "Papier":
                ai_choice = "Ciseau"
            if player_last_choice == "Ciseau":
                ai_choice = "Roche"

        # Change option to prevent the player to counter
        elif not did_player_won:
            if ai_last_choice == "Roche":
                ai_choice = "Papier"
            elif ai_last_choice == "Papier":
                ai_choice = "Ciseau"
            elif ai_last_choice == "Ciseau":
                ai_choice = "Roche"

        # straight up ceahting
        # if player_choice == "Roche":
        #     ai_choice = "Papier"
        # if player_choice == "Papier":
        #     ai_choice = "Ciseau"
        # if player_choice == "Ciseau":
        #     ai_choice = "Roche"

        print(f"L'IA choisi {ai_choice}")

        print(ascii_ai[ai_choice])

        # Game logic
        # Check for a tie
        if player_choice == ai_choice:
            print("Match nul")
            ties += 1
            did_player_won = False
        else:
            # Check if the player won
            if player_choice == "Roche" and ai_choice == "Ciseau" or \
                    player_choice == "Papier" and ai_choice == "Roche" or \
                    player_choice == "Ciseau" and ai_choice == "Papier":
                print("Le Joueur gagne")
                player_wins += 1
                did_player_won = True
            # If not, the AI won
            else:
                print("L'IA gagne")
                ai_wins += 1
                did_player_won = False

        # Keep track of the player inputs
        player_last_choice = player_choice
        player_past_choices.append(player_choice)

        # Keep track of match
        total_match += 1

        # After 10 match annonce who won the most
        if total_match == 10:
            print(f"{player_wins = }")
            print(f"{ai_wins = }")
            print(f"{ties = }")
            if ai_wins == player_wins:
                print("Nul")
            elif ai_wins > player_wins:
                print("L'IA a gagner")
            else:
                print("Tu as gagner")


# |Default script|------------------------------------------------------------------------------------------------------
def leave():
    input("Press enter to quit: ")
    sys.exit()


if __name__ == "__main__":
    Harpy(
        [
            time_waster,
            leave
        ]
    ).act()


