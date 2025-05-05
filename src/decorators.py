from functools import wraps


def log(filename=None):
    """
    Декоратор, который записывает в файл или в консоль статус выполнения функции"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                message = f'{func.__name__} error: {e}. Inputs: {args, kwargs}'
            else:
                message = f'{func.__name__} ok'
            finally:
                if filename:
                    with open(filename, 'w', encoding='utf-8') as file:
                        file.write(message)
                else:
                    print(message)
                return result
        return wrapper
    return decorator
