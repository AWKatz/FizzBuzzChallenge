# This is Day 5 of 100 for the Udemy Python Bootcamp

# Any number divisible by 3 will be replaced by "Fizz"
# Any number divisible by 5 will be replaced by "Buzz"
# Any number divisible by 3 and 5 will be replaced by "FizzBuzz"

#FizzBuzz
total = 0
for number in range(1, 101):
    total = number

    if total % 3 == 0 and total % 5 == 0:
        total = "FizzBuzz"

    elif total % 3 == 0:
        total = "Fizz"

    elif total % 5 == 0:
        total = "Buzz"

    print(total)
