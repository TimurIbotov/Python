def decor(func):
    def wrapper(*args, **kwargs):
        print("start")
        val = func(*args, **kwargs)
        print("end")
        return val

    return wrapper

@decor
def p(x):
    return x*x

a = p(4)

print(a)