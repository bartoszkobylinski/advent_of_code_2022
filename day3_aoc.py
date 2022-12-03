#Day 3 Advent of Code

FILE = 'rucksaks.txt'

def extract_input_file(file):
    with open(file, "r") as input_file:
        rucksacks_list = input_file.readlines()
    return rucksacks_list

print(extract_input_file(FILE))

