import math

def list_squared(m, n):
    # your code
    solutions = []
    for i in range(m, n):
        div = getDivisors(i)
        div_sum = sum([j ** 2 for j in div])
        if math.sqrt(div_sum) % 1 == 0:
            solutions.append([i, div_sum])
    return solutions

def getDivisors(n):
    div = []
    for i in range(1, n + 1):
        if n % i == 0: div.append(i)
    return div

def test(observed, expected):
    print("Results:", observed == expected, "\nObserved:", observed, "\nExpected:", expected)

test(list_squared(1, 250), [[1, 1], [42, 2500], [246, 84100]])
test(list_squared(42, 250), [[42, 2500], [246, 84100]])
test(list_squared(250, 500), [[287, 84100]])

