'''Program to demonstrate Merge Sort'''
def mergesort(array):
    if len(array)>1:
        mid=len(array)//2#finding the middle of array
        #dividing array into two halves
        left=array[:mid]
        right=array[mid:]
        #recursively calling the mergesort()
        mergesort(left)
        mergesort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:#checking for smaller element
                array[k]=left[i]
                i+=1
            else:
                array[k]=right[j]
                j+=1
            k+=1
        #for leftover elements
        while i<len(left):
            array[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            array[k]=right[j]
            j+=1
            k+=1
        
def display(array):
  for i in array:
    print(i,end=" ")
  print()
    
array=[67,78,34,12,54]
mergesort(array)
display(array)
