def is_even(n):
  """
  returns true if the number is even,false otherwise
  """
return n % 2 == 0

def multiply_list(numbers):
  """ 
  multiplies all numbers in a list and returns the result.
  """
  result = 1
  for num in numbers:
    result *= num
  return result
