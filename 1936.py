A, B = map(int, input().split())

if A == 1 :         # A가 가위
    if B == 2 :     # B가 바위
        print('B')
    elif B == 3 :   # B가 보
        print('A')

if A == 2 :         # A가 바위
    if B == 1 :     # B가 가위
        print('A')
    elif B == 3 :   # B가 보
        print('B')

if A == 3 :         # A가 보
    if B == 1 :     # B가 가위
        print('B')
    elif B == 2 :   # B가 바위
        print('A') 