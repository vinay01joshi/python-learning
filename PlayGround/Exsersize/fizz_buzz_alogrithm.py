# if the input id divisible by 3
# return string "Fizz"
# if the input is divisible by 5
# return "Buzz"
# if the input is divisible by both  3 and 5
# return FizzBuzz
# elese return the number same it as


def fizz_buzz(number):
    if(number % 3 == 0 and number % 5 == 0):
        return "FizzBuzz"
    elif(number % 3 == 0):
        return "Fizz"
    elif(number % 5 == 0):
        return "Buzz"
    else:
        return number


print(fizz_buzz(5))
