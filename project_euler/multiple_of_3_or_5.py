#project euler 1
numbers = range(1000)
filter_numbers = filter(lambda x: x % 3 == 0 or x % 5 == 0, numbers)
result = sum(filter_numbers)
print(result)