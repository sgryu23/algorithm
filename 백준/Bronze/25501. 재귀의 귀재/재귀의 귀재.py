import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def is_palindrome(idx, recursion):
    if string[idx] == string[len(string) - 1 - idx]:
        if len(string) // 2 == idx:
            print(1, recursion)
            return
        else:
            is_palindrome(idx + 1, recursion + 1)
            return
    else:
        print(0, recursion)
        return


T = int(input())

for _ in range(T):
    string = list(input().rstrip())
    is_palindrome(0, 1)