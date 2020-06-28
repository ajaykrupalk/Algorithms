'''Program to demonstrate Bubble Sort'''
def bsort(array):
  for i in range(len(array)):
    for j in range(len(array)-1):
      if array[j]>array[j+1]:#comparison of consecutive characters
      #swapping the elements
        array[j],array[j+1]=array[j+1],array[j]
  print("Sorted array:",array)

bsort([77,23,12,53,21,30])
