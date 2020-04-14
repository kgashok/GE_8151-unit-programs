def selectsort(lst):
  '''implements the selection sort

  @param lst unsorted list of numbers 
  @returns sorted list of numbers
  
  >>> selectsort([6, 4, 7, 8, 5, 1, 2, 3])
  inter [1, 4, 7, 8, 5, 6, 2, 3]
  inter [1, 2, 7, 8, 5, 6, 4, 3]
  inter [1, 2, 3, 8, 5, 6, 4, 7]
  inter [1, 2, 3, 4, 5, 6, 8, 7]
  inter [1, 2, 3, 4, 5, 6, 8, 7]
  inter [1, 2, 3, 4, 5, 6, 8, 7]
  inter [1, 2, 3, 4, 5, 6, 7, 8]
  [1, 2, 3, 4, 5, 6, 7, 8]
  '''
  def index_of_minimum(i):
    '''return the index of the minimum value
    in the subarray lst[i:]

    @param i index from where the sublist starts
    @returns the index of the minimum value 
    '''
    return lst.index(min(lst[i:]), i)
  def swap(x, y):
    '''swaps list elements at index x and y
    
    @param x an index value 
    @param y an index value 
    '''
    if x != y: 
      lst[x], lst[y] = lst[y], lst[x]

  # Step 0 iterate from 0 to n-1
  for i in range(0, len(lst)-1):
    # Step 1 select a minimum 
    mdx = index_of_minimum(i)
    # Step 2 swap if required 
    swap(i, mdx)
    print("inter", lst)
  return lst

# doctstring testing
from doctest import testmod
testmod(name="selectsort", verbose=True)

# driver program
from random import shuffle
lst = list(range(1, 9))
shuffle(lst)
print(selectsort(lst))