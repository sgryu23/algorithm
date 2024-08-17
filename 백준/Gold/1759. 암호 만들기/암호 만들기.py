import sys
input = sys.stdin.readline


def construct_password(password, idx):
    if len(password) == L:
        vowel = 0
        consonant = 0
        for p in password:
            if p in 'aeiou':
                vowel += 1
            else:
                consonant += 1
        if vowel > 0 and consonant > 1:
            print(password)
        return

    for i in range(idx + 1, C):
        password = password + alphabets[i]
        construct_password(password, i)
        password = password[:-1]


L, C = map(int, input().split())
alphabets = sorted(list(input().split()))

for j in range(C):
    pw = alphabets[j]
    construct_password(pw, j)