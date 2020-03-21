[n, s] = map(int, input().split())
arr = []

for i in range(0,n):
    row =   input()
    arr.append(row)
#print(arr)
#print(arr[0][0])

ddict = dict()
# for every rug placement with left corner at (i,j):
for i in range(n-s+1):
    for j in range(n-s+1):
        d_covered = 0
        # for every spot covered by rug:
        for x in range(i, i+s):
            for y in range(j, j+s):
                if arr[x][y] == "D":
                    d_covered += 1
        if d_covered in ddict:
            ddict[d_covered] += 1
        else:
            ddict[d_covered] = 1

#print(ddict)
output = []
for key in ddict:
    output.append([key, ddict[key]])
output.sort()
#print(output)

for i in output:
    print(str(i[0]) + " " + str(i[1]))
