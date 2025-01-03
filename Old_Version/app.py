from pprint import pprint as pp

class Flight:
    def __init__(self, flight_number, airplane):
        self.flight_number = flight_number
        self.airplane = airplane

        rows, seats = self.airplane.get_seating_plan()
        # self.seating_plan = [x for x in rows]
        # self.seating_plan = [row for row in rows]
        # self.seating_plan = [{key: value for '?' in iterable} for _ in rows]
        # self.seating_plan = [{key: value for '?' in seats} for _ in rows]
        self.seating_plan = [None] + [{letter: None for letter in seats} for _ in rows]
        # result = ['I will not swearing' for _ in range(100)]

    def get_airline(self):
        return self.flight_number[:2]

    def get_flight_number(self):
        return self.flight_number[2:]

    def get_model(self):
        return self.airplane.get_airplane_model()

    def _parse_seat(self, seat):
        rows, seats = self.airplane.get_seating_plan()

        letter = seat[-1]

        if letter not in seats:
            raise ValueError(f'Invalid seat letter: {letter}')

        row_text = seat[:-1]

        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f'Invalid row number: {row_text}')

        if row not in rows:
            raise ValueError(f'Row number is out of range: {row}')

        return row, letter

    def allocate_passenger(self, passenger, seat):
        row, letter = self._parse_seat(seat)

        if self.seating_plan[row][letter] is not None:
            raise ValueError(f'Seat is already taken: {seat}')

        self.seating_plan[row][letter] = passenger

    def relocate_passenger(self, seat_from, seat_to):
        row_from, letter_from = self._parse_seat(seat_from)

        if self.seating_plan[row_from][letter_from] is None:
            raise ValueError(f'Seat_from is not occupied : {seat_from}')

        row_to, letter_to = self._parse_seat(seat_to)

        if self.seating_plan[row_to][letter_to] is not None:
            raise ValueError(f'Seat_to is occupied : {seat_to}')

        self.seating_plan[row_to][letter_to] = self.seating_plan[row_from][letter_from]
        self.seating_plan[row_from][letter_to] = None

    def get_empty_seat(self):
        return sum(sum(1 for seat in row.values()
                        if seat is None)
                    for row in self.seating_plan if row is not None)

        # return sum(len([seat for seat in row.values()
        #                if seat is None])
        #            for row in self.seating_plan if row is not None)

        # total = 0
        #
        # for row in self.seating_plan:
        #     if row is not None:
        #         for passenger in row.values():
        #             if passenger is None:
        #                 total += 1
        # return total

    def get_passenger_list(self):
        rows, seats = self.airplane.get_seating_plan()

        for row in rows:
            for letter in seats:
                passenger = self.seating_plan[row][letter]
                if passenger is not None:
                    yield passenger, f'{row} {letter}'

    def print_tickets(self, printer):
        for passenger, seat in self.get_passenger_list():
            printer(passenger, seat, self.get_model(), self.flight_number)





class Airplane:
    def get_seats_no(self):
        rows, seats = self.get_seating_plan()
        return len(rows) * len(seats)


class AirbusA380(Airplane):
    @staticmethod
    def get_airplane_model():
        return 'Airbus 380'

    @staticmethod
    def get_seating_plan():
        return range(1, 26), 'ABCDEG'


class Boeing737Max(Airplane):
    @staticmethod
    def get_airplane_model():
        return 'Boeing737Max'

    @staticmethod
    def get_seating_plan():
        return range(1, 46), 'ABCDEGHJK'

def card_printer(passenger, seat, airplane, flight_number):
    message = f'| Passenger: \033[91m{passenger.title()}\033[0m, Seat: {seat}, Airplane: {airplane}, {flight_number} |'
    frame = f'+{'-' * (len(message) -2)}+'
    empty_frame = f'|{' ' * (len(message) -2)}|'

    banner = [frame, empty_frame,empty_frame,empty_frame, message, empty_frame,empty_frame,empty_frame, frame]
    print('\n'.join(banner))


plane = Airplane()
airbus = AirbusA380()
boeing = Boeing737Max()
f = Flight('LO127', airbus)
# print(boeing.get_seating_plan())
# print(f.get_airline())
# print(f.get_flight_number())
# print(airbus.get_airplane_model())
# print(boeing.get_airplane_model())
# print(f.get_model())
# print(boeing.get_seating_plan())
# print(airbus.get_seating_plan())
f.allocate_passenger(passenger='Lech K', seat='12B')
f.allocate_passenger(passenger='Donald T', seat='12C')
f.allocate_passenger(passenger='Jaro K', seat='13C')
f.relocate_passenger('13C', '25G')
# # f.allocate_passenger(passenger='Parasite', seat='32C')
# print(f.get_empty_seat() == airbus.get_seats_no())
# pp(f.seating_plan)
# for passenger in f.get_passenger_list():
#     print(passenger)
f.print_tickets(card_printer)
