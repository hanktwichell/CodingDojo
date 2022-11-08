# 1. Countdown
def countdown(num): 
    while num>=0:
        print(num)
        num-=1
# countdown(5)

# 2. Print & Return
def print_and_return(list):
    print(list[0])
    return list[1]
# print(print_and_return(['print', 'return']))

# 3. First Plus Length
def first_plus_length(list):
    return list[0] + len(list)
# print(first_plus_length([1, 2, 3, 4, 5]))

# 4. Values Greater than Second
def values_greater_than_second(list):
    result = []
    if (len(list) < 2):
        return False
    for x in list:
        if (x>list[1]):
            result.append(x)
    print(len(result))
    return result
# print(values_greater_than_second([5, 2, 3, 2, 1, 4]))
# print(values_greater_than_second([3]))

# 5. This Length, That Value
def length_and_value(size, value):
    result = []
    for x in range(size):
        result.append(value)
    return result
# print(length_and_value(4,7))
# print(length_and_value(6,2))