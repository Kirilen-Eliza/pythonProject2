from functools import wraps
from typing import Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор, который записывает в файл или в консоль статус выполнения функции"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Optional[int], **kwargs: Optional[int]) -> Optional[int | None]:
            result = None
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                message = f"{func.__name__} error: {e}. Inputs: {args, kwargs}"
            else:
                message = f"{func.__name__} ok"
            finally:
                if filename:
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(message)
                else:
                    print(message)
                return result

        return wrapper

    return decorator
