def add(*args):
    sum = 0
    for any_num in args:
        sum += any_num
    return sum

print(add(100, 200, 300))

def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]

calculate(5, add=3, multiply=5)


def test(*args):
    print(args)


test(1, 2, 3, 5) #output becomes a tuple


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64) #args becomes tuple and kwargs become dictionary

