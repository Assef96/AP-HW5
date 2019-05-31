from numpy import pi as piNumber
from random import uniform

def IsInCircle(x, y):
    return x*x + y*y <= 0.25

def find():
    N = 0
    M = 0
    abs_error = 1.0
    max_error = 0.01
    while abs_error > max_error:
        x = uniform(-0.5, 0.5)
        y = uniform(-0.5, 0.5)
        N += 1
        if IsInCircle(x, y):
            M += 1
        result = 4 * M / N
        abs_error = abs(result - piNumber)

    return (result, M + N, abs_error)

if __name__ == '__main__':
    repeat = 1
    try:
        repeat = int(input('How many time do you want to repeat the algotithm?'))
    except ValueError:
        print('Error: Not a number!')
    sum = 0.0
    for i in range(repeat):
        (pi, counter, abs_error) = find()
        sum += pi
        print(f'pi={pi:.5f} \t conter={counter} \t abs_error={abs_error:.5f}')
    calculated_pi = sum / repeat
    print(f'\naverage pi = {calculated_pi:.5f}')