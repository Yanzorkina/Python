from functools import wraps

def val_checker(lamb_f):
    def value_checker(func):

        @wraps(func)
        def wrapper(num):
            if lamb_f(num):
                print(func(num))
            else:

                raise ValueError(f'wrong value {num}')

        return wrapper
    return value_checker



@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

try:
    i = calc_cube(-9)
    print(calc_cube)
except (ValueError, TypeError) as e:
    print(e)
