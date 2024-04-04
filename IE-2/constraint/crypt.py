from itertools import permutations

def solve_cryptarithmetic(puzzle):
    words = puzzle.split()
    # SEND + MORE = MONEY
    unique_chars = set(char for word in words for char in word if char.isalpha())
    if len(unique_chars) > 10:
        print("Invalid puzzle: More than 10 unique characters")
        return

    for perm in permutations(range(10), len(unique_chars)):
        mapping = dict(zip(unique_chars, perm))

        nums = []
        for word in words[:-1]:
            num_str = "".join(str(mapping.get(char, char)) for char in word if char.isalpha())
            if num_str:
                nums.append(int(num_str))
                
        try:
            result_str = "".join(str(mapping.get(char, char)) for char in words[-1] if char.isalpha())
            if result_str and sum(nums) == int(result_str):
                print("Solution found:")
                print(mapping)
                return

        except ValueError:
            pass
    print("No solution found.")

puzzle_input = input("Enter the cryptarithmetic puzzle: ")
solve_cryptarithmetic(puzzle_input)
