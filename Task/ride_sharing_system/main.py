"""Ride Sharing System: the main program.

Run it from inside the ride_sharing_system folder:
    python main.py
"""

from vehicles import Bike, Car
from decorators import ride_logger
from exceptions import RideError, InvalidVehicleError

HISTORY_FILE = "ride_history.txt"


def nice_number(n):
    """12.0 -> 12, 12.5 -> 12.5 (so the output looks clean)."""
    if n == int(n):
        return int(n)
    return round(n, 2)


def create_vehicle(vehicle_type, driver_name, rating):
    """Make the right vehicle object from the user's choice."""
    if vehicle_type == "Bike":
        return Bike(driver_name, rating)
    elif vehicle_type == "Car":
        return Car(driver_name, rating)
    else:
        raise InvalidVehicleError(f"'{vehicle_type}' is not available. Choose Bike or Car.")


def save_ride(ride):
    """Add one ride to the end of ride_history.txt ("a" keeps old rides)."""
    line = (f"Driver: {ride['driver']} | Vehicle: {ride['vehicle']} | "
            f"Rating: {nice_number(ride['rating'])} | Distance: {nice_number(ride['distance'])} km | "
            f"Fare: Rs. {nice_number(ride['fare'])}\n")
    with open(HISTORY_FILE, "a") as f:
        f.write(line)


@ride_logger
def book_ride(vehicle, distance):
    """Calculate the fare, save the ride, and give back the ride details."""
    fare = vehicle.calculate_fare(distance)      # may raise InvalidDistanceError
    ride = {
        "driver": vehicle.driver_name,
        "vehicle": vehicle.vehicle_type,
        "rating": vehicle.rating,
        "distance": distance,
        "fare": fare,
    }
    save_ride(ride)                              # may raise OSError
    return ride


def show_ride(ride):
    print()
    print(f"Driver: {ride['driver']}")
    print(f"Vehicle: {ride['vehicle']}")
    print(f"Distance: {nice_number(ride['distance'])} km")
    print(f"Fare: Rs. {nice_number(ride['fare'])}")


def book_ride_flow():
    """Ask the user for ride details and book the ride."""
    try:
        vehicle_type = input("Enter Vehicle Type (Bike, Car): ").strip().capitalize()
        if vehicle_type not in ["Bike", "Car"]:
            raise InvalidVehicleError(f"'{vehicle_type}' is not available. Choose Bike or Car.")

        driver_name = input("Enter Driver Name: ").strip()
        if driver_name == "":
            raise RideError("Driver name cannot be empty.")

        rating = float(input("Enter Rating: "))
        vehicle = create_vehicle(vehicle_type, driver_name, rating)   # setter checks rating

        distance = float(input("Enter Distance: "))
        ride = book_ride(vehicle, distance)
        show_ride(ride)

    except ValueError:
        print("Error: Rating and distance must be numbers.")
    except RideError as e:                       # any of our custom errors
        print(f"Error: {e}")
    except OSError as e:                         # any file problem
        print(f"Error: Could not save the ride history. ({e})")


def show_history():
    """Read every ride from ride_history.txt."""
    try:
        with open(HISTORY_FILE, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("No rides yet. ride_history.txt does not exist.")
        return
    except OSError as e:
        print(f"Error: Could not read the ride history. ({e})")
        return

    if len(lines) == 0:
        print("No rides yet.")
        return

    print("\n----- Ride History -----")
    for number, line in enumerate(lines, start=1):
        print(f"{number}. {line.strip()}")


def main():
    print("===== Ride Sharing System =====")
    while True:
        print("\n1. Book a ride")
        print("2. View ride history")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            book_ride_flow()
        elif choice == "2":
            show_history()
        elif choice == "3":
            print("Thank you for riding with us!")
            break
        else:
            print("Please choose 1, 2 or 3.")


if __name__ == "__main__":
    main()
