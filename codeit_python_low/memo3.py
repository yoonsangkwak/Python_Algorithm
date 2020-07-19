print('첫번째 수를 입력하시오: ', end='')
number1 = int(input())
print('두번째 수를 입력하시오: ', end='')
number2 = int(input())

try:
    add = number1 + number2
    subtract = number1 - number2
    multiply = number1 * number2
    divide = number1 / number2
except ZeroDivisionError:
    divide = None

print(number1, '+', number2, '=', add)
print(number1, '-', number2, '=', subtract)
print(number1, '*', number2, '=', multiply)
print(number1, '/', number2, '=', divide)