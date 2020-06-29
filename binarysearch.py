'''Program to demonstrate Binary Search'''
def bsearch(array,low,high,search):
  if low<=high:
    mid=(low+high)//2
    if array[mid]==search:#if element is found at mid
      return f"Found at {mid}"
    elif search<array[mid]:#checking if element is less than that present at mid
      return bsearch(array,low,mid-1,search)
    else:#checking if element is greater than that present at mid
      return bsearch(array,mid+1,high,search)
  else:
    return "Not Found"

a=[78,56,23,45,77,27]
print(bsearch(a,0,len(a)-1,77)) 
