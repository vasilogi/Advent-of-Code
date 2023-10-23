# aim: the number of Calories each Elf is carrying

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


def calculate_total_calories(filepath='input.txt'):
    """
        Calculate the total calories carried by each elf and identify the elf with the most calories.

        This function reads calorie values from a text file, calculates the total calories carried by each elf,
        and identifies the elf with the maximum total calories.

        Args:
            filepath (str): The path to the input text file. Default is 'input.txt'.

        Returns:
            tuple: A tuple containing two values:
                - int: The index of the elf with the most total calories.
                - int: The maximum total calories carried by an elf.
    """
    lines = file2list(filepath)
    calories = []
    sum_calories = []
    for line in lines:
        if line:
            calories.append(int(line))
        else:
            sum_calories.append(sum(calories))
            calories = []
    return sorted(sum_calories, reverse=True)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # part A
    input_file = 'input.txt'
    total_calories = calculate_total_calories(input_file)
    print(f"The elf carrying out the maximum total Calories, carries : {total_calories[0]}")

    # part B
    max_three = sum(total_calories[:3])
    print(f"The total Calories carried by the top three elves is: {max_three}")
