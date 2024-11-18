# General use functions
def get_user_number(text="Enter number: ", num_type=int):
    while True:
        try:
            num = num_type(input(text))
            return num
        except ValueError:
            print("Error: Wrong type")
    #



def leave():
    input("Exiting.")
    quit()


if __name__ == "__main__":
    func_list = [leave]
    while True:
        print("Script list")
        for count, x in enumerate(func_list):
            print(f'[{count}] {x.__name__}')

        func_to_use = get_user_number()
        if -1 < func_to_use < len(func_list):
            func_list[func_to_use]()
        else:
            print("Error: out of index")

