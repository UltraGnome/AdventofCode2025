class Part1:

    @staticmethod
    def solution(_matrix: list[str]) -> int:
        result = 0


        for x, row in enumerate(_matrix):
            for y, roll in enumerate(row):
                print(roll)
                if roll != '@': continue
                section = [chunk[max(0,y - 1):y + 2] for chunk in _matrix[max(0,x - 1):x + 2]]
                adjacent_rolls = sum(row.count("@") for row in section)
                if adjacent_rolls <= 4: #includes current position roll
                  result += 1

        return result


class Part2:
    @staticmethod
    def solution(_matrix: list[list[str]]) -> int:
        result = 0

        while 1:
            locked_rolls = [row[:] for row in _matrix]  # the collection of un-removable rolls
            pass_count = 0  # count for this iteration of checks
            for x, row in enumerate(_matrix):
                for y, roll in enumerate(row):
                    # print(roll)
                    if roll != '@': continue
                    section = [chunk[max(0,y - 1):y + 2] for chunk in _matrix[max(0,x - 1):x + 2]]
                    adjacent_rolls = sum(row.count("@") for row in section)
                    if adjacent_rolls <= 4: #includes current position roll
                        pass_count += 1
                        locked_rolls[x][y] = "."
            if pass_count == 0: break # no more rolls so we are done
            result += pass_count
            _matrix = locked_rolls

        return result

ff = [list(line.strip() )for line in open("input.txt", "r")]  # strings are immutable



# print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(ff)}")



