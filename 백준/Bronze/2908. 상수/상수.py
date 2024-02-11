input1, input2 = input().split()
num1 = int(input1[2]) * 100 + int(input1[1]) * 10 + int(input1[0])
num2 = int(input2[2]) * 100 + int(input2[1]) * 10 + int(input2[0])
print(max(num1, num2))