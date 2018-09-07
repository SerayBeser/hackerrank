# Enter your code here. Read input from STDIN. Print output to STDOUT

size = int(raw_input())
numbers = list(map(int, raw_input().split()))
sorted_list = numbers
sorted_list.sort()

mean = sum(numbers) / float(size)

if size % 2 == 0:
    median = float(sorted_list[size / 2 - 1] + sorted_list[size / 2]) / 2
else:
    median = sorted_list[(size - 1) / 2]

m = max([numbers.count(a) for a in numbers])
mode = [x for x in numbers if numbers.count(x) == m][0] if m > 1 else sorted_list[0]

print(mean)
print(median)
print(mode)
