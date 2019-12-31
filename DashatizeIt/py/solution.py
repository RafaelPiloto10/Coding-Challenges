def dashatize(num):
    # get 'em'
    num = num if str(num)[0] != '-' else int(str(num)[1:])
    if num is None: return "None"
    s = "" + str(num)[0] + ("-" if int(str(num)[0]) % 2 != 0 else "")
    if len(str(num)) == 1: return s[:-1] if s[-1] == "-" else s 
    for i in range(1, len(str(num))):
        if int(str(num)[i]) % 2 != 0: s+= ("-" if s[-1] != "-" else "") + str(num)[i] + ("-" if i != len(str(num)) - 1 else "")
        else: s += str(num)[i]
    return s

print('Basic')
print(dashatize(274),"2-7-4", "Should return 2-7-4")
print(dashatize(5311),"5-3-1-1", "Should return 5-3-1-1")
print(dashatize(86320),"86-3-20", "Should return 86-3-20")
print(dashatize(974302),"9-7-4-3-02", "Should return 9-7-4-3-02")
print('Weird')
print(dashatize(None),"None", "Should return None");
print(dashatize(0),"0", "Should return 0");
print(dashatize(-1),"1", "Should return 1");
print(dashatize(-28369),"28-3-6-9", "Should return 28-3-6-9");
