num1 = 42 # variable declaration - type: number (int)
num2 = 2.3  # variable declaration - type: number (float)
boolean = True  # variable declaration - type: boolean
string = 'Hello World'  # variable declaration - type: string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 
        'Cheese', 'Olives'] # variable declaration - type: list
person = {'name': 'John', 'location': 'Salt Lake',
        'age': 37, 'is_balding': False}  # variable declaration - type: dictionary
fruit = ('blueberry', 'strawberry', 'banana')  # variable declaration - type: tuple
print(type(fruit))  # log statement - type check
print(pizza_toppings[1])  # log statement
pizza_toppings.append('Mushrooms') # list - add value
print(person['name'])  # log statement
person['name'] = 'George' # dictionary - change value
person['eye_color'] = 'blue' # dictionary - add value
print(fruit[2])  # log statement

if num1 > 45:  # conditional
    print("It's greater")  # log statement
else:
    print("It's lower")  # log statement

if len(string) < 5:  # conditional if + length check
    print("It's a short word!")  # log statement
elif len(string) > 15:  # conditional elif + length check
    print("It's a long word!")  # log statement
else:  # conditional else
    print("Just right!")  # log statement

for x in range(5):  # for loop
    print(x)  # log statement
for x in range(2, 5):  # for loop
    print(x)  # log statement
for x in range(2, 10, 3):  # for loop
    print(x)  # log statement
x = 0 # variable declaration
while (x < 5):  # while loop
    print(x)  # log statement
    x += 1 # while loop - increment

pizza_toppings.pop() # list - remove value
pizza_toppings.pop(1) # list - remove value @ index 1

print(person)  # log statement
person.pop('eye_color') # dictionary - remove value
print(person)  # log statement

for topping in pizza_toppings:
    if topping == 'Pepperoni':  # conditional if
        continue # for loop - continue
    print('After 1st if statement')  # log statement
    if topping == 'Olives':  # conditional if
        break # for loop - break


def print_hello_ten_times(): # function
    for num in range(10):  # for loop
        print('Hello')  # log statement


print_hello_ten_times() # function


def print_hello_x_times(x): # function (parameter: x)
    for num in range(x):  # for loop
        print('Hello')  # log statement


print_hello_x_times(4) # function


def print_hello_x_or_ten_times(x=10): # function
    for num in range(x): # for loop
        print('Hello')  # log statement


print_hello_x_or_ten_times()  # function
print_hello_x_or_ten_times(4)  # function


"""
Bonus section
"""

# print(num3) # NameError
# num3 = 72 # no error
# fruit[0] = 'cranberry' # Tuple value cannot be changed
# print(person['favorite_team']) # AttributeError: 'dictionary' object has no attribute 'favorite_team'
# print(pizza_toppings[7]) # IndexError
#   print(boolean) # IndentationError
# fruit.append('raspberry') # Tuple value cannot be changed
# fruit.pop(1) # Tuple value cannot be changed
