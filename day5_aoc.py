#Day 5 of Advent of Code
import time

FILE = 'stocks.txt'

with open(FILE, 'r') as input_file:
    temporary_stokcs = input_file.readlines()
    temporary_movement = temporary_stokcs[10:]
    movements = []
    for instruction in temporary_movement:
        one_instruction = []
        instruction = instruction.split(" ")
        one_instruction.append(int(instruction[1]))
        one_instruction.append(int(instruction[3]))
        one_instruction.append(int(instruction[5].rstrip('\n')))
        movements.append(one_instruction)

stocks = {
    '1': ['Z','P','M','H','R'],
    '2': ['P','C','J','B'],
    '3': ['S','N','H','G','L','C','D'],
    '4': ['F','T','M','D','Q','S','R','L'],
    '5': ['F','S','P','Q','B','T','Z','M'],
    '6': ['T','F','S','Z','B','G'],
    '7': ['N','R','V'],
    '8': ['P','G','L','T','D','V','C','M'],
    '9': ['W','Q','N','J','F','M','L']
}

'''
for instruction in movements:
    #print(instruction)
    for _ in range(instruction[0]):
        element = stocks.get(f"{instruction[1]}").pop()
        stocks.get(f"{instruction[2]}").append(element)
'''

letters = ''
for box in stocks:
    letters += stocks[box][-1]

print(letters)
    
for instruction in movements:
    cut = int(instruction[0])
    cutted_list = stocks.get(f"{instruction[1]}")[-cut:]
    rest_list = [element for element in stocks.get(f"{instruction[1]}") if element not in cutted_list]
    stocks[f"{instruction[1]}"] = rest_list
    stocks[f"{instruction[2]}"] += cutted_list
    pass


letters = ''
for box in stocks:
    if stocks.get(f"{box}") is not None:
        print(stocks.get(f"{box}"))
        time.sleep(5)