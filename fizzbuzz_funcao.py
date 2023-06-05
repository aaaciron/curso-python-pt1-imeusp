def fizz(n):
    if n % 3 == 0:
        return True
    else:
        return False
def buzz(n):
    if n % 5 == 0:
        return True
    else:
        return False
def fizzbuzz(n):
    if fizz(n) and buzz(n):
        return "FizzBuzz"
    if not fizz(n) and not buzz(n):
        return n
    if fizz(n) and not buzz(n):
        return "Fizz"
    if not fizz(n) and buzz(n):
        return "Buzz"
