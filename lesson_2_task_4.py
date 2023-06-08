def fizzBuzz(n):
  for n in range(1,n):
    if n % 3 == 0 and n % 5 == 0:
     print("FizzBuzz")
    elif n % 3 == 0:
     print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print (n)

fizzBuzz (6)

