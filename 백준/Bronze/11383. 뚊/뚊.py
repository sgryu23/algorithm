import sys
input = sys.stdin.readline

n, m = map(int, input().split())
first_image = []
is_same_image = []
second_image = []

for i in range(n):
    first_image.append(list(input().rstrip()))
    is_same_image.append([])
    for element in first_image[i]:
        for double in range(2):
            is_same_image[i].append(element)

for j in range(n):
    second_image.append(list(input().rstrip()))
    if second_image[j] != is_same_image[j]:
        print('Not Eyfa')
        quit()

print('Eyfa')