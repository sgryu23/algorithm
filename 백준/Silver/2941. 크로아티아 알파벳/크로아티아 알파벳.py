import sys

Croatian_alphabets = ['c-', 'c=', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

input_alphabet = sys.stdin.readline().rstrip()

for alpha in Croatian_alphabets:
    if alpha in Croatian_alphabets:
        input_alphabet = input_alphabet.replace(alpha, 'A')

answer = len(input_alphabet)

print(answer)