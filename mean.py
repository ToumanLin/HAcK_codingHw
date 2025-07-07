def mean(input):
    sum = 0
    for entry in input:
        sum += entry
    return sum / len(input)

my_list = [1, 2, 3, 4, 5]
print(mean(my_list))