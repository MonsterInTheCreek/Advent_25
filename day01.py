## AoC 2025 - Day 1
# It's late...  Favoring writing code quickly over well written.
# Premature refactoring, and the devil, and all that.

def get_data(file):
    with open(file,"r") as source:
        return source.readlines()


def spin(start, instruction):
    instruction = instruction.strip()
    if instruction[0] == "L":
        return start - int(instruction[1:])
    elif instruction[0] == "R":
        return start + int(instruction[1:])
    else:
        print("somehow got non left or right instruction")


def get_mod(position):
    return position % 100


# crappy monolithic wall of code inside gate, not good for prod

if __name__ == "__main__":
    ## Example
    ex_input = ["L68","L30","R48","L5","R60","L55","L1","L99","R14","L82"]
    init_position = 50
    zeros = 0
    current = init_position
    for inst in ex_input:
        current = spin(current, inst)
        if get_mod(current) == 0:
            zeros += 1
    print(f"Example = {get_mod(current)}")
    print(f"Zeros = {zeros}")

    ## Part A
    loops = 0
    zeros = 0
    input_file = "input01.txt"
    a_input = get_data(input_file)
    current = init_position
    for inst in a_input:
        current = spin(current, inst)
        if get_mod(current) == 0:
            zeros += 1
        loops += 1
    print(f"This many loops = {loops}")
    print(f"Final position = {get_mod(current)}")
    print(f"Zeros = {zeros}")
