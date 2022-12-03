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
        list = list.strip()
        middle_index = int(len(list)/2)
        list_1 = list[:middle_index]
        list_2 = list[middle_index:]
        common_element = set(list_1).intersection(list_2)
        common_element = next(iter(common_element))
        point = alphabet.index(common_element) + 1
        result += point
    return result

print(f"that is result: {calculate_total_result(extract_input_file(file=FILE), alphabet=ALPHABET)}")
