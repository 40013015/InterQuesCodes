from itertools import permutations
def isprime(n):
  if n == 2 or n == 3:
    return True
  elif n % 2 == 0 or n == 1:
    return False
  for i in range(3,n//2):
    if n % i == 0:
      return False
  return True

def PrimeChecker(num):
  digits = [i for i in str(num)]
  for number in permutations(digits, len(str(num))):
    if isprime(int(''.join(number))):
      return 1
  return 0


print(PrimeChecker(input()))