def likes(names):
    #your code here
    if len(names) == 0: return 'no one likes this' 
    if len(names) == 1: return names[0] + ' likes this'
    if len(names) == 2: return names[0] + ' and ' + names[1] + ' like this'
    if len(names) == 3: return names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'
    if len(names) > 3: return names [0] + ', ' + names[1] + ' and ' + str(len(names) - 2) + ' others like this'

print(likes([]), 'no one likes this')
print(likes(['Peter']), 'Peter likes this')
print(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
print(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
print(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')
