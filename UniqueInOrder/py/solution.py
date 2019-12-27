def unique_in_order(iterable):
    if len(iterable) == 0: return [] 
    unique = [iterable[0]]
    for i in range(1, len(iterable)):
        if unique[len(unique) - 1] == iterable[i]:
            continue
        else: unique.append(iterable[i])
    return unique

print(unique_in_order('AAAABBBCCDAABBB') == ['A','B','C','D','A','B'])


