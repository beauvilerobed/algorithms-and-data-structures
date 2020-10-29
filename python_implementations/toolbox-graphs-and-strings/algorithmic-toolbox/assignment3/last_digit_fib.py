

def last_digit_of_fib_naive(n):
    if n <= 1:
        return n
    
    return (last_digit_of_fib_naive(n - 1) + last_digit_of_fib_naive(n - 2)) % 10
    

def last_digit_of_fib(n):
    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n):
        previous, current = current, (current + previous) % 10
    
    return previous


def main():
    input_n = int(input())
    print(last_digit_of_fib(input_n))


if __name__ == '__main__':
    main()