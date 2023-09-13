# definitions of functions
def subtraction(num1, num2):
    return num1 - num2

def addition(num1, num2):
    return num1 + num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        print('Error: division by zero! :(')
    else:
        return num1 / num2

def main():
    task = input('Enter your expression:')
    task = task.split(" ")
    num1, num2 = float(task[0]), float(task[2])
    mode = task[1]
    return operations[mode](num1, num2)


# dictionary with functions names
operations = {'/': division,
              '-': subtraction,
              '+': addition,
              '*': multiplication
              }
# start calculations
result = main()
print(result)
