# 1. Update Values in Dictionaries and Lists
x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

x[1][0] = 15
students[0]["last_name"] = "Bryant"
sports_directory["soccer"][0] = "Andres"
z[0]["y"]=30


# 2. Iterate Through a List of Dictionaries
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

def iterateDictionary(list): 
    for dict in list:
        result = ""
        for key in dict:
            result += key + " - " + dict[key]
            if (key == "first_name"):
                result += ", "
        print(result)

iterateDictionary(students)
print()


# 3. Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for dict in some_list:
        print(dict[key_name])

iterateDictionary2('last_name', students)
print()


# 4. Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo): 
    for each_key in dojo:
        print(len(dojo[each_key]), each_key)
        for i in range(0, len(dojo[each_key])):
            print(dojo[each_key][i])
        print()

printInfo(dojo)