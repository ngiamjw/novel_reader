import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python script.py arg1 arg2")
        sys.exit(1)

    database = sys.argv[1]
    dna = sys.argv[2]

    # TODO: Read database file into a variable
    data_list = []
    names_list = []
    keys = []

    with open(database, newline='') as csvfile:
        csvreader = csv.reader(csvfile)

        next(csvreader)
        for row in csvreader:
            name = row[0]
            variables = {'AGATC': row[1], 'AATG': row[2], 'TTTTTTCT': row[3], 'TCTAG': row[4], 'GATA': row[5], 'TATC': row[6],'GAAA': row[7], 'TCTG': row[8]}
            data_list.append(variables)
            names_list.append(name)
            keys = variables.keys()

    # TODO: Read DNA sequence file into a variable

    with open(dna, 'r') as file:
        dna_contents = file.read()

    # TODO: Find longest match of each STR in DNA sequence

    longest_str = {key:str(longest_match(dna_contents, key)) for key in keys}
    print(longest_str)
    print(data_list[13])

    # TODO: Check database for matching profiles
    for number in range(len(names_list)):
        if data_list[number] == longest_str:
            print(names_list[number])
            exit(0)
    print("No match")

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()

