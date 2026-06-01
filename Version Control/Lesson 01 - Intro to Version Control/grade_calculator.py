"""
Grade Calculator
Calculates student grades and determines pass/fail status
"""

def calculate_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)


def get_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'


def is_passing(average):
    return average >= 60

