
def sum(a, b):
    return a + b



def mult(a, b):
    return a * b



def list_numbers(n):
    numbers = []
    for num in range(1, n):
        numbers.append(num)
    return numbers


if __name__ == '__main__':
    print(sum(2, 4))
    print(mult(3, 5))
    print(list_numbers(10))


