import re
#given a string, Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
#obtain 1. Game ID, sum of reds, blues and greens

#12 red cubes, 13 green cubes, and 14 blue cubes
def main():
    total_reds = 12
    total_greens = 13
    total_blues = 14

    #my_str = 'Game 4:  3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'

    with open("input.txt", "r") as file:
        sum_of_ids = 0
        line = file.readline()
        while line:
            #get game id
            game_id = re.search(r'\d+', line).group()

            num_of_reds = get_largest_red(line)
            num_of_blues = get_largest_blue(line)
            num_of_greens = get_largest_green(line)
            if num_of_reds <= total_reds and num_of_blues <= total_blues and num_of_greens <= total_greens:
                sum_of_ids += int(game_id)
            line = file.readline()
        print(sum_of_ids)



def get_largest_red(some_string):
    reds = re.findall(r'\d+ red', some_string)
    numbers_only = [int(''.join(char for char in item if char.isdigit())) for item in reds]
    return (max(numbers_only))

def get_largest_blue(some_string):
    blues = re.findall(r'\d+ blue', some_string)
    numbers_only = [int(''.join(char for char in item if char.isdigit())) for item in blues]
    return (max(numbers_only))

def get_largest_green(some_string):
    greens = re.findall(r'\d+ green', some_string)
    numbers_only = [int(''.join(char for char in item if char.isdigit())) for item in greens]
    return (max(numbers_only))

if __name__ == '__main__':
    main()
