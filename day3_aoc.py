#Day 3 Advent of Code
import time
from string import ascii_letters

ALPHABET = ascii_letters

FILE = 'rucksaks.txt'

def extract_input_file(file):
    with open(file, "r") as input_file:
        rucksacks_list = input_file.readlines()
    return rucksacks_list

def calculate_total_result(rucksacks_list, alphabet):

    result = 0
    for list in rucksacks_list:
        print(f"that is list: {list}")
        print(f"that is next list: {next(iter(list))}")
        list = list.strip()
        middle_index = int(len(list)/2)
        list_1 = list[:middle_index]
        list_2 = list[middle_index:]
        common_element = set(list_1).intersection(list_2)
        common_element = next(iter(common_element))
        point = alphabet.index(common_element) + 1
        result += point
        time.sleep(2)
    return result


rucksacks_list = extract_input_file(file=FILE)
rucksacks_list = iter(rucksacks_list)
result_1 = 0
while True:
    temp_list = []
    try:
        for _ in range(3):
            rucksack = next(rucksacks_list).strip()
            temp_list.append(rucksack)
    except StopIteration:
        break
    common_element = set(temp_list[0]).intersection(temp_list[1],temp_list[2])
    point = ALPHABET.index(common_element.pop()) +1
    result_1 +=point
    
print(result_1)