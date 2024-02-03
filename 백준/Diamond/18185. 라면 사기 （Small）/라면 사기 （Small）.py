import sys
input = sys.stdin.readline

n = int(input())
factories = list(map(int, input().split())) + [0, 0]
cost = 0

for i in range(n):
    if factories[i + 1] > factories[i + 2]:
        min_value = min(factories[i], factories[i + 1] - factories[i + 2])
        factories[i] -= min_value
        factories[i + 1] -= min_value
        cost += 5 * min_value

        in_case_buy_three = min(factories[i:i + 3])
        factories[i] -= in_case_buy_three
        factories[i + 1] -= in_case_buy_three
        factories[i + 2] -= in_case_buy_three
        cost += 7 * in_case_buy_three

        cost += 3 * factories[i]

    else:
        in_case_buy_three = min(factories[i:i + 3])
        factories[i] -= in_case_buy_three
        factories[i + 1] -= in_case_buy_three
        factories[i + 2] -= in_case_buy_three
        cost += 7 * in_case_buy_three

        in_case_buy_two = min(factories[i:i + 2])
        factories[i] -= in_case_buy_two
        factories[i + 1] -= in_case_buy_two
        cost += 5 * in_case_buy_two

        cost += 3 * factories[i]

print(cost)