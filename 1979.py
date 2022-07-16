T = int(input())    #test 케이스

for tc in range(1, T+1) :    
    N, K = map(int, input().split())    #  N : 사각형의 갯수, K : 단어의 길이
    data = [list(map(int, input().split())) for _ in range(N)]
    result = 0

# 가로 확인
for i in range(N):
    cnt = 0
    for j in range(N) :
        if data[i][j] == 1 :
            cnt += 1
        if data[i][j] == 0 or j == N-1:
            if cnt == k :
                result += 1
            if data[i][j] == 0:
                cnt = 0
# 세로 확인
for i in range(N) :
    cnt = 0
    if data[j][i] == 1:
        cnt += 1
    if data[j][i] == 0 or j == N-1:
        if cnt == k:
            result += 1
        if data[j][i] == 0:
            cnt = 0
print('#%d, %d', (tc, result))