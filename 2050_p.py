from ctypes.wintypes import WORD


WORD = list(input())
for i in range(len(WORD)) :
    print(ord(WORD[i])-64, end='')
