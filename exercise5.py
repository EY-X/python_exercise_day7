# Exercise 1

# def double(my_number):
#     return my_number * 2

# Exercise 2
# def negative(numba):
#     if numba > 0:
#         return True
#     else:
#         return False


# print(negative(-7))
# print(negative(8))

# Exercise 3
# def is_even(numba):
#     if numba % 2 == 1:
#         return False
#     else:
#         return True


# print(is_even(5))

# Exercise 4
# def count_letters(s):
#     if len(s) >= 8:
#         return True
#     else: 
#         return False


# print(count_letters('hello'))

Exercise 5

temp = input("Enter Temp\n")
temp = int()


def conversion(f):
    c = (f - 32) * (5/9)
    c = int(c) #converting str --> int
    return c

print('the conversion is {}'.format(conversion)) #calling function

