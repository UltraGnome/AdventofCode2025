import re


class Part1:

    @staticmethod
    def solution(file_lines: list[str]) -> int:
        result = 0
        range_list = file_lines[0].split(',')

        print(len(range_list))

        for minmax in range_list:
            min_max = minmax.split('-')
            min: int = int(min_max[0])
            max: int = int(min_max[1])

            for i in range(min,max):
                # The regex pattern (.+)\1+ looks for:
                # (.+) : Any character (except newline) one or more times, captured in group 1.
                # \1+  : One or more occurrences of the content captured in group 1.
                # We add a check for digits specifically by ensuring the captured group only contains digits.
                # This is done by adding \d+ inside the capturing group.
                if bool(re.search(r'(\d+)\1+', str(i))):
                    print(f'funky data found : {i}' )
                    result += i


        return result

class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        result = 0

        for line in file_lines:


          return result



with open("test_input.txt", "r") as file:
# with open("input.txt", "r") as file:
    f = file.read().splitlines()

print(f"Part 1: {Part1.solution(f)}")
# print(f"Part 2: {Part2.solution(f)}")



