
'''
left, right and middle represent indicies in the list
binary search returns the index of the found element
if the element is not found, it will return -1
'''

def iterative_binary_search(list_to_search, num_to_find):
	left = 0
	right = len(list_to_search) - 1
	middle = (left + right) / 2

	while (left <= right): 

		if (num_to_find == list_to_search[middle]): 
			return middle
		elif (num_to_find < list_to_search[middle]):
			right = middle -1
			middle = (left + right) / 2
		else:
			left = middle + 1
			middle = (left + right) / 2

	return -1

def recursive_binary_search(list_to_search, num_to_find, right, left=0):
	middle = (left + right) / 2

	if (left >= right):
		return -1
	if num_to_find == list_to_search[middle]:
		return middle
	if num_to_find > list_to_search[middle]:
		return recursive_binary_search(list_to_search, num_to_find, right, middle+1)
	else:
		return recursive_binary_search(list_to_search, num_to_find, middle-1, left)



def main():
	list_to_search = [1, 2,  3, 4, 5, 6, 10, 11, 29]
	num_to_find = 11

	print "iterative: ", iterative_binary_search(list_to_search, num_to_find)

	right = len(list_to_search) - 1
	print "recursive: ", recursive_binary_search(list_to_search, num_to_find, right=right)


if __name__ == '__main__':
	main()