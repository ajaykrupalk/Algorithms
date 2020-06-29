'''Program to demonstrate Shell Sort'''
def lsearch(array,search):
  for element in array:
    if element==search:#comparison of element with element to be searched
      return "Element found"
  return "Element not found"

array=[12,24,22,30,35,7]
print(lsearch(array,30))
