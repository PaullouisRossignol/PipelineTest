# from math import *
Rep = 0

# function that sum all numbers passed (or add to the result of last operation if only one numb passsed)
def add(*numbers):
    global Rep
    sum = 0
    #if only one numb passed => divide the result from last operation
    if len(numbers) == 1:
        sum = Rep + numbers[0]
    #if only one numb passed => add to the result of last operation
    else:
        for x in numbers:
            sum += x
    Rep = sum
    return sum
# function that substract all numbers passed (or subs to the result of last operation if only one numb passsed)
def subs(*numbers):
    global Rep
    sum = 0
    #if only one numb passed => divide the result from last operation
    if len(numbers) == 1:
        sum = Rep - numbers[0]
    #if only one numb passed => subs from the result of last operation
    else:
        for x in numbers:
            sum -= x
    Rep = sum
    return sum
# function that divide the first numb passed by the others (or divide the result from last operation if only one numb passsed)
def div(*numbers):
    global Rep
    res = float(0.0)
    divide = False

    #check if there is no 0 in the divisers tuples
    for x in numbers:
        if x == 0:
            raise ZeroDivisionError
    #if only one numb passed => divide the result from last operation
    if len(numbers) == 1:
        res = Rep / numbers[0]
    #else, we divide the first numb passed by the others
    else:
        for x in numbers:
            if divide:
                res = float(res) / x
            else:
                divide = True
                res = numbers[0]
    Rep = res
    return res
# function that multiply the first numb passed by the others (or multiply the result from last operation if only one numb passsed)
def mul(*numbers):
    global Rep
    res = float(0.0)
    multiply = False

    #if only one numb passed => multiply the result from last operation
    if len(numbers) == 1:
        res = Rep * numbers[0]

    #else, we multiply the first numb passed by the others
    else:
        for x in numbers:
            if multiply:
                res = float(res) * x
            else:
                multiply = True
                res = numbers[0]
    Rep = res
    return res

if __name__ == "__main__":

    mul(1, 2, 3, 2, 2, 3)
    print(Rep)
    div(2)
    print(Rep)



