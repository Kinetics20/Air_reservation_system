def card_printer(passenger, seat, airplane, flight_number):
    message = f'| Passenger: \033[91m{passenger.title()}\033[0m, Seat: {seat}, Airplane: {airplane}, {flight_number} |'
    frame = f'+{'-' * (len(message) -2)}+'
    empty_frame = f'|{' ' * (len(message) -2)}|'

    banner = [frame, empty_frame,empty_frame,empty_frame, message, empty_frame,empty_frame,empty_frame, frame]
    print('\n'.join(banner))
