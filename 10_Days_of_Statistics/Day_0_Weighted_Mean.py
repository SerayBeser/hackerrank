# Enter your code here. Read input from STDIN. Print output to STDOUT

size = int(raw_input())
numbers = map(float, raw_input().split())
weigted = map(float, raw_input().split())

total = 0
for i in range(0, size):
    total += numbers[i] * weigted[i]

print (round(total / float(sum(weigted)), 1))
