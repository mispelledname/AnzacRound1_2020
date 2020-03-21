

num_correct = int(input())
my_ans = input()
them_ans = input()

num_same = 0
num_diff = 0
num_q = len(my_ans)
for i in range(num_q):
    if my_ans[i] == them_ans[i]:
        num_same+=1
    else:
        num_diff+=1

if (num_same >= num_correct):
    print(num_correct + num_diff)
elif num_same < num_correct:
    print(num_diff-num_correct+2*num_same)




