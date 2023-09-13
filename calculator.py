# input for calculation
task = input()
task = task.split(" ")


# definition of functions
def main(task):
    num1, num2 = float(task[0]), float(task[2])
    mode = task[1]
    if mode == '+':
        return addition(num1, num2)
    elif mode == '-':
        return substraction(num1, num2)
    elif mode == '*':
        return multiplication(num1, num2)
    elif mode == '/':
        return division(num1, num2)

def division(num1, num2):
    if num2 == 0:
        print("Error: can't divide by zero! :(")
    else:
        return num1 / num2


result = main(task)
print(result)


