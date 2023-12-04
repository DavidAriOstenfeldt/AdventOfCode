from KMP import *

input_file = open("Day1_Input.txt", 'r', encoding='utf8')


def part_one():
    sum_total = 0
    for i, line in enumerate(input_file):
        first_val = ""
        last_val = ""
        for character in line:
            if character.isdigit():
                if first_val == "":
                    first_val = character
                last_val = character

        sum_total += int(str(first_val)+str(last_val))
        first_val = ""
        last_val = ""

    print("Part one: ", sum_total)

def part_two():
    sum_total = 0
    patterns = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, line in enumerate(input_file):
        digits_spelled = ""
        spelled_index = []
        digits_numbers = ""
        numbers_index = []
        for i, character in enumerate(line):
            if character.isdigit():
                numbers_index.append(i)
                digits_numbers += character

        for pat in patterns:
            text_to_digit = ""
            index = KMPSearch(pat, line)
            if index != []:
                if pat == "one":
                    text_to_digit = "1"
                elif pat == "two":
                    text_to_digit = "2"
                elif pat == "three":
                    text_to_digit = "3"
                elif pat == "four":
                    text_to_digit = "4"
                elif pat == "five":
                    text_to_digit = "5"
                elif pat == "six":
                    text_to_digit = "6"
                elif pat == "seven":
                    text_to_digit = "7"
                elif pat == "eight":
                    text_to_digit = "8"
                elif pat == "nine":
                    text_to_digit = "9"

                digits_spelled += text_to_digit * len(index)
                spelled_index.extend(index)

        spelled = len(spelled_index) > 0
        if spelled:
            spelled_first = min(spelled_index)
            spelled_last = max(spelled_index)
            spelled = True
        numbers = len(numbers_index) > 0
        if numbers:
            numbers_first = min(numbers_index)
            numbers_last = max(numbers_index)

        if spelled and numbers:
            first = min(spelled_first, numbers_first)
            if spelled_first < numbers_first:
                for ind, numb in enumerate(spelled_index):
                    if spelled_first == numb:
                        first = digits_spelled[ind]
            else:
                for ind, numb in enumerate(numbers_index):
                    if numbers_first == numb:
                        first = digits_numbers[ind]


            last = max(spelled_last, numbers_last)
            if spelled_last > numbers_last:
                for ind, numb in enumerate(spelled_index):
                    if spelled_last == numb:
                        last = digits_spelled[ind]
            else:
                for ind, numb in enumerate(numbers_index):
                    if numbers_last == numb:
                        last = digits_numbers[ind]

        elif spelled and not numbers:
            for ind, numb in enumerate(spelled_index):
                if spelled_first == numb:
                    first = digits_spelled[ind]
            for ind, numb in enumerate(spelled_index):
                if spelled_last == numb:
                    last = digits_spelled[ind]
        elif not spelled and numbers:
            for ind, numb in enumerate(numbers_index):
                if numbers_first == numb:
                    first = digits_numbers[ind]
            for ind, numb in enumerate(numbers_index):
                if numbers_last == numb:
                    last = digits_numbers[ind]

        sum_total += int(first + last)


    print("Part two: ", sum_total)


if __name__ == "__main__":
    part_two()

