import sys

angles = []
angles_sum = 0
answer = 'Equilateral'

for _ in range(3):
    angle = int(sys.stdin.readline().rstrip())
    angles_sum += angle
    angles.append(angle)
    if angle != 60:
        answer = None

angles.sort()

if angles_sum == 180:
    if answer != 'Equilateral':
        if angles[0] == angles[1] or angles[1] == angles[2]:
            answer = 'Isosceles'
        else:
            answer = 'Scalene'
else:
    answer = 'Error'

print(answer)
