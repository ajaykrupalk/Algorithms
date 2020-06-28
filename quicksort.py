'''Program to demonstrate Quick Sort'''
def partition(a,low,high):
  key=a[low]#taking first element as pivot
  i=low
  j=high
  while i<j:
    while a[i]<=key:
      i+=1
    while a[j]>=key:
      j-=1
    if i<=j:
    #swapping elements
      a[i],a[j]=a[j],a[i]
  #swapping pivot and first element 
  a[low],a[j]=a[j],key
  return j

def quicksort(a,low,high):
  if low<high:
    p=partition(a,low,high)#getting partition
    quicksort(a,low,p-1)
    quicksort(a,p+1,high)

a=[23,30,21,12,7]
quicksort(a,0,4)
print(a)
