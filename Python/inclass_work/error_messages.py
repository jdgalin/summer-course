def divide_numbers(a, b):
    if b!=0: return a / b
    else: return None

def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    avg = divide_numbers(total, count)
    return avg

def process_scores(score_list):
    average = calculate_average(score_list)
    print(f"Average score: {average}")
    return average

scores = []
process_scores(scores)