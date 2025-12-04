import re


class Part1:

    @staticmethod
    def solution(file_lines: list[str]) -> int:
        result = 0
        count = 0

        for bank in file_lines:
           count += 1

           first_pointer = 0
           first_index = 0
           second_pointer = 0

           first_digit = "0"
           second_digit = "0"

           while first_pointer < len(bank) - 1:
                if int((bank[first_pointer])) > int(first_digit):
                    first_digit = bank[first_pointer]
                    first_index = first_pointer
                    second_pointer = first_index + 1

                first_pointer += 1

           while second_pointer < len(bank):

               if int((bank[second_pointer])) > int(second_digit):
                   second_digit = bank[second_pointer]

               if second_digit == '9':
                   second_pointer = len(bank)
               else:
                   second_pointer += 1

           print(f"{count} - found: {first_digit}{second_digit} from {bank}" )

           result += int(first_digit + second_digit)

        return result

class Part2:

    @staticmethod
    def solution(file_lines: list[str]) -> int:
        result = 0
        count = 0

        for bank in file_lines:
            count += 1

            first_pointer = 0
            first_index = 0
            next_pointer = 0

            first_digit = "0"
            next_digit = "0"

            while first_pointer < len(bank) - 1:
                if int((bank[first_pointer])) > int(first_digit):
                    first_digit = bank[first_pointer]
                    first_index = first_pointer
                    next_pointer = first_index + 1

                first_pointer += 1

            while next_pointer < len(bank):

                if int((bank[next_pointer])) > int(next_digit):
                    next_digit = bank[next_pointer]

                    next_pointer += 1

            print(f"{count} - found: {first_digit}{second_digit} from {bank}")

            result += int(first_digit + second_digit)

        return result





# with open("test_input.txt", "r") as file:
with open("input.txt", "r") as file:
    f = file.read().splitlines()

print(f"Part 1: {Part1.solution(f)}")
# print(f"Part 2: {Part2.solution(f)}")



