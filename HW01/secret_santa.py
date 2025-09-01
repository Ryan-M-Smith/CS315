#
# Filename: secret_santa.py | Homework 1
# Description: Implements a general “Secret Santa” problem, and outputs all the permissible combinations.
# Created: 2025-08-31
#

from itertools import product
from typing import cast

def parse_input() -> list[tuple[int, int]]:
    """
    Parses the input file and returns a list of tuples containing the pairs of integers.

    Returns:
        list[tuple[int, int]]: The input data as a list of tuples.
    """
    
    data: list[tuple[int, int]] = []
    
    with open("input.txt") as file:
        lines = file.readlines()
        
        for line in lines:
            a, b = map(int, line.split(","))
            data.append((a, b))
    
    return data

def write_output(data: list[tuple[int, int]]) -> None:
    """
    Writes the output data to a file.

    Args:
        data (list[tuple[int, int]]): The output data as a list of tuples.
    """
    
    with open("output.txt", "w") as file:
        for a, b in data:
            file.write(f"{a},{b}\n")

def main():
    """ The main function. """
    
    NUM_PEOPLE = int(input("How many people are participating? "))
    
    impermissible = parse_input()
    combinations = list(product(range(NUM_PEOPLE), repeat=2))
    
    valid = list(filter(lambda c: c not in impermissible, combinations))
    valid = cast(list[tuple[int, int]], valid)
    
    print(f"There are {len(valid)} valid combinations.")
    
    write_output(valid)
    print("Output saved to output.txt.")

if __name__ == "__main__":
    import sys
    sys.exit(main())