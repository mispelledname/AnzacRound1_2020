
[n, s] = input().split()
times = input().split()
n= int(n)
s= int(s)

max = 0
for i in range(len(times)):
    if int(times[i]) > max:
        max = int(times[i])


final1 = max*s/1000.00
final2 = round(final1)
if final1 > final2:
    print(final2+1)
else: 
    print(final2)