# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
# A for Rock, B for Paper, and C for Scissors.
# X for Rock, Y for Paper, and Z for Scissors.
# Your total score is the sum of your scores for each round.
# The score for a single round is the score for the shape you selected
# (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the
# outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)

# Part A
def file2list(filepath='input.txt'):
    """
        Reads a text file and converts its contents into a list of strings.

        Args:
            filepath (str): The path to the input text file. Default is 'input.txt'.

        Returns:
            list: A list of strings, each representing a line from the file with leading and trailing whitespaces removed.
    """
    lines = []
    with open(filepath, 'r') as ifile:
        for item in ifile:
            lines.append(item.strip())
    return lines


def get_rps_score(strategy: str) -> int:
    # get the score only from the rock paper scissor
    # win: 6
    # draw: 3
    # loss: 0

    score_table = {
        'A X': 3,
        'A Y': 6,
        'A Z': 0,
        'B X': 0,
        'B Y': 3,
        'B Z': 6,
        'C X': 6,
        'C Y': 0,
        'C Z': 3
    }

    return score_table.get(strategy)


def get_choice_score(strategy: str) -> int:
    # get the score only because of your choice
    # (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the

    strategy = strategy.split(' ')[-1]

    match strategy:
        case 'X':
            return 1
        case 'Y':
            return 2
        case 'Z':
            return 3


def calculate_total_score(strategies: list) -> int:
    total_score = 0
    for strategy in strategies:
        total_score += get_rps_score(strategy) + get_choice_score(strategy)
    print(f"The total score is: {total_score}")
    return total_score


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # part A
    input_file = 'input.txt'
    score_pairs = file2list(input_file)
    calculate_total_score(score_pairs)