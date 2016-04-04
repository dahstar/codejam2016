def sequentialSearch(alist, item):
	    pos = 0
	    found = False
	
	    while pos < len(alist) and not found:
	        if alist[pos] == item:
	            found = True
	        else:
	            pos = pos+1
	
	    return found
def orderedSequentialSearch(alist, item):
	    pos = 0
	    found = False
	    stop = False
	    while pos < len(alist) and not found and not stop:
	        if alist[pos] == item:
	            found = True
	        else:
	            if alist[pos] > item:
	                stop = True
	            else:
	                pos = pos+1
	
	    return found
def binarySearch(alist, item):
	    first = 0
	    last = len(alist)-1
	    found = False
	
	    while first<=last and not found:
	        midpoint = (first + last)//2
	        if alist[midpoint] == item:
	            found = True
	        else:
	            if item < alist[midpoint]:
	                last = midpoint-1
	            else:
	                first = midpoint+1
	
	    return found
testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))