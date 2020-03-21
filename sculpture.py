
def higher(x, y):
    if x > y:
        return 1
    else:
        return 0


[r, c] =map(int, input().split())
arr = []

for i in range(0,r):
    row =  map(int, input().split())
    row = list(row)
    arr.append(row)

output = []
for i in range(r):
    output.append([0]*c)

for i in range(1, r-1):
    for j in range(1, c-1):
        
        output[i][j] = ((
        higher(arr[i-1][j], arr[i][j]) + 
        higher(arr[i+1][j], arr[i][j]) + 
        higher(arr[i][j-1], arr[i][j]) + 
        higher(arr[i][j+1], arr[i][j])
        )
        //4)
         
for i in range(r):
    for j in range(c):
        print(str(output[i][j]) + " ", end = '')
    print("")

