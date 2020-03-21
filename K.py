def max_truth(pairs, n):
    
    for i in range(n, 0, -1):
        count = 0
        for j in range(len(pairs)):
            if pairs[j][0] <= i <= pairs[j][1]:
                count += 1
        if i == count:
            return i

    return -1

n = int(input())
pairs = []
for i in range(n):
    curr = input().split()
    curr = [int(x) for x in curr]
    pairs = pairs + [curr]
print(max_truth(pairs, n))