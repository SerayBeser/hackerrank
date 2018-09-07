# Enter your code here. Read input from STDIN. Print output to STDOUT

size = int(raw_input())
elements = map(int, raw_input().split())
freqs = map(int, raw_input().split())

numbers = list()
a = 0
for j in freqs:
    for i in range(0, j):
        numbers.append(elements[a])
    a += 1
numbers.sort()

size = len(numbers)
if size % 2 == 0:
    median_q2 = float(numbers[size / 2 - 1] + numbers[size / 2]) / 2
    lower_half = numbers[:size / 2]
    upper_half = numbers[size / 2:]
else:
    median_q2 = numbers[(size - 1) / 2]
    lower_half = numbers[:(size - 1) / 2]
    upper_half = numbers[(size - 1) / 2 + 1:]

size = len(lower_half)
if size % 2 == 0:
    median_q1 = float(lower_half[size / 2 - 1] + lower_half[size / 2]) / 2
else:
    median_q1 = lower_half[(size - 1) / 2]

size = len(upper_half)
if size % 2 == 0:
    median_q3 = float(upper_half[size / 2 - 1] + upper_half[size / 2]) / 2
else:
    median_q3 = upper_half[(size - 1) / 2]

print float(median_q3 - median_q1)
