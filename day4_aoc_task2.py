#Day 4 of Advent of Code
import time

FILE = 'sections.txt'

sections = []

with open (FILE, 'r') as input_file:
    sections = input_file.readlines()

counter = 0
sections1 = []

for section in sections:
    section = section.rstrip('\n')
    section = section.split(',')
    section1 =[]
    for element in section:
        element = element.split('-')
        #print(element)
        section1.append(element)

    sections1.append(section1)

for section in sections1:
    start1 = int(section[0][0])
    stop1 = int(section[0][1]) + 1
    start2 = int(section[1][0])
    stop2 = int(section[1][1]) + 1
    if start1 == stop1:
        first_range = [start1]
    else:
        first_range = list(range(start1, stop1))
    print(f"section: {section}")
    print(first_range)
    if start2 ==stop2:
        second_range = [start2]
    else:
        second_range = list(range(start2, stop2))
    print(second_range)
    #a = first_range.issubset(second_range)
    common_list = set(first_range).intersection(second_range)
    if common_list:
        counter +=1
    '''
    a = second_range.issubset(first_range)
    if a:
        counter +=1
    '''
    print('\n')
    #time.sleep(4)

print(f"counter: {counter}")
        
    
'''

        start1 = int(section[0][0])
        print(start1)
        stop1 = int(section[0][-1])
        print(stop1)
        start2 = int(section[1][0])
        stop2 = int(section[1][-1])
        first_range = range(start1,stop1)
        second_range = range(start2, stop2)
    else: 
        start1 = int(section[0][:2])
        stop1=int(section[0][-2:])
        start2 = int(section[1][:2])
        stop2 = int(section[1][-2:])
        first_range = range(start1,stop1)
        second_range = range(start2, stop2)
    
    
    print(first_range)
    print(second_range)
'''
