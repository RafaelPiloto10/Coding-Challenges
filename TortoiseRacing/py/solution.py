import math 

def race(v1, v2, g):
    # your code
    if v1 > v2: return None
    else:
        h = round(g/(v2 - v1), 5)
        m = (h - math.floor(h)) * 60
        s = (m - math.floor(m)) * 60
        m += math.floor(s / 60.0)
        s %= 60
        return [math.floor(h), math.floor(m), math.floor(s)]

print(race(720, 850, 70), [0, 32, 18])
print(race(80, 91, 37), [3, 21, 49])
print(race(80, 100, 40), [2, 0, 0])
