T = int(input())

for test_case in range(1, T+1) :
    sum = 0
    num = list(map(int, input().split()))
    for i in num:
        sum += i
    print("#{} {}".format(test_case, round(sum/len(num))))