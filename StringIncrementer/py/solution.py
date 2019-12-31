def increment_string(strng):
    if len(strng) == 0: return '1'
    if not strng[-1].isdigit(): return strng + '1'
    strIndex = len(strng)
    if strIndex == 1: return str(int(strng) + 1)
    for i in range(len(strng) - 1, 0, -1):
        if not strng[i].isdigit():
            break
        strIndex -= 1

    num = int(strng[strIndex if not strng.isdigit() else 0:]) + 1
    adj = len(strng[strIndex if not strng.isdigit() else 0:]) - len(str(num))
    strng = strng[:strIndex + (adj if adj > 0 else 0)] + str(num)
    return strng


print(increment_string("foo"), "foo1")
print(increment_string("foobar001"), "foobar002")
print(increment_string("foobar1"), "foobar2")
print(increment_string("foobar00"), "foobar01")
print(increment_string("foobar99"), "foobar100")
print(increment_string("foobar099"), "foobar100")
print(increment_string(""), "1")
