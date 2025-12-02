class Part1:

    def solution(file_lines: list[str]) -> int:
      result = 0

      dial_value = 50

      for line in file_lines:
          if line.startswith('L') and int(line[1:]) >= 100:
            step = int(line[1:]) % 100
            dial_value = (dial_value - step)
            if dial_value < 0:
              dial_value = 100 + (dial_value)
            if dial_value == 0:
              result = result + 1
              print(f"result: {result}")
            print(f"dial_value: {dial_value}")
          elif line.startswith('L') and dial_value - int(line[1:]) in range(1, 99) :
              dial_value = (dial_value - int(line[1:]))
              print(f"dial_value: {dial_value}")
          elif line.startswith('L') and dial_value - int(line[1:]) < 0   :
              dial_value = 100 + (dial_value - int(line[1:]))
              print(f"dial_value: {dial_value}")
          elif line.startswith('L') and dial_value - int(line[1:]) == 0  :
              dial_value = 0
              result = result + 1
              print(f"result: {result}")

          elif line.startswith('R') and int(line[1:]) >= 100:
              step = int(line[1:]) % 100
              dial_value = (dial_value + step) - 100
              if dial_value < 0:
                  dial_value = 100 + (dial_value)
              if dial_value == 0:
                  result = result + 1
                  print(f"result: {result}")
              print(f"dial_value: {dial_value}")
          elif line.startswith('R') and dial_value + int(line[1:]) == 99:
              dial_value = 99
              print(f"dial_value: {dial_value}")
          elif line.startswith('R') and dial_value + int(line[1:]) in range(1, 99):
              dial_value = (dial_value + int(line[1:]))
              print(f"dial_value: {dial_value}")
          elif line.startswith('R') and dial_value + int(line[1:]) >= 100:
              dial_value = (dial_value + int(line[1:])) - 100
              if dial_value == 0:
                  result = result + 1
                  print(f"result: {result}")

              print(f"dial_value: {dial_value}")
          elif line.startswith('R') and dial_value + int(line[1:]) == 0  :
              dial_value = 0
              result = result + 1
              print(f"result: {result}")
          else :
              print('error ' + line + " dial=" + str(dial_value))

      return result



class Part2:

    def solution(file_lines: list[str]) -> int:
        result = 0

        dial_value = 50

        for line in file_lines:
            if line.startswith('L') and int(line[1:]) >= 100:
                spins = int(line[1:]) / 100
                step = int(line[1:]) % 100
                dial_value = (dial_value - step)
                if dial_value < 0:
                    dial_value = 100 + dial_value
                if dial_value == 0:
                    result = result + 1
                    print(f"result: {result}")
                result = result + spins
            elif line.startswith('L') and dial_value - int(line[1:]) in range(1, 99):
                dial_value = (dial_value - int(line[1:]))

            elif line.startswith('L') and dial_value - int(line[1:]) < 0:
                dial_value = 100 + (dial_value - int(line[1:]))
                result = result + 1
            elif line.startswith('L') and dial_value - int(line[1:]) == 0:
                dial_value = 0
                result = result + 1
                print(f"result: {result}")

            elif line.startswith('R') and int(line[1:]) >= 100:
                spins = int(line[1:]) / 100
                step = int(line[1:]) % 100
                dial_value = (dial_value + step) - 100
                if dial_value < 0:
                    dial_value = 100 + (dial_value)
                if dial_value == 0:
                    result = result + 1
                    print(f"result: {result}")
                result = result + spins

            elif line.startswith('R') and dial_value + int(line[1:]) == 99:
                dial_value = 99
            elif line.startswith('R') and dial_value + int(line[1:]) in range(1, 99):
                dial_value = (dial_value + int(line[1:]))
            elif line.startswith('R') and dial_value + int(line[1:]) >= 100:
                result = result + 1
                dial_value = (dial_value + int(line[1:])) - 100
                if dial_value == 0:
                    result = result + 1
                    print(f"result: {result}")
            else:
                print('error ' + line + " dial=" + str(dial_value))

        return result


with open("test_input2.txt", "r") as file:
# with open("input.txt", "r") as file:
    f = file.read().splitlines()

# print(f"Test input: {Part1.solution(f)}")
#print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
