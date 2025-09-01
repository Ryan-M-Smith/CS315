#
# Filename: secret_santa.py | Homework 1
# Description: Implements a general “Secret Santa” problem, and outputs all the permissible combinations.
# Created: 2025-08-31
#

from itertools import permutations

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
    
    NUM_PEOPLE = 6
    impermissible = set(parse_input())
    people = list(range(NUM_PEOPLE))
    valid_assignments = []
    
    print(f"Finding valid Secret Santa assignments for {NUM_PEOPLE} people with {len(impermissible)} impermissible pairs (input.txt)...")

    # Generate all possible Secret Santa assignments (permutations)
    for receivers in permutations(people):
        # Each giver could theoretically give to each receiver (before checking constraints)
        assignments = list(zip(people, receivers))
        
        #
        # People cannot give gifts to themselves and must not be in the impermissible pairs.
        # If either of these rules are not met, the assignment is invalid.
        #
        valid = True
        for giver, receiver in assignments:
            if giver == receiver or (giver, receiver) in impermissible:
                valid = False
                break
        
        if valid:
            valid_assignments.append(assignments)

    print(f"There are {len(valid_assignments)} valid Secret Santa assignments.")

    # Write all valid assignments to output.txt
    with open("output.txt", "w") as file:
        for assignment in valid_assignments:
            file.write(", ".join(f"{giver} -> {receiver}" for giver, receiver in assignment) + "\n")
    print("Output saved to output.txt.")

if __name__ == "__main__":
    import sys
    sys.exit(main())