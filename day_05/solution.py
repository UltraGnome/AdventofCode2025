class Part1:
    def solution(file_lines: list[str]) -> int:
        result = 0
        fresh_ranges = []

        for line in file_lines:
            if "-" in line:
                fresh_ranges.append(str(line.strip()))
            elif len(line.strip()) == 0:
                continue
            else:
                for _range in fresh_ranges:
                    rangepair = _range.split('-')
                    minny = int(rangepair[0])
                    maxxy = int(rangepair[1])
                    if int(line.strip()) in range(minny, maxxy + 1):
                        result += 1; break
        return result

class Part2:
    def solution(filename: str) -> int:

        ranges, _ = open(filename, "r").read().split("\n\n")
        ranges = [list(map(int, r.split("-"))) for r in ranges.splitlines()]

        # fresh_ranges = []
        #
        # for line in file_lines:
        #     if "-" in line:
        #        fresh_ranges.append(line)
        #     else:
        #         break
        # too damn slow below
        # for pair in fresh_ranges:
        #     rangepair = pair.split('-')
        #     minny = int(rangepair[0])
        #     maxxy = int(rangepair[1])
        #     for _id in range(minny,maxxy + 1):
        #         fresh_ids.append(_id)
        #         print(_id)
        #
        # return len(set(fresh_ids))
        # fresh_ranges.sort()
        #
        # last = None
        # result = 0
        #
        # for pair in fresh_ranges:
        #     rangepair = pair.split('-')
        #     if last is None:
        #         last = (int(rangepair[0]), int(rangepair[1]))
        #     elif last[1] < int(rangepair[0]):
        #         result += last[1] - last[0] + 1 # calculate rather than loop over each
        #         last = (int(rangepair[0]), int(rangepair[1]))
        #     else:
        #         last = (last[0], max(last[1], int(rangepair[1])))
        #
        # result += last[1] - last[0] + 1
        # return result
        ranges.sort()

        last = None
        count = 0

        for lo, hi in ranges:
            if last is None:
                last = (lo, hi)
            elif last[1] < lo:
                count += last[1] - last[0] + 1
                last = (lo, hi)
            else:
                last = (last[0], max(last[1], hi))

        count += last[1] - last[0] + 1
        return count


# with open("test_input.txt", "r") as file:
# with open("test_input.txt", "r").read().split("\n\n"):
# with open("input.txt", "r") as file:
     # only get lines until the blank line



# print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution('input.txt')}")



