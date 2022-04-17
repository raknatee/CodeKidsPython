# import my_code

# print(my_code.number)
# my_code.add(5)

# #################################################

# from my_code import number, add

# print(number)
# add(20)

# #################################################



from other_code import code_a

code_a.say_hello("CodeKids")
print(code_a.a)

#################################################

from other_code.code_a import say_hello

say_hello("CodeKids")