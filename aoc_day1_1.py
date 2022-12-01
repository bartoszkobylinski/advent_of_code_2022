# Advent of Code task #1
import time
from collections import Counter

calories_list = []
elves_list = dict()

with open('calories_input.txt', 'r') as calories_file:
    calories_inputs = calories_file.readlines()
    for line in calories_inputs:
        calories_list.append(line[:-1])

elf_counter = 1


for calorie in calories_list:
    if elves_list.get(f'Elf {elf_counter}', "Don't exist") == "Don't exist":
        elves_list[f"Elf {elf_counter}"] = list()
        if len(calorie) > 0:
            temp = elves_list[f"Elf {elf_counter}"]
            temp.append(int(calorie))
        else:
            elf_counter +=1
    else:
        if len(calorie) > 0:
            temp = elves_list[f"Elf {elf_counter}"]
            temp.append(int(calorie))
        else:
            elf_counter +=1

for elf, calories_list in elves_list.items():
    elves_list[elf] = sum(calories_list)

print(f"that is elf with the highest amount of calories: {max(elves_list.values())}")

three_highest = Counter(elves_list)
most_common = three_highest.most_common(3)
sum_three_highest = 0
for item in most_common:
    sum_three_highest += item[1]
print(f"thos is sum of three the highest amount of calories carries by elves: {sum_three_highest}")
