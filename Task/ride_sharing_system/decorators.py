"""Decorators for the Ride Sharing System."""


def ride_logger(func):
    """Print a message after a ride is booked successfully.

    If func raises an error, the line after it never runs,
    so the message only shows for a successful booking.
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("\nRide booked successfully!")
        return result
    return wrapper
