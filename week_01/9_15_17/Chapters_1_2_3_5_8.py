# Catching exceptions using try and except
#inp = input('Enter Fahrenheit Temperature: ')
#try:
 #   fahr = float(inp)
  #  cel = (fahr - 32.0) * 5.0 / 9.0
   # print(cel)
#except:
 #   print("please enter a digit")

# guardian pattern
# x = 6
# y = 2
# print(x >= 2 and (x/y) > 2)
# # gives a False becuase python stops executing after the first statement fails.
# x = 1
# y = 0
# print(x >= 2 and (x/y) > 2)
# # Gives you a runtime error because you divide by zero
# # x = 6
# #y = 0
# #print(x >= 2 and (x/y) > 2)
# # no runtime error because we put an extra statement to ensure x/y is not executed if y = 0, y != 0 acts as a guard
# x = 6
# y = 0
# print(x >= 2 and y != 0 and (x/y) > 2)

# chapter 5
# the while statement
#n = 10
## while n >= 0:
 #   print(n)
  #  n = n - 1
#print("blast off!")

# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)
# print('Done!')
#
# while True:
#     line = input('> ')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print('Done!')


# friends = ['Joseph', 'Glenn', 'Sally']
# for friend in friends:
#     print('Happy New Year:', friend)
# print('Done!')

# Chapter 8, traversing a list

# cheeses = ['Cheddar', 'Edam', 'Gouda', '1']
# # for cheese in cheeses:
# #     print(cheese)
# i = []
# print(range(len(cheeses)))
# for i in range(len(cheeses)):
#     cheeses[i] = cheeses[i] * 2
# print(i)

# total = 0
# count = 0
# while (True):
#     inp = input('Enter a number: ')
#     if inp == 'done': break
#     value = float(inp)
#     total = total + value
#     count = count + 1
#
# average = total / count
# print('Average:', average)

# numlist = list()
# while (True):
#     inp = input('Enter a number: ')
#     if inp == 'done': break
#     value = float(inp)
#     numlist.append(value)
#
# average = sum(numlist) / len(numlist)
# print('Average:', average)

#exerxise 1
# Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None.
#
# Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.


# def chop(t):
#      del t[0]
#      del t[len(t)-1]
#      return t
#
# list_test = [1,2,3,4,5,6,7,8,9]
# print('starting list', list_test)
# chop(list_test)
# print('starting list', list_test)
#
#
# def middle(t):
#     new_list = t[1:(len(t)-1)]
#     return new_list
#
# list_test = [1,2,3,4,5,6,7,8,9]
# print('starting list', list_test)
# new_list = middle(list_test)
# print('starting list', list_test)
# print('output   list', new_list)

word_1 = "Hello"
word_2 = "were"

word_3 = word_1[-2:] + word_2[0:3]
print(word_3)
