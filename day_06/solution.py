import math
import re

class Part1:
    @staticmethod
    def solution(_matrix: list[list[str]]) -> int:
        result = 0

        column_index = 0  # To get the second column (index 1)

        col_count = len(_matrix[0])

        for c in range(column_index,col_count):
            column = [row[c] for row in _matrix]
            column.reverse()
            sign = column[0]
            int_list = [int(s) for s in column[1:]]
            if sign == '+':
                result += sum(int_list)
            else:
                result += math.prod(int_list)

        return result


def do_math(sign, numerals)-> int:
    if sign == "add":
        return sum(numerals)
    elif sign == "multiply":
        return math.prod((numerals))
    else:
        return 0

def pad_number(match):
    number = int(match.group(1))
    return format(number, "03d")

class Part2:
    def solution(grid: list[str]) -> int:
        result = 0

        column_index = 0  # To get the second column (index 1)

        col_count = len(grid[0])

        sign = "+"
        cols = list(zip(*grid))

        groups = []
        group = []

        for col in cols:
            if set(col) == {" "}:
                groups.append(group)
                group = []
            else:
                group.append(col)

        groups.append(group)

        total = 0

        for group in groups:
            total += eval(group[0][-1].join("".join(line[:-1]) for line in group))

        print(total)


with open("input.txt", "r") as file:

    grid = [line.rstrip('\n') for line in open("input.txt")]
    # grid = file.readlines()
#     clean_list = []
#     for line in f:
#         line = line.strip()
#         while "  " in line:
#             line = line.replace("  ", " ")
#         clean_list.append(line)
# 
# 
# filtered_list = [item for item in clean_list if item]
# 
# ff = [list(line.split(" "))for line in filtered_list]

# grid = [line.strip("\n") for line in open("test_input.txt")]



# print(f"Part 1: {Part1.solution(ff)}")
print(f"Part 2: {Part2.solution(grid)}")

# print(f"Part 2: {Part2.solution('input.txt')}")
