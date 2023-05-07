#Searching & Sorting Techniques


'''
# Find the maximum element in a list
steps to find max in array 
1. asumme first ele is max element
2. Iterate over all elements in list
    a. if any element is grater than max element, assign max value to max varible
3. Finally will get maximum element in array with time complexity 'n'


'''
def maxEle(L):
    max = L[0]
    for i in range(len(L)):
        if L[i]>max:
            max = L[i]
    return max
print(maxEle([1,2,3,4,5,6,7,8,9,10]))


'''
Check whether a list contains duplicates
Nave approch:
1. take first element at 0 index position in array.
2. compare first element with all other element by scanning array.
3. if match found at any position return match otherwise scan complete array.
4. after scanning complete array, take element at index position 1 scan array fro this position onwards.
5. reapeat procedure until you scan all elemnts in array with sequenetial comparison

steps:
1. apply first for loop over length of array
2. nested for loop from index position first to length of array
3. If match found return true otherwise false

complexity of this program is n**2

'''

def noDuplicates(L):
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if L[i]==L[j]:
                return 'Duplicate element present'
    
    return 'No Duplicate element is present'

print(noDuplicates([1,2,3,4,5,1]))


'''
Matrix multiplication
Matrix is represented as list of lists
[[1,2,3],[4,5,6]]
Input matrices have size m × n, n × p
Output matrix is m × p
Three nested loops

Overall time is O(mnp) — O(n**3) if
both are n × n

'''

def matrixMultiply(A,B):
    (m,n,p) = (len(A),len(B),len(B[0]))

    C = [[ 0 for i in range(p) ] for j in range(m) ]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] = C[i][j] + A[i][k]*B[k][j]
    return(C)


    '''
    Number of bits in binary representation of n
    log n steps for n to reach 1
    '''

def numberOfBits(n):
    count = 1
    while n > 1:
        count = count + 1
        n = n // 2
    return(count)


'''
Searching in a List

Is value v present in list l?
below solution scans the list
Input size n, the length of the list
Worst case is when v is not present in l
Worst case complexity is O(n)


'''

def search(v,l):
    for i in l:
        if v==i:
            return 'element found in array'
    return 'element not found in array'

print(search(v=0,l=[1,2,3,4,5,6,0]))


'''

Binary Search:
 ---if l is sorted in ascending order
 ---Compare v with the midpoint of l
    --If midpoint is v, the value is found
    --If v less than midpoint, search the first half
    --If v greater than midpoint, search the second half
    --Stop when the interval to search becomes empty

--Search in an unsorted list takes time O(n)
--Need to scan the entire list
--Worst case is when the value is not present in the list
--For a sorted list, binary search takes time O(log n)
--Halve the interval to search each time


'''
# Non-Recurcive Implementation

def binarysearch(L, v):
    low = 0
	high = len(L) - 1
	while low <= high: 
	    mid = (low + high) // 2
	    if L[mid ] < v:
	        low = mid  + 1
	    elif L[mid ] > v:
	        high = mid  - 1
	    else:
	        return mid
    return False
	
L = [1,3,4,5,6,8]
v = 6
print(binarysearch(L,v))



# Recurcive Implementation

def bsearch(v,l):
    if l == []:
        return(False)
    m = len(l)//2
    if v == l[m]:
        return(True)
    if v < l[m]:
        return(bsearch(v,l[:m]))
    else:
        return(bsearch(v,l[m+1:]))


'''
Selection Sort

Strategy:

--Scan the entire pile and find the paper with minimum marks

--Move this paper to a new pile

--Repeat with the remaining papers
    Add the paper with next minimum marks to the second pile each time

--Eventually, the new pile is sorted in descending order


Steps:

1. Select the next element in sorted order
2. Append it to the final sorted list
3. Avoid using a second list
    --Swap the minimum element into the first position
    --Swap the second minimum element into the second position
    -- ...
4. Eventually the list is rearranged in place in ascending order

Worst case complexity is O(n**2)
'''

def SelectionSort(L):
    n = len(L)
    if n < 1:
        return(L)
    for i in range(n):
        # Assume L[:i] is sorted
        mpos = i
        # mpos: position of minimum in L[i:]
        for j in range(i+1,n):
            if L[j] < L[mpos]:
                mpos = j
        # L[mpos] : smallest value in L[i:]
        # Exchange L[mpos] and L[i]
        (L[i],L[mpos]) = (L[mpos],L[i])
        # Now L[:i+1] is sorted
    return(L)




'''
Strategy:

--Move the first paper to a new pile
--Second paper
    --Lower marks than first paper? Place below
    --first paper in new pile
    --Higher marks than first paper? Place above
    --first paper in new pile
--Third paper
    --Insert into correct position with respect to first two

--Do this for the remaining papers

Steps:
1. Start building a new sorted list
2. Pick next element and insert it into the sorted list
3.An iterative formulation 
    Assume L[:i] is sorted
    Insert L[i] in L[:i]
or 
3. A recursive formulation
    Inductively sort L[:i]
    Insert L[i] in L[:i]


Worst case Complexity is O(n**2)
'''

def InsertionSort(L):
    n = len(L)
    if n < 1:
        return(L)
    for i in range(n):
        # Assume L[:i] is sorted
        # Move L[i] to correct position in L[:i]
        j = i
        while(j > 0 and L[j] < L[j-1]):
            (L[j],L[j-1]) = (L[j-1],L[j])
            j = j-1
            # Now L[:i+1] is sorted
    return(L)


# Recurcive Method

def Insert(L,v):
    n = len(L)
    if n == 0:
        return([v])
    if v >= L[-1]:
        return(L+[v])
    else:
        return(Insert(L[:-1],v)+L[-1:])

def ISort(L):
    n = len(L)
    if n < 1:
        return(L)
    L = Insert(ISort(L[:-1]),L[-1])
    return(L)
