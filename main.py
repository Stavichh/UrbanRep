
def print_params(a = 1, b = "первый", c = True):
    print("параметры следующие - ", a, b, c)


print_params()
print_params(2, 3, 8)
print_params(4, 15)
print_params("new", b = "old", c = None)

print_params(b = 25)
print_params(c = [1,2,3])


value_list = [125, "bold", False]
value_dict = {"a":5, "b":"последний", "c":False}

print_params(*value_list)
print_params(**value_dict)