# #  number one
# number = int(input("Please eneter a positive integer.\n\n"))
# for row in range(1, number + 1):
#     output = ''
#     for col in range(1, row + 1):
#         output +='* '
#     print(output)


#  number two

# number = int(input("Please eneter a positive integer.\n\n"))
# for row in range(1, number + 1):
#     output = ''
#     for col in range(1, row + 1):
#         output += str(col) + ' '
#     print(output)

#  number three
# number = int(input("Please eneter a positive integer.\n\n"))
# count = 1
# greatest_int = number * (number+1) // 2
# number_of_characters = len(str(greatest_int))
# for row in range(1, number + 1):
#     output = ''
#     for col in range(1, row + 1):
#         output += '{:>{}}'.format(count, number_of_characters) + ' '
#         count += 1
#     print(output)


#  number four.
#
# number = int(input("Please eneter a positive integer.\n\n"))
# for row in reversed(range(1, number + 1)):
#     output = ''
#     for col in range(1, row + 1):
#         output +='* '
#     print(output)


#number five
# number = int(input("Please eneter a positive integer.\n\n"))
# for row in reversed(range(1, number + 1)):
#     output = ''
#     for col in range(1, row + 1):
#         output += str(col) + ' '
#     print(output)

# number six

number = int(input("Please eneter a positive integer.\n\n"))
count = 1
greatest_int = number * (number+1) // 2
number_of_characters = len(str(greatest_int))
for row in (reversed(range(1, number + 1))):
    output = ''
    for col in range(1, row + 1):
        output += '{:<{}}'.format(count, number_of_characters) + ' '
        count += 1
    print(output)
