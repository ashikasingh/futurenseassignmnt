#SELECTION SORT 
A = [64, 25, 12, 22, 11]
  # Traverse through all array elements
for i in range(len(A)):
      
    # Find the minimum element in remaining 
    # unsorted array
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
              
    # Swap the found minimum element with 
    # the first element        
    A[i], A[min_idx] = A[min_idx], A[i]
print ("Sorted array")
for i in range(len(A)):
    print("%d" %A[i]), 

#BUBBLE SORT
def bubblesort(elements):
  # Looping from size of array from last index[-1] to index [0]
  for n in range(len(elements)-1, 0, -1):
    for i in range(n):
      if elements[i] > elements[i + 1]:
        # swapping data if the element is less than next element in the array
        elements[i], elements[i + 1] = elements[i + 1], elements[i]
elements = [39,12,18,85,72,10,2,18]
  
print("Unsorted list is,") 
print( elements)
bubblesort(elements)
print("Sorted Array is, ")
print(elements)