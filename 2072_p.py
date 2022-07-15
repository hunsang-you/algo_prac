T = int(input())
 
for test_case in range(1,T+1):
    num = map(int, input().split())
    ans = 0
    for i in num:
        if i%2!=0:
            ans += i
    print("#"+str(test_case),str(ans))