'''
DOCSTRING : Given two int values, return their sum. Unless the two values are the same,
            then return double their sum.

INPUT : Integer values

'''
def sum_double(a,b):
  '''
  sum_double(1, 2) → 3
  sum_double(3, 2) → 5
  sum_double(2, 2) → 8
  '''
    #a = int(input("Enter first number: "))
    #b = int(input("Enter second number: "))
    if a == b:
        return (a+b)*2
    else:
        return a+b