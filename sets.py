s = {4,10,2,3}



def fib_sequence(n: int)->int :
    if n in [0,1]:
        return n
    a, b = 0,1
    for i in range(n):
        a, b = b, a+b
    return a

bruh = (fib_sequence(i) for i in range(20))


for i in range (20):
    print(f"number nr: {i}, value: {next(bruh)}")




