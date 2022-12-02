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

def calculate_game_result(game_results, task):
    game_result = 0
    match task:
        case "1":
            for single_play in game_results:
                game_result += result_of_single_play(single_play)
        case "2":
            for single_play in game_results:
                game_result += result_of_single_play_second_task(single_play)
    
    return game_result

def main(file, task):
    a = calculate_game_result(extract_game_results(file=file), task=task)
    print(f"that is a final score for task {task} and you get: {a}")

def result_of_single_play_second_task(result):
    match result[0]:
        case 'A':
            match result[-1]:
                case 'X':
                    return 3
                case 'Y':
                    return 4
                case 'Z':
                    return 8
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
                    return 2
                case 'Y':
                    return 6
                case 'Z':
                    return 7


main(file=FILE, task='1')
main(file=FILE, task='2')