import csv

def difference_between_months(csv_file, start_year, start_month, end_year, end_month):
    """
    This function is used to determine how many workers were added to the work force
    in that presidents term.

    :param csv_file:
    :param start_year:
    :param start_month:
    :param end_year:
    :param end_month:
    :return: Difference from the start of the presidents term and the end
    """
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)

        header = next(csv_reader)

        start_month_index = header.index(start_month)
        end_month_index = header.index(end_month)

        employee_counts = {}

        for row in csv_reader:
            year = int(row[0])


            if start_year <= year <= end_year:
                if year == start_year:
                    employee_counts[start_month] = int(row[start_month_index])

                if year == end_year:
                    employee_counts[end_month] = int(row[end_month_index])

    if start_month in employee_counts and end_month in employee_counts:
        difference = employee_counts[end_month] - employee_counts[start_month]
        return difference
    else:
        return None

def sum_of_party(csv_file):
    """
    This function takes in teh presidentd csv file and calculates the total of each parties
    contribution to the job market.
    :param csv_file:
    :return: democrat_total, republican_total, statement
    """
    democrat_total = 0
    republican_total = 0
    with open(csv_file, "r") as file:

        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            sum_of_jobs = int(difference_between_months("BLS_private.csv", int(row["start_year"]), row["start_month"], int(row["end_year"]), row["end_month"]))
            if row["party"] == "Democrat":
                democrat_total += sum_of_jobs
            elif row["party"] == "Republican":
                republican_total += sum_of_jobs

    democrat_total *= 1000
    republican_total *= 1000

    statement = f"The total amount of jobs created under the Democratic party {democrat_total} and the total jobs created under the Republican party were {republican_total}. "
    return [democrat_total, republican_total, statement]



def main():
    result = sum_of_party("presidents.csv")
    if result[0] > result[1]:
        solution_statement = ["Bill Clinton was right. ", result[2],
    "These numbers were attained through going through every presidents term and getting the difference from the start of their term to the end of their term." ]
    elif result[1] > result[0]:
        solution_statement = ["Bill Clinton was wrong", result[2],
    "These numbers were attained through going through every presidents term and getting the difference from the start of their term to the end of their term." ]
    else:
        solution_statement = ["There is something wrong with the data or the code please try to run the program again."]
    with open("conclusion.md", "w") as file:
        file.writelines(solution_statement)



if __name__ == "__main__":
    main()
