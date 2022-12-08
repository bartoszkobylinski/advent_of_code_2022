#Day 7 Advent of Code

FILE = 'directory.txt'

with open(FILE, 'r') as input_file:
    commands_package = input_file.readlines()

print(commands_package)

HDD = {'0':[]}
level = 0
current_dir = ''
'''
for command in commands_package:

    match command:
        case '$ ls':
            pass
        case '$ cd ..':
            level -=1
        case command[1:3] == 'dir':
            command = list(command)
            print(command)
            

HDD = {
    '0': [
        {'files'}: [
            {'chvtw.czb'}:{53302},{'dwhl.nrn'}:{240038}
        ]
    ]
}


hej, czy można jakoś zrobić sum() z zip() ? mam 2 listy, na jednej kwadraty liczb pierwszych a na drugiej kwadraty ciągu Fibonacciego, 
teraz muszę zsumować poszczególne elementy. Da się to zrobić z zip? (mam polecenie w zadaniu aby wykorzystać funkcje zip)
'''
a1 = [4,9,25,49]
a2 = [1,1,4,9]

a = list(zip(a1,a2))



