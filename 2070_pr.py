T = int(input())

for test_case in range(1, T+1) :
    A, B = map(int, input().split())
    if A > B :
        print(">")
    elif A < B :
        print("<")
    elif A == B :
        print("=")