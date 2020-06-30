'''Program to demonstrate Shell Sort'''
def shsort(array,n):
  gap=n//2#creating a gap
  while gap>0:
    for i in range(gap,n):
      pos=array[i]
      j=i
      while j>=gap and array[j-gap]>pos:
      #comparing on either side of the gaps
        array[j]=array[j-gap]
        j-=gap
      array[j]=pos#swapping element
    gap//=2#reducing the gap by two

mylist=[45,23,13,2,94,61,15,7]#array of 8 elements
length=len(mylist)
shsort(mylist,length)
print(mylist)
