

passengers=['Lopez', 'Chen', 'Okafor', 'Smith', 'Patel']

def print_boarding_list(passengers):
    for seat, passenger in enumerate(passengers, start=10):
        print(f'seat {seat}: {passenger}')
    return enumerate(passengers)

print_boarding_list(passengers)

