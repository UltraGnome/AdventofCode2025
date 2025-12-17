from collections import deque
from functools import cache

class Part1:
    @staticmethod
    def solution(grid: list[str]) -> int:

        S = [(r_index, c) for r_index, row_string in enumerate(grid) for c, char in enumerate(row_string) if char == "S"][0]
        # deque - a double-ended queue for storing the beams
        beams = deque([S]) 
        visited = {S}  # S is the first visited point to be stored in the set.

        def add(r, c):
            if (r, c) in visited: return
            visited.add((r, c))
            beams.append((r, c))

        count = 0

        while len(beams) > 0:
            r, c = beams.popleft()
            if grid[r][c] == "." or grid[r][c] == "S":
                if r == len(grid) - 1: continue
                add(r + 1, c)
            elif grid[r][c] == "^":
                count += 1
                add(r, c - 1) # the left beam
                add(r, c + 1) # the right beam

        print(count)

        return count

class Part2:
    def solution(grid: list[str]) -> int:
        S = [(r, c) for r, row in enumerate(grid) for c, char in enumerate(row) if char == "S"][0]
        
        @cache
        def solve(r, c):
            if r >= len(grid): return 1

            if grid[r][c] == "." or grid[r][c] == "S":
                return solve(r + 1, c)
            elif grid[r][c] == "^":
                return solve(r, c - 1) + solve(r, c + 1)

        print(solve(*S))
# The asterisk (*) in print(solve(*S)) is used for iterable unpacking. It unpacks the elements of the variable S and passes them as separate positional arguments to the solve function.
# Here is a breakdown of how it works in the context of the code:
# S is an iterable: The variable S is expected to be an iterable (such as a list or a tuple) that contains exactly two elements, likely the starting row and column coordinates for the problem the code is solving.
# Unpacking: The *S expression tells Python to extract the elements from S and pass them individually to the function. For example, if S is (0, 0), the function call is effectively print(solve(0, 0)).
# Function arguments: The solve function is defined to accept two arguments, r (row) and c (column): def solve(r, c):. The unpacking ensures that the elements of S are correctly mapped to these two parameters.
# This allows the starting coordinates to be stored in a single variable S but used as two separate arguments when calling the solve function.
# The provided Python code defines a function solution that operates on a grid represented as a list of strings. It appears to be a recursive solution to a pathfinding or counting problem within this grid.
# Here is a breakdown of the code: def solution(grid: list[str]) -> int.
#     This defines a function named solution that takes one argument, grid, which is expected to be a list of strings. The -> int annotation indicates that the function is expected to return an integer.
# S = [(r, c) for r, row in enumerate(grid) for c, char in enumerate(row) if char == "S"]
# This line uses a list comprehension to find the coordinates (r, c) of the character 'S' within the grid.
# enumerate(grid) iterates through the rows of the grid, providing both the row index r and the row string.
# enumerate(row) then iterates through the characters in each row, providing the column index c and the char.
# if char == "S" filters for the character 'S'.
# [0]then takes the first (and presumably only) occurrence of 'S' found, assigning its coordinates as a tuple (r, c) to the variable S. This S represents the starting point.
# @cache.
# This is a decorator from functools (implicitly imported or assumed to be available in the context). It memoizes the results of the solve function. This means that if solve is called with the same arguments multiple times, the cached result will be returned instead of re-executing the function, significantly improving performance for recursive functions with overlapping subproblems.
# def solve(r, c):
#     This defines a recursive helper function solve that takes the current row r and column c as arguments. if r >= len(grid): return 1.
# This is the base case for the recursion. If the current row r is greater than or equal to the number of rows in the grid, it means a valid path has reached beyond the grid's bottom boundary. In this scenario, it returns 1, likely indicating one successful path.
# if grid[r][c] == "." or grid[r][c] == "S": return solve(r + 1, c)
# If the character at the current position (r, c) is either . (empty space) or S (start point), the path continues by moving one step down to the next row, keeping the same column. It recursively calls solve(r + 1, c).
# elif grid[r][c] == "^": return solve(r, c - 1) + solve(r, c + 1)
# If the character at the current position (r, c) is ^, it implies a branching point. The path can split and move either one step left (solve(r, c - 1)) or one step right (solve(r, c + 1)), while staying in the same row. The results of these two recursive calls are summed, suggesting that the function counts the total number of paths. print(solve(*S)).
# Finally, the solve function is called with the starting coordinates stored in S. The *S unpacks the tuple S into its individual r and c components as arguments for solve. The result, which represents the total number of paths found, is then printed to the console.
# In essence, this code explores paths in a grid, starting from 'S'. It moves downwards on '.' or 'S' cells and branches left and right on '^' cells, counting the total number of ways to reach beyond the bottom of the grid. The @cache decorator optimizes this exploration.
# 

# with open("test_input.txt", "r") as file:
with open("input.txt", "r") as file:
    f = file.read().splitlines()



# print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")

# print(f"Part 2: {Part2.solution('input.txt')}")
