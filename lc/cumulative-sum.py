"""
The cumulative sum of an array at index i is defined as the sum of all elements of the array from index 0 to index i.
Examples

Initial Array: [1, 2, 3, 4]
Cumulative Sum: [1, 3, 6, 10]

Initial Array: [1, 1, 1, 1, 1]
Cumulative Sum: [1, 2, 3, 4, 5]

Initial Array: [1, 3, 5, 7, 9]
Cumulative Sum: [1, 4, 9, 16, 25]

Given an array, return its cumulative sum.
"""

def cumSum(arr):
  answer = []
  s = 0

  for i, el in enumerate(arr):
    s += el
    answer.append(s)

  return answer

def pos_sum(arr):
  answer = []
  s = 0

  for i, el in enumerate(arr):
    s += el
    
    if s > 0:
      answer.append(s)

  return answer  


def main():
  print(cumSum([1, 3, 5, 7, 9]))


if __name__ == '__main__':
  main()