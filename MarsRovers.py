#!/usr/bin/env python3
import sys
import re


def main():
    if len(sys.argv) < 2:
        print("please provide a file containing input instructions")
        return

    for filename in sys.argv[1:]:
        try:
            file = open(filename)
            width, height = extract_width_and_height(file.readline())
            robots = []
            for line in file:
                robot, instructions = extract_start_instructions(line)
                for instruction in instructions:
                    if instruction == "F":
                        robot.forward(width, height)
                        if robot.lost:
                            break
                    elif instruction == "L":
                        robot.left()
                    elif instruction == "R":
                        robot.right()
                robots.append(robot)

            if len(sys.argv) > 2:
                print(f"===={filename}====")
            for robot in robots:
                print(
                    f"({robot.x}, {robot.y}, {robot.direction}){' LOST' if robot.lost else ''}"
                )

        except FileNotFoundError:
            print(f"File {filename} is not found")
            return
        except ValueError as e:
            print(f"File {filename} is incorrectly formatted {e}")
            return


def extract_width_and_height(first_line):
    # matches digits then whitespace then digits then optional whitespace then EOL
    # regex might be controversial, and in this case a sledgehammer to crack a walnut,
    # but I like it for this task, especially later parts
    match = re.match("(\d+)\s+(\d+)\s*\n", first_line)
    if match == None:
        raise ValueError(f"Invalid first line {first_line}")
    else:
        width = int(match.group(1))
        height = int(match.group(2))
        return width, height


def extract_start_instructions(line):
    # matches lines of the form (int, int, [N|E|S|W]) [FLR]*
    # doesn't care about whitespace, this is what the regex really excels at
    match = re.match("\((\d+)\s*,\s*(\d+)\s*,\s*([NSEW])\s*\)\s*([LRF]*)\n", line)
    if match == None:
        raise ValueError(f"Invalid line {line}")
    else:
        position = RobotPosition(
            int(match.group(1)), int(match.group(2)), match.group(3)
        )
        instructions = match.group(4)
        return position, instructions


class RobotPosition:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.lost = False

    def left(self):
        # dir could be an enum, in a more strongly typed language I'd say definiely
        # here I think it doesn't add much.
        if self.direction == "N":
            self.direction = "W"
        elif self.direction == "E":
            self.direction = "N"
        elif self.direction == "S":
            self.direction = "E"
        elif self.direction == "W":
            self.direction = "S"

    def right(self):
        if self.direction == "N":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "W"
        elif self.direction == "W":
            self.direction = "N"

    def forward(self, width, height):
        if self.direction == "N":
            if self.y >= height:
                self.lost = True
            else:
                self.y += 1
        elif self.direction == "E":
            if self.x >= width:
                self.lost = True
            else:
                self.x += 1
        elif self.direction == "S":
            if self.y <= 0:
                self.lost = True
            else:
                self.y -= 1
        elif self.direction == "W":
            if self.x <= 0:
                self.lost = True
            else:
                self.x -= 1


if __name__ == "__main__":
    main()
