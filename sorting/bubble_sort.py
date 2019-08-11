def bubble_sort(list1):
	for i in list1:
		for j in i:
			if(list1[j] > list1[j+1]):
				list1[j],list1[j+1] = list1[j+1],list1[j]
	print(list1)

  #enhanced bubble sort
def short_bubble(list2):
	exchanges = True
	n = len(list2)-1
	while n>0 and exchanges:
		exchanges = False
		for i in range(n):
			if(list2[i]>list2[i+1]):
				exchanges = True
				list2[i],list2[i+1] = list2[i+1],list2[i]
				n = n-1
				