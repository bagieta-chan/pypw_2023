import time
from time import sleep
from functools import wraps



def cached(fn):
    cache = {}

    @wraps(fn)
    def wrapper(*args, **kwargs):
        params = (args, tuple(kwargs.items()))
        if params not in cache:
            cache[params] = fn(*args, **kwargs)
        return cache[params]
    return wrapper




def time_it(fn):

    def wrapper(*args, **kwargs):

        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print(f"Duration: {end-start}")
        print(result())
        return result

    return wrapper

@time_it
def greeting():
    print("Hello World")
    sleep(3)


@cached
def fib_reccursive(n):
    if n in [0, 1]:
        return n

    return fib_reccursive(n-1)+fib_reccursive(n-2)



def fib_sequence(n: int)->int:
    if n in [0,1]:
        return n
    a, b = 0,1
    for i in range(n):
        yield a
        a, b = b, a+b

def is_prime(number: int)->bool:

    if number <= 1:
        return False
    for d in range(2, number):
        if number%d == 0:
            return False
    return True


def primes(amount: int):
        x = 0
        cnt = 0

        while cnt<amount:
            while not is_prime(x):
                x+=1
            yield x
            x+=1
            cnt +=1

@time_it
def division(a: int, b: int)->float:

    sleep(2)
    return a/b


print(fib_reccursive.__name__)


