def selection_sort(list1):
	for fill_slot in range(len(list1)-1,0,-1):
		pos_of_max = 0
		for location in range(1,fill_slot+1):
			if(list1[location] > list1[pos_of_max]):
				pos_of_max = location
		list1[fill_slot],list1[pos_of_max] = list1[pos_of_max],list1[fill_slot]

