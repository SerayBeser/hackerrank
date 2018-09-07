# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
size = int(raw_input())
numbers = map(int, raw_input().split())

mean = sum(numbers) / float(size)
total = 0
for i in numbers:
    total += (i - mean) * (i - mean)

std = math.sqrt(total / size)
print round(std,1)
