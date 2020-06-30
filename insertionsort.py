'''Program to demonstrate Insertion Sort'''
def inssort(array):
  for i in range(1,len(array)):
    j=i
    while j>=1:
      if array[j]<array[j-1]:#comparison of previous elements
      #swapping of elements
        array[j],array[j-1]=array[j-1],array[j]
      j-=1#decreementing the index
  print('The Sorted Array is:')
  for i in array:
    print(i,end=" ")
  print()

inssort([23,45,12,67,32,7])
