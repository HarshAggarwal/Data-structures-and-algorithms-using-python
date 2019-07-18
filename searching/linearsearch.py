def linear_search(list1 , item):
	pos = 0
	found = False

	while (pos<len(list1) and not found):
		if(list1[pos] == item):
			found = True
		else:
			pos+=1
	return found

def improved_version(list1 , item): #list should be ordered in ascending order
	pos = 0
	found = False
	stop = False

	while (pos<len(list1) and not found and not stop):
		if(list1[pos] == item):
			found = True
		elif(list1[pos]>item):
			stop = True
		else:
			pos+=1
	return found


#driver_code
tlist = [1,5,7,9,6,4,5,45,69,58,23,12]
print(linear_search(tlist , 9))
print(linear_search(tlist , 22))