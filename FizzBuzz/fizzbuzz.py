def fizz_buzz(number):
    """
    FizzBuzz test return 'Fizz', 'Buzz', 'FizzBuzz' if 
    number input is divisible by 3, 5, or both respectively
    The number is returned if it's not divisible by both 3 and
    5
  """

    if number % 15 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return number
