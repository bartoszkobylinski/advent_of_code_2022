#Day 6 Advent of Code
import time

FILE = 'descript.txt'

with open(FILE, 'r') as input_file:
    code = input_file.readlines()[0]


start = 0
end_1 = 14
marker_number = 0
for step in range(len(code)):
    temp_code = code[start:end_1]
    print(step, temp_code)
    if(len(set(temp_code)) == len(temp_code)):
        print('f')
        print(temp_code)
        marker_number = step
        break
    start +=1
    end_1 +=1

print(f"Marker starts at {marker_number + 14}")
