def insertion_sort(a_list):
	for index in range(1, len(a_list)):

		current_value = a_list[index]
		pos = index

		while(pos>0 and a_list[pos-1]>current_value):
			a_list[pos] = a_list[pos-1]
			pos = pos-1

		a_list[pos] = current_value

a_list = [54,26,93,17,77,31,44,55,20]
insertion_sort(a_list)
print(a_list)