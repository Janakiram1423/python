from itertools import combinations
list = [-2,7,-9,3,9,-5]
print("Positive combinations:")
for r in range(1,len(list)+1):
    for combo in combinations(list,r):
        if all(num>0 for num in combo):
            print(combo)