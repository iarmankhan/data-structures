# Simple Python3 program to find
# n'th node from end


class Node:
	def __init__(self, new_data):
		self.data = new_data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	# createNode and and make linked list
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# Function to get the nth node from
	# the last of a linked list
	def printNthFromLast(self, n):
		temp = self.head  # used temp variable

		length = 0
		while temp is not None:
			temp = temp.next
			length += 1

		# print count
		if n > length:  # if entered location is greater
					# than length of linked list
			print('Location is greater than the' +
						' length of LinkedList')
			return
		temp = self.head
		for i in range(0, length - n):
			temp = temp.next
		print(temp.data)

	def find_mid(self):
		slow_pt = self.head
		fast_pt = self.head
		count = 0
		if self.head is not None:
			while fast_pt is not None and fast_pt.next is not None:
				slow_pt = slow_pt.next
				fast_pt = fast_pt.next.next
				count += 1

			return slow_pt.data

# Driver Code		 
llist = LinkedList() 
llist.push(1) 
llist.push(2) 
llist.push(3) 
llist.push(4) 
llist.push(5) 
print(llist.find_mid())

# This code is contributed by Yogesh Joshi 
