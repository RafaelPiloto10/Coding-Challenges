def productFib(prod):
    # your code    
    seq = [0, 1]
    c_prod = 0
    n = 0
    while(c_prod < prod):
        seq.append(seq[n] + seq[n + 1])
        n += 1
        c_prod = seq[n] * seq[n + 1]
    if c_prod == prod: return [seq[n], seq[n + 1], True]
    else: return [seq[n], seq[n + 1], False]

print(productFib(4895), [55, 89, True])
print(productFib(5895), [89, 144, False])

