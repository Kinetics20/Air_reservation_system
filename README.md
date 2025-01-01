# ✈️ Air Reservation System

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Notebook](https://img.shields.io/badge/Notebook-7.3.1-orange?logo=jupyter&logoColor=white)
![mypy](https://img.shields.io/badge/mypy-1.14.1-blueviolet?logo=mypy&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-8.3.4-yellow?logo=pytest&logoColor=white)
![Poetry](https://img.shields.io/badge/Poetry-1.x-65C2CB?logo=poetry&logoColor=white)
![PyCharm](https://img.shields.io/badge/PyCharm-2024.3.1.1-00D1B2?logo=pycharm&logoColor=white)

Welcome to the **Air Reservation System** project! This system allows you to manage airline ticket reservations, featuring models for airplanes like Airbus A380 and Boeing 737 Max. It includes functionalities such as passenger seat allocation and ticket printing.

## 🚀 Features
- **Airplane Models:** Airbus A380, Boeing 737 Max
- **Seat Allocation** for passengers
- **Ticket Printing** functionality

## 🛠️ Technologies Used
```toml
python = "^3.12"
mypy = "1.14.1"
pytest = "8.3.4"
```

## 📦 Installation and Setup

To get started with the project, follow these steps:

## How to Run?

1. Install `pipx` (a recommended way to manage Python tools):  
   ```bash
   sudo apt install pipx
   pipx ensurepath

2. Install Poetry using pipx:
    ```bash
    pipx install poetry
    ```

3. Install Mypy using Poetry:
    ```bash
    poetry add mypy
    ```

4. Install Jupyter Notebook using Poetry:
    ```bash
    poetry add 'pytest==8.3.4'
    ```

5. Run the application:

``` bash 
    python -m Air_reservation_system
```

 

## Update all dependencies:
```bash
poetry update
```



![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Poetry](https://img.shields.io/badge/Poetry-1.x-65C2CB?logo=poetry&logoColor=white)

## 🚀 How It Works

### Overview

The **Air Reservation System** is designed to manage airline ticket reservations, featuring different airplane models like **Airbus A380** and **Boeing 737 Max**. It allows for functions like passenger seat allocation, flight details, and ticket printing.

### File Structure
The project is divided into three main directories: `flight`, `helpers`, and `planes`.

### 1. `__main__.py`
The entry point of the system. It sets up the airplane models and flight, then allocates passengers to seats and prints tickets.

```python
from helpers import card_printer
from planes import AirbusA380, Airplane, Boeing737Max
from flight import Flight

def main():
    plane = Airplane()
    airbus = AirbusA380()
    boeing = Boeing737Max()
    f = Flight('LO127', airbus)
    f.allocate_passenger(passenger='Lech K', seat='12B')
    f.allocate_passenger(passenger='Donald T', seat='12C')
    f.allocate_passenger(passenger='Jaro K', seat='13C')
    f.relocate_passenger('13C', '25G')
    f.print_tickets(card_printer)

if __name__ == '__main__':
    main()
```


### 2. Planes Directory

Contains airplane models and their seating plans.

# Airplane Model Base Class
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
        return range(1, 31), 'ABCDEGHJK'

class Boeing737Max(Airplane):
    @staticmethod
    def get_airplane_model():
        return 'Boeing 737 Max'

    @staticmethod
    def get_seating_plan():
        return range(1, 46), 'ABCDEGHJK'

### 3. Helpers Directory

Contains the ticket printing function.

def card_printer(passenger, seat, airplane, flight_number):
    message = f'| Passenger: \033[91m{passenger.title()}\033[0m, Seat: {seat}, Airplane: {airplane}, {flight_number} |'
    frame = f'+{'-' * (len(message) - 2)}+'
    empty_frame = f'|{" " * (len(message) - 2)}|'

    banner = [frame, empty_frame, empty_frame, empty_frame, message, empty_frame, empty_frame, empty_frame, frame]
    print('\n'.join(banner))

### 4. flight Directory

Handles the flight operations such as allocating passengers, relocating them, and printing tickets.

class Flight:
    def __init__(self, flight_number, airplane):
        self.flight_number = flight_number
        self.airplane = airplane
        rows, seats = self.airplane.get_seating_plan()
        self.seating_plan = [None] + [{letter: None for letter in seats} for _ in rows]

    def allocate_passenger(self, passenger, seat):
        row, letter = self._parse_seat(seat)
        if self.seating_plan[row][letter] is not None:
            raise ValueError(f'Seat is already taken: {seat}')
        self.seating_plan[row][letter] = passenger

    def relocate_passenger(self, seat_from, seat_to):
        row_from, letter_from = self._parse_seat(seat_from)
        if self.seating_plan[row_from][letter_from] is None:
            raise ValueError(f'Seat_from is not occupied: {seat_from}')
        row_to, letter_to = self._parse_seat(seat_to)
        if self.seating_plan[row_to][letter_to] is not None:
            raise ValueError(f'Seat_to is occupied: {seat_to}')
        self.seating_plan[row_to][letter_to] = self.seating_plan[row_from][letter_from]
        self.seating_plan[row_from][letter_from] = None

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

📑 Summary

    The project uses object-oriented programming to represent airplanes and flights.
    It supports seat allocation, passenger management, and ticket printing.
    The system is highly modular, with separate components for planes, flight management, and helpers for ticket printing.

💬 Thank You!

Thank you for your interest in the Air Reservation System! Feel free to give feedback or ask any questions. Your input is highly appreciated. 😊✈️