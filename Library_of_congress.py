import os
import sys


def collect_file():
    return str(sys.argv[1])


def name_without_extension(file_name):
    name_without_extension = os.path.splitext(file_name)[0]
    return name_without_extension


def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        data_dict = {}
        for line in file:
            text, line_number = line.strip().split("|")
            data_dict[int(line_number)] = text

    return data_dict


def sort_dict(my_dict):
    tuple_of_tuples = tuple((key, value) for key, value in my_dict.items())
    sorted_tuple = sorted(tuple_of_tuples)
    return dict(sorted_tuple)

def find_longest_line(my_dict):
    longest_value = None
    longest_key = None
    longest_length = 0

    for key, value in my_dict.items():
        if len(value) >= longest_length:
            longest_key = key
            longest_value = value
            longest_length = len(value)

    return f'Longest line ({longest_key}): {longest_value}'

def average_length(my_dict):
    total_characters = 0
    number_of_lines = 0

    for value in my_dict.values():
        total_characters += len(value)
        number_of_lines += 1

    average = int(total_characters / number_of_lines)
    return f"Average length: {average}"

def write_results_to_file(output_file, input_file):
    with open(output_file, "w", encoding="utf-8") as file:
        data = read_file(input_file)
        sorted_data = sort_dict(data)
        longest_line = find_longest_line(sorted_data)
        avg_len = average_length(sorted_data)

        file.write(name_without_extension(input_file) + "\n")
        file.write(longest_line + "\n")
        file.write(avg_len)

if __name__ == "__main__":
    input_file = collect_file()
    output_file = os.path.splitext(input_file)[0] + "_book.txt"
    write_results_to_file(output_file, input_file)



