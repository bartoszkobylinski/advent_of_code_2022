# Advent of Code task #1

FILE = 'paper_scizors_game_results.txt'

def extract_game_results(file):
    game_results = list()
    with open(FILE) as game_file:
        game_source_results = game_file.readlines()
        for line in game_source_results:
            line = line[:-1]
            game_results.append(line)

    return game_results

def result_of_single_play(result):
    match result[0]:
        case 'A':
            match result[-1]:
                case 'X':
                    return 4
                case 'Y':
                    return 8
                case 'Z':
                    return 3
        case 'B':
            match result[-1]:
                case 'X':
                    return 1
                case 'Y':
                    return 5
                case 'Z':
                    return 9
        case 'C':
            match result[-1]:
                case 'X':
                    return 7
                case 'Y':
                    return 2
                case 'Z':
                    return 6

def calculate_game_result(game_results):
    game_result = 0
    for single_play in game_results:
        game_result += result_of_single_play(single_play)
    
    return game_result

def main(file):
    a = calculate_game_result(extract_game_results(file=FILE))
    print(f"that is a final score you get: {a}")

main(file=FILE)