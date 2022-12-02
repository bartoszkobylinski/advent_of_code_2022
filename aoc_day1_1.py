# Advent of Code task #1
import time
from collections import Counter

ELF_COUNTER = 1
FILE = "calories_input.txt"
ELVES_LIST = dict()

def extract_calories_list_from_file(calories_file):
    calories_list = []
    with open(calories_file, 'r') as calories_file:
        calories_inputs = calories_file.readlines()
        for line in calories_inputs:
            calories_list.append(line[:-1])
    return calories_list



def sort_calories_by_elves(calories_list, elf_counter):

    for calorie in calories_list:
        if ELVES_LIST.get(f'Elf {elf_counter}', "Don't exist") == "Don't exist":
            ELVES_LIST[f"Elf {elf_counter}"] = list()
            if len(calorie) > 0:
                temp = ELVES_LIST[f"Elf {elf_counter}"]
                temp.append(int(calorie))
            else:
                elf_counter +=1
        else:
            if len(calorie) > 0:
                temp = ELVES_LIST[f"Elf {elf_counter}"]
                temp.append(int(calorie))
            else:
                elf_counter +=1

def show_the_elf_with_the_highest_calories(elves_list):
    for elf, calories_list in elves_list.items():
        elves_list[elf] = sum(calories_list)
    return max(elves_list.values())


def main(file, elf_counter, elves_list):
    calories_list = extract_calories_list_from_file(file)
    sort_calories_by_elves(calories_list,elf_counter)
    elf_with_highest_calories = show_the_elf_with_the_highest_calories(elves_list)
    return elf_with_highest_calories

#print(f"that is elf with the highest amount of calories: {max(elves_list.values())}")

elf = main(file=FILE, elf_counter=ELF_COUNTER, elves_list=ELVES_LIST)
print(f"Highest calories is: {elf}")

def show_three_highest_elves(elves_list):
    three_highest = Counter(elves_list)
    most_common = three_highest.most_common(3)
    sum_three_highest = 0
    for item in most_common:
        sum_three_highest += item[1]
    return sum_three_highest

print(f"three highest elves {show_three_highest_elves(elves_list=ELVES_LIST)}")
