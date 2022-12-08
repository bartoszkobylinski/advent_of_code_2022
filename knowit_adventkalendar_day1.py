#Knowit Julekalendar 2022 dag1

letter = '' 
dictionary = []

with open('letter.txt', 'r') as file_letter:
    letter += file_letter.readline()

print(letter)

with open('dictionary.txt','r') as file_dictionary:
    dictionary = file_dictionary.readlines()

temp_dictionary = []

for word in dictionary:
    temp_dictionary.append(word.replace('\n',' '))

del dictionary

new_dictionary = dict()

for translation in temp_dictionary:
    translation = translation.split(',')
    new_dictionary[translation[0]] = translation[1]

del temp_dictionary

temporary_word = ''
translated_letter = ''
temporary_letter = ''


for character in letter:
    temporary_word +=character
    if temporary_word in new_dictionary.keys():
        print("znalazlem")
        print(temporary_word)
        print(new_dictionary[temporary_word])
        translated_letter +=new_dictionary[temporary_word]
        print(letter)
        letter=letter[len(temporary_word):]
        print(letter)
        temporary_word = ''
        continue

