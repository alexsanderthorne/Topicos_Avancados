def func(f):
    def wrapper(*args, **kwargs):
        rv = f(*args, **kwargs)

        return rv
    return wrapper


@func
def func2(x, y):
    print(x)
    return y


@func
def func3():
    print("i am func3")


x = func2(9, 8)
print(x)
func(0)
func3()
