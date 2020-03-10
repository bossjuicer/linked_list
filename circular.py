class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class Linked:
	def __init__(self):
		self.head=None

	def insertEnd(self,data):
		if self.head is None:
			self.head=Node(data)
			self.head.next=self.head
		else:
			cur=self.head
			while cur:
				if cur.next==self.head:
					break
				cur=cur.next	
			newNode=Node(data)
			cur.next=newNode
			newNode.next=self.head	
	def insertHead(self,data):
		if self.head is None:
			self.head=Node(data)
			self.head.next=self.head
		else:
			cur=self.head
			while cur:
				if cur.next==self.head:
					break
				cur=cur.next
			newNode=Node(data)
			newNode.next=self.head
			cur.next=newNode
			self.head=newNode
	def delete(self,data):
		if self.head.data==data:
			cur=self.head
			while cur:
				if cur.next==self.head:
					break
				cur=cur.next
			cur.next=self.head.next
			self.head=self.head.next

		else:	
			cur =self.head	
			while cur:
				if cur.data==data:
					break
				prev=cur
				cur=cur.next
			prev.next=cur.next
			del cur.data
		# else:
			# print("wrong input")

	def insertAt(self,data,pos):
		curpos=1
		cur=self.head
		while cur.next!=self.head:
			if curpos==pos:
				break
			prev=cur
			cur=cur.next
			curpos+=1
		newNode=Node(data)
		prev.next=newNode
		newNode.next=cur

	def looplength(self):
		if None==self.head or None==self.head.next:
			return 0
		slow=self.head.next
		fast=slow.next
		while slow!=fast:
			slow=slow.next
			try:
				fast=fast.next.next
			except AttributeError:
				return 0
		looplength=0
		slow=slow.next
		while slow!=fast:
			slow=slow.next
			looplength+=1
		return looplength				
	def listlen(self):
		currentNode=self.head
		length=0
		while currentNode.next!=self.head:
			length+=1
			currentNode=currentNode.next	
		return length

	#josephus cycle for executing people	
	def josephuscycle(self):
		answer=[]
		cur=self.head
		counter=0
		while cur.next!=self.head:
			counter+=1
			if counter==3:
				counter=0
				# prev=cur.next
				answer.append(cur.data)
			# else:
				# prev=cur
			cur=cur.next
		# answer.append(cur.data)
		print(answer)

	def printList(self):
		cur=self.head
		while cur:
			print(cur.data)
			cur=cur.next
			if cur==self.head:
				break


link=Linked()
# link.insertEnd(1)
# link.insertEnd(2)
# link.insertEnd(3)
link.insertEnd(0)
link.insertEnd(1)
link.insertEnd(2)
link.insertEnd(3)
link.insertEnd(4)
link.insertEnd(5)
link.insertEnd(6)
link.insertEnd(7)
link.insertEnd(8)
link.insertEnd(9                                               )
# link.insertEnd(0)
# link.insertHead(1)
# link.insertHead(2)
# link.insertHead(3)
# link.insertHead(4)
# link.insertHead(5)
# link.insertAt("kashif",3)
# link.delete("kashif")
link.listlen()
# link.looplength()
link.printList()	
print("---------------")							
link.josephuscycle()		