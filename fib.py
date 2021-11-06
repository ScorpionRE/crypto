from math import sqrt

def fib_v1(n):
    if n == 0 or n == 1:
        return n
    else:
        print(n)
        return fib_v1(n - 1) + fib_v1(n - 2)


def fib_v2(n):
    if n == 0 or n == 1:
        return n
    else:
        return int(((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5)))


def main():
    result1 = fib_v1(12)
    result2 = fib_v2(12)
    print('Flag is here!')
    print(result1)
    print(result2)
    print("I won't ever tell you")


if __name__ == '__main__':
    main()
