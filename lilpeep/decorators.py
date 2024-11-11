def log_message(func):
    def wrapper(*args, **kwargs):
        print(f"Виклик функції {func.__name__}")
        return func(*args, **kwargs)
    return wrapper