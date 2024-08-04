import sys
input = sys.stdin.readline

saved = 0

for i in range(3):
    s = input().rstrip()
    if s == 'Fizz':
        continue
    elif s == 'Buzz':
        continue
    elif s == 'FizzBuzz':
        continue
    else:
        s = int(s)
        saved = s + (3 - i)

if saved % 3 == 0 and saved % 5 == 0:
    print('FizzBuzz')
elif saved % 3 == 0:
    print('Fizz')
elif saved % 5 == 0:
    print('Buzz')
else:
    print(saved)