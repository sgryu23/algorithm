import sys
input = sys.stdin.readline

while True:
    try:
        n = int(input())
        number = 1
        answer = 1

        while True:
            if number % n == 0:
                break
            number = number * 10 + 1
            answer += 1

        print(answer)
    except:
        quit()