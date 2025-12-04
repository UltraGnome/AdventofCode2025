import re


class Part1:

    @staticmethod
    def solution(file_lines: list[str]) -> int:
        def find_first_max(bank: str, pointer: int = 0, first_digit: str = "0", first_index: int = 0) -> tuple[
            str, int]:
            # Base case: reached end of string (excluding last character)
            if pointer >= len(bank) - 1:
                return first_digit, first_index

            # Check if current digit is greater than current max
            if int(bank[pointer]) > int(first_digit):
                return find_first_max(bank, pointer + 1, bank[pointer], pointer)
            else:
                return find_first_max(bank, pointer + 1, first_digit, first_index)

        def find_second_max(bank: str, pointer: int, second_digit: str = "0") -> str:
            # Base case: reached end of string or found '9'
            if pointer >= len(bank) or second_digit == '9':
                return second_digit

            # Check if current digit is greater than current max
            if int(bank[pointer]) > int(second_digit):
                return find_second_max(bank, pointer + 1, bank[pointer])
            else:
                return find_second_max(bank, pointer + 1, second_digit)

        def process_lines(lines: list[str], count: int = 0, result: int = 0) -> int:
            # Base case: no more lines to process
            if count >= len(lines):
                return result

            bank = lines[count]

            # Find first max digit
            first_digit, first_index = find_first_max(bank)

            # Find second max digit starting after first_index
            second_pointer = first_index + 1
            second_digit = find_second_max(bank, second_pointer)

            print(f"{count + 1} - found: {first_digit}{second_digit} from {bank}")

            # Recursive case: process next line
            return process_lines(lines, count + 1, result + int(first_digit + second_digit))

        return process_lines(file_lines)


# class Part2:

    # @staticmethod
    # def solution(file_lines: list[str]) -> int:
    #     result = 0
    #     count = 0
    #
    #     for bank in file_lines:
    #         count += 1
    #
    #         first_pointer = 0
    #         first_index = 0
    #         next_pointer = 0
    #
    #         first_digit = "0"
    #         next_digit = "0"
    #
    #         while first_pointer < len(bank) - 1:
    #             if int((bank[first_pointer])) > int(first_digit):
    #                 first_digit = bank[first_pointer]
    #                 first_index = first_pointer
    #                 next_pointer = first_index + 1
    #
    #             first_pointer += 1
    #
    #         while next_pointer < len(bank):
    #
    #             if int((bank[next_pointer])) > int(next_digit):
    #                 next_digit = bank[next_pointer]
    #
    #                 next_pointer += 1
    #
    #         print(f"{count} - found: {first_digit}{second_digit} from {bank}")
    #
    #         result += int(first_digit + second_digit)
    #
    #     return result
    #



with open("test_input.txt", "r") as file:
# with open("input.txt", "r") as file:
    f = file.read().splitlines()

print(f"Part 1: {Part1.solution(f)}")
# print(f"Part 2: {Part2.solution(f)}")



