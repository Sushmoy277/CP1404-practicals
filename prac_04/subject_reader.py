"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Display subject details from the data file."""
    subject_details = load_subject_details(FILENAME)
    display_subjects(subject_details)


def load_subject_details(filename):
    subject_details = []
    with open(filename) as input_file:
        for line in input_file:
            parts = line.strip().split(',')
            parts[2] = int(parts[2])
            subject_details.append(parts)
    return subject_details


def display_subjects(subjects):
    """Display subject data nicely."""
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]:3} students")


main()
