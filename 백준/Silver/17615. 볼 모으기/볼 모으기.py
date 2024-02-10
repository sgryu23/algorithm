import sys
input = sys.stdin.readline

n = int(input())
balls = str(input().strip())
answer_candidate = []

red_to_right = balls.rstrip('R')
answer_candidate.append(red_to_right.count('R'))

blue_to_right = balls.rstrip('B')
answer_candidate.append(blue_to_right.count('B'))

red_to_left = balls.lstrip('R')
answer_candidate.append(red_to_left.count('R'))

blue_to_left = balls.lstrip('B')
answer_candidate.append(blue_to_left.count('B'))

print(min(answer_candidate))