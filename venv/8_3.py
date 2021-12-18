from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for arg in args:
            print(f"{func.__name__} ({arg}: {type(arg)}), ")
        for kwarg in kwargs.values():
            print(f"{func.__name__} ({kwarg}: {type(kwarg)}), ")
        return result

    return wrapper


@type_logger
def calc_cube(*args, **kwargs):
    result = []
    for i in args:
        result.append(i ** 3)
    for k in kwargs.values():
        result.append(k ** 3)

    return result


print(calc_cube(3.3, 2, 6, f=34))