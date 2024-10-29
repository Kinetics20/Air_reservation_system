from helpers import card_printer
from planes import AirbusA380, Airplane, Boeing737Max
from flight import Flight


def main():
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

# main()
if __name__ == '__main__':
    main()