# Write a method called `multiply_by` that takes a list and
# a number, and returns the list of numbers multiplied by that number.
#
# You'll want to apply your fundamental programming knowledge here.
# What are the pieces to this problem? You'll need to define a method,
# need a return statement, need a for loop to iterate over the array.
#
# Example method call:
#
# multiply_by([1, 2, 3], 5)
#
# > [5, 10, 15]

def multiply_by(arr, number):
    my_list = []
    for item in arr:
        # print(item)
        my_list.append(item*number)
    return my_list

print(multiply_by([1,2,3], 4))

def multiply_by2(ls, num):
    # lambda function
    new_list = map(lambda x: num * x, ls)
    return new_list