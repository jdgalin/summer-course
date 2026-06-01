"""
Grade Calculator
Calculates student grades and determines pass/fail status
"""

def calculate_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)


def calculate_weighted_average(homework, exams, projects):
    hw_avg = calculate_average(homework)
    exam_avg = calculate_average(exams)
    proj_avg = calculate_average(projects)
    
    weighted = (hw_avg * 0.30) + (exam_avg * 0.05) + (proj_avg * 0.20)
    return weighted


def apply_bonus_points(average, participation_days, extra_credit_completed):
    bonus = min(participation_days * 0.1, 2.0)  # Max 2 points for participation
    bonus += extra_credit_completed * 1.0  # 1 point per extra credit
    
    final_average = min(average + bonus, 100)
    return final_average


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

