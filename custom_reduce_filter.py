
"""
Problem Statement​ ​1:
Write a Python Program to implement your own myreduce() function which works exactly
like Python's built-in function reduce()
Problem Statement​ ​2:
Write a Python program to implement your own myfilter() function which works exactly
like Python's built-in function filter()

"""

# Reduce will produce a single result
def myreduce(anyfunc, sequence):

 # Get first item in sequence and assign to result
  result = sequence[0]
 # iterate over remaining items in sequence and apply reduction function 
  for item in sequence[1:]:
   result = anyfunc(result, item)

  return result


# Custom filter function 
def myfilter(anyfunc, sequence):

 # Initialize empty list