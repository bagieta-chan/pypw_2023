s = {4,10,2,3}



def fib_sequence(n: int)->int :
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


for prime in primes(20):
    print(prime)




