# input values from user
value_1 = input("Enter your first value")
value_2 = input("Enter your second value")
operator = input("Enter the operator")
# validate inputs
valid_values = True
valid_operator = True
if value_1.isdigit() and value_2.isdigit():
    value_1 = int(value_1)
    value_2 = int(value_2)
else:
    valid_values = False
    print("Your values are not integers")
if operator not in '+-/*':
    valid_operator = False
    print("The operator is False")
# Calculate
if valid_operator and valid_values == True:
    if operator == '+':
        print("%d + %d = " % (value_1, value_2), value_1 + value_2)
    if operator == '-':
        print("%d - %d = " % (value_1, value_2), value_1 - value_2)
    if operator == '*':
        print("%d * %d = " % (value_1, value_2), value_1 * value_2)
    if operator == '/':
        print("%d / %d = " % (value_1, value_2), value_1 / value_2)