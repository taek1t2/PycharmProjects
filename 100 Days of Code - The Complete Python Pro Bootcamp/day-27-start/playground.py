def add(*args):
    sum = 0
    for any_num in args:
        sum += any_num
    print(args)

add(100, 200, 300)