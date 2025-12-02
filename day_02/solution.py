import re


class Part1:

    @staticmethod
    def solution(file_lines: list[str]) -> int:
        result = 0
        range_list = file_lines[0].split(',')

        for minmax in range_list:
            min_max = minmax.split('-')
            min: int = int(min_max[0])
            max: int = int(min_max[1])

            for i in range(min,max + 1):

                if bool(re.search(r'^(.*)\1$', str(i))):
                    print(f'funky data found : {i}' )
                    result += i


        return result

class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        range_list = file_lines[0].split(',')
        result = 0

        for minmax in range_list:
            min_max = minmax.split('-')
            min: int = int(min_max[0])
            max: int = int(min_max[1])

            for i in range(min,max + 1):

                if bool(re.search(r'^(\d+)\1+$', str(i))):
                    print(f'funky data found : {i}' )
                    result += i


        return result



# with open("test_input.txt", "r") as file:
with open("input.txt", "r") as file:
    f = file.read().splitlines()

# print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")



