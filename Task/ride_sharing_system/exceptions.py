"""Custom exceptions for the Ride Sharing System.

Every custom exception inherits from RideError, and RideError
inherits from Python's built-in Exception class.
So `except RideError` catches all of them in one place.
"""


class RideError(Exception):
    """Parent of every ride-sharing error."""
    pass


class InvalidRatingError(RideError):
    """Rating is not between 1 and 5."""
    pass


class InvalidDistanceError(RideError):
    """Distance is zero or negative."""
    pass


class InvalidVehicleError(RideError):
    """Vehicle type is not Bike or Car."""
    pass
