def isOperator(input):
    switch = {
        '+': 1,
        '-': 1,
        '*': 1,
        '/': 1,
        '%': 1,
        '(': 1,
    }
    return switch.get(input, False)
# To check if the input character is an operand
def isOperand(input):
    if ((ord(input) >= 65 and ord(input) <= 90) or
            (ord(input) >= 97 and ord(input) <= 122)):
        return 1
    return 0
# Function to return precedence value
# if operator is present in stack
def inPrec(input):
    switch = {
        '+': 2,
        '-': 2,
        '*': 4,
        '/': 4,
        '%': 4,
        '(': 0,
    }
    return switch.get(input, 0)
# Function to return precedence value
# if operator is present outside stack.
def outPrec(input):
    switch = {
        '+': 1,
        '-': 1,
        '*': 3,
        '/': 3,
        '%': 3,
        '(': 100,
    }
    return switch.get(input, 0)
# Function to convert infix to postfix
def inToPost(input):
    i = 0
    s = []
    # While input is not NULL iterate
    while (len(input) != i):
        # If character an operand
        if (isOperand(input[i]) == 1):
            print(input[i], end="")
        # If input is an operator, push
        elif (isOperator(input[i]) == 1):
            if (len(s) == 0 or
                outPrec(input[i]) >
                    inPrec(s[-1])):
                s.append(input[i])
            else:
                while (len(s) > 0 and
                       outPrec(input[i]) <
                       inPrec(s[-1])):
                    print(s[-1], end="")
                    s.pop()
                s.append(input[i])
        # Condition for opening bracket
        elif (input[i] == ')'):
            while (s[-1] != '('):
                print(s[-1], end="")
                s.pop()
                # If opening bracket not present
                if (len(s) == 0):
                    print('Wrong input')
                    exit(1)
            # pop the opening bracket.
            s.pop()
        i += 1
    # pop the remaining operators
    while (len(s) > 0):

        if (s[-1] == '('):

            print('Wrong input')

            exit(1)

        print(s[-1], end="")

        s.pop()
input = input()
inToPost(input)
