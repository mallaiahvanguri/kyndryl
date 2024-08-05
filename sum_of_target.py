
from itertools import combinations

def sumoftarget(lst, target):
    res = []
    # Use a set to track combinations we've already seen
    seen = set()
    
    for r in range(1, len(lst) + 1):
        for com in combinations(lst, r):
            if sum(com) == target:
                # Sort the combination and add it to the set to avoid duplicates
                sorted_com = tuple(sorted(com))
                if sorted_com not in seen:
                    seen.add(sorted_com)
                    res.append(sorted_com)
                    
    return res

lst = [1, 2, 2, 3, 4, 5]
target = 7
res = sumoftarget(lst, target)

print(res)

