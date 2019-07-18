def binary_search(a_list , item):
	first = 0
	last = len(a_list)-1
	found = False

	while(first<=last and not found):
		midpoint = (first+last)//2
		if(a_list[midpoint]==item):
			found = True
		elif(item < a_list[midpoint]):
			last = midpoint-1
		else:
			first = midpoint+1
	return found

def binary_search_recursion(a_list,item):
	if(len(a_list) == 0):
		return False
	else:
		midpoint = len(a_list)//2
		if(a_list[midpoint]==item):
			return True
		elif(item < a_list[midpoint]):
			return binary_search_recursion(a_list[:midpoint] , item)
		else:
			return binary_search_recursion(a_list[midpoint+1:] , item)

#driver code
#list must be sorted

list1 = [1,2,3,4,5,6,7,8,9,45,54,56,65,69]
print(binary_search(list1 , 45))
print(binary_search_recursion(list1 , 69))