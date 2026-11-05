def announce(func):
    def wrapper(*args, **kwargs):
        print("Calling", func.__name__)
        result = func(*args, **kwargs)
        return result
    return wrapper