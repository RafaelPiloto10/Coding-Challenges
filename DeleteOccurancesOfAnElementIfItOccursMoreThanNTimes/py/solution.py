def delete_nth(order,max_e):
    # code here 
    seen = {}
    new_order = []
    for i in order:
        if str(i) in seen:
            if seen.get(str(i)) != max_e:
                seen[str(i)] += 1
                new_order.append(i)
            else: continue
        else:
            seen[str(i)] = 1
            new_order.append(i)
    print(seen)
    return new_order 


def test(obs, exp):
    print("\nObserved:", obs, "Expected:", exp, "Passed" if obs == exp else "Failed")

test(delete_nth([20,37,20,21], 1), [20,37,21])
test(delete_nth([1,1,3,3,7,2,2,2,2], 3), [1, 1, 3, 3, 7, 2, 2, 2])
