class Part1:

    def solution(file_lines: list[str]) -> int:
        result = 0
        dial_value = 50

        for line in file_lines:
            if not line or len(line) < 2:
                print(f'error: invalid line "{line}"')
                continue

            direction = line[0]
            try:
                step = int(line[1:])
            except ValueError:
                print(f'error: invalid number in "{line}"')
                continue

            if direction == 'L':
                dial_value = (dial_value - step) % 100
            elif direction == 'R':
                dial_value = (dial_value + step) % 100
            else:
                print(f'error: unknown direction in "{line}" dial={dial_value}')
                continue

            if dial_value == 0:
                result += 1
                print(f"result: {result}")

            print(f"dial_value: {dial_value}")

        return result


class Part2:

    def solution(file_lines: list[str]) -> int:
        dial_value = 50
        result = 0
        for line in file_lines:
            line = line.strip()
            direction = line[0]
            step = int(line[1:])
            if direction == 'L':
                new_position = (dial_value - step) % 100
                if new_position > dial_value != 0:
                    result += 1
            elif direction == 'R':
                new_position = (dial_value + step) % 100
                if new_position < dial_value and new_position != 0:
                    result += 1
            else:
                raise ValueError("Invalid direction.")

            dial_value = new_position

            if dial_value == 0:
                result += 1
            number_of_rotations = step // 100
            result += number_of_rotations

        return result

# with open("test_input2.txt", "r") as file:
with open("input.txt", "r") as file:
    f = file.read().splitlines()

# print(f"Test input: {Part1.solution(f)}")
# print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
