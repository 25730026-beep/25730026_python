first = int(input())
second = int(input())
third = int(input())
largest = first
if second > largest:
    largest = second
if third > largest:
    largest = third
print(largest)
