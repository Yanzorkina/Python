from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        result = func(*args)
        for arg in args:
            print(f"{func.__name__} ({arg}: {type(arg)}), ")
        return result

    return wrapper


@type_logger
def calc_cube(*args):
    result = []
    for i in args:
        result.append(i ** 3)

    return result


print(calc_cube(3.3, 2, 6))

