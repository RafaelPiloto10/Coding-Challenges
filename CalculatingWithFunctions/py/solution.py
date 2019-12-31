def zero(func=None): #your code here
    if func is None: return 0
    return eval(("0" + func))

def one(func=None): #your code here
    if func is None: return 1
    return eval(("1" + func))

def two(func=None): #your code here
    if func is None: return 2
    return eval(("2" + func))

def three(func=None): #your code here
    if func is None: return 3
    return eval(("3" + func))

def four(func=None): #your code here
    if func is None: return 4
    return eval(("4" + func))

def five(func=None): #your code here
    if func is None: return 5
    return eval(("5" + func))

def six(func = None): #your code here
    if func is None: return 6
    return eval(("6" + func))

def seven(func=None): #your code here
    if func is None: return 7
    return eval(("7" + func))

def eight(func=None): #your code here
    if not func: return 8
    return eval(("8" + func))

def nine(func=None): #your code here
    if not func: return 9
    return eval(("9" + func))

def plus(num): #your code here
    return "+" + str(num)
def minus(num): #your code here
    return "-" + str(num)
def times(num): #your code here
    return "*" + str(num)
def divided_by(num): #your code here
    return "//" + str(num)


print('Basic Tests')
print(seven(plus(one())))
print(seven(times(five())), 35)
print(four(plus(nine())), 13)
print(eight(minus(three())), 5)
print(six(divided_by(two())), 3)
