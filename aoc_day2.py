# Advent of Code task #1

FILE = 'paper_scizors_game_results.txt'

def extract_game_results(file):
    with open(FILE) as game_file:
        game_results = game_file.readlines()
    return game_results

game_results = extract_game_results(file=FILE)
print(game_results)
