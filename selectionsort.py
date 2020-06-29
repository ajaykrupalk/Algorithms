'''Program to demonstarte Selection Sort'''
def ssort(array):
  for i in range(len(array)):
    pos=i
    for j in range(i+1,len(array)):
      if array[j]<array[pos]:
        pos=j
    array[i],array[pos]=array[pos],array[i]
  print("Sorted Array:")
  for i in array:
    print(i,end=" ")
  print()
    
array=[45,75,30,25,15,17]
ssort(array)
