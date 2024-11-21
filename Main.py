import json
import sys
import time

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
            return num_type(0)
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
def fail_safe_for_dev():
    print("BULLSHIT")
    time.sleep(5)


# |Default script|------------------------------------------------------------------------------------------------------
def leave():
    input("Press enter to quit: ")
    sys.exit()


if __name__ == "__main__":
    Harpy(
        [fail_safe_for_dev,
         leave]
    ).act()


