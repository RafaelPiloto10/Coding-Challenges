# Too hard, I have no idea.. wtf..

def decompose(n):
    # your code
    sq = n ** 2
    sqs = []
    for i in range(n - 1, 1, -1):
        if(sum(sqs) + i**2 <= sq):
            sqs.append(i)



print(decompose(5) == [3,4])
print(decompose(8) == None)


