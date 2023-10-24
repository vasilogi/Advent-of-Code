# Find the description of the problem here:
# https://adventofcode.com/2022/day/2

# Part A
def file2list(filepath: object = 'input.txt') -> object:
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
    """Calculates the score of a rock-paper-scissors strategy.

        Args:
            strategy: A string representing the rock-paper-scissors strategy, in the format
                "opponent's choice player's choice". For example, "A X" represents the strategy where the
                opponent chooses "rock" and the player also chooses "rock".

        Returns:
            An integer representing the score of the strategy. The score is calculated as follows:

            * Win: 6 points
            * Draw: 3 points
            * Loss: 0 points

        Raises:
            ValueError: If the strategy string is not in the correct format.
        """
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
    """Calculates the score of a rock-paper-scissors choice.

        Args:
            strategy: A string representing the rock-paper-scissors choice, in the format "X", "Y", or "Z".

        Returns:
            An integer representing the score of the choice. The score is calculated as follows:

            * Rock: 1 point
            * Paper: 2 points
            * Scissors: 3 points

        Raises:
            ValueError: If the strategy string is not in the correct format.
        """

    strategy = strategy.split(' ')[-1]

    match strategy:
        case 'X':
            return 1
        case 'Y':
            return 2
        case 'Z':
            return 3


def calculate_total_score(strategies: list) -> int:
    """Calculates the total score of a list of rock-paper-scissors strategies.

        Args:
            strategies: A list of strings representing the rock-paper-scissors strategies, in the format
                "opponent's choice player's choice". For example, ["A X", "B Y", "C Z"] represents the
                list of strategies where the opponent chooses "rock", "paper", and "scissors", respectively, and
                the player chooses "rock", "paper", and "scissors", respectively.

        Returns:
            An integer representing the total score of the strategies.

        Raises:
            ValueError: If any of the strategy strings are not in the correct format.
        """

    total_score = 0
    for strategy in strategies:
        total_score += get_rps_score(strategy) + get_choice_score(strategy)
    print(f"The total score is: {total_score}")
    return total_score


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # part A
    input_file = 'input.txt'
    score_pairs: list = file2list(input_file)
    calculate_total_score(score_pairs)
