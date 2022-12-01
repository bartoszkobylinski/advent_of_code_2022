# Advent of Code task #1
import time
from typing import Counter

calories_list = []
elves_list = dict()
print(elves_list)

with open('calories_input.txt', 'r') as calories_file:
    calories_inputs = calories_file.readlines()
    #print(calories_inputs)
    for line in calories_inputs:
        #print(line[:-1])
        calories_list.append(line[:-1])

elf_counter = 1


for calorie in calories_list:

    if elves_list.get(f'Elf {elf_counter}', "Don't exist") is "Don't exist":
        elves_list[f"Elf {elf_counter}"] = list()
        if len(calorie) > 0:
            temp = elves_list[f"Elf {elf_counter}"]
            print(f"this is a temp: {temp}")
            temp.append(int(calorie))
        else:
            elf_counter +=1
    else:
        if len(calorie) > 0:
            temp = elves_list[f"Elf {elf_counter}"]
            print(f"this is a temp: {temp}")
            temp.append(int(calorie))
        else:
            elf_counter +=1


print(elves_list)

'''

    if len(calorie) > 0:
        elves_list[f'Elf {counter}']
        calorie = int(calorie)
        print(f"that is a calorie type{type(calorie)} and a value: {calorie}")
        elf_calories_list.append(calorie)
        print(f"this is a list after append{elf_calories_list}")
        print(f"that is sum: {sum(elf_calories_list)}")
    else:
        print(f"I have found empty string and sum is: {sum(elf_calories_list)}")
    #print(f"type: {type(calorie)} and the calorie: {calorie}")
'''    
