def add_rv(v1, v2):
    set1 = set(v1[1:])
    set2 = set(v2[1:])
    both = set1.union(set2)

    abs1 = set([abs(x) for x in set1])
    abs2 = set([abs(x) for x in set2])

    keep = set1.intersection(set2)
    keep_abs = set([abs(x) for x in list(keep)])

    throw = (abs1.intersection(abs2)).difference(keep_abs)
    nthrow = set([-x for x in list(throw)])
    throw = throw.union(nthrow)

    new = list(both.difference(throw))
    new = sorted(new, key = abs)
    n = [len(new)]
    ans = ""
    
    for num in (n+new):
        num = str(num)
        ans = ans + num + " "

    return ans

def prod_rv(v1, v2):
    set1 = set(v1[1:])
    set2 = set(v2[1:])
    both = set1.union(set2)

    abs1 = set([abs(x) for x in set1])
    abs2 = set([abs(x) for x in set2])

    keep = set1.intersection(set2)
    keep = set([abs(x) for x in list(keep)])

    negatives = (abs1.intersection(abs2)).difference(keep)
    negatives = set([-x for x in list(negatives)])

    new = list(keep.union(negatives))
    new = sorted(new, key = abs)
    n = [len(new)]
    ans = ""
    
    for num in (n+new):
        num = str(num)
        ans = ans + num + " "

    return ans

def rotate(v, k, size):
    new = []
    for x in v[1:]:
        pos = abs(x) - k
        if pos <= 0:
            pos = size + pos
        if x < 0:
            pos = -pos
        new = new + [pos]

    new = sorted(new, key = abs)
    n = [len(new)]
    ans = ""
    
    for num in (n+new):
        num = str(num)
        ans = ans + num + " "
    
    return ans

[size, k]= map(int, input().split())
v1 = input().split()
v1 = [int(x) for x in v1]
v2 = input().split()
v2 = [int(x) for x in v2]
print(add_rv(v1, v2))
print(prod_rv(v1, v2))
print(rotate(v1, k, size))
print(rotate(v2, k, size))