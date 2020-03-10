import pdb
class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class LinkedList:
	def __init__(self):
		self.head=None

	def insert(self,data):
		
		newNode=Node(data)
		if self.head is None:
			self.head=newNode
		else:
			lastNode=self.head
			while True:
				if lastNode.next is None:
					break
				lastNode=lastNode.next
			lastNode.next=newNode

	def listlen(self):
		currentNode=self.head
		length=0
		while currentNode is not None:
			length+=1
			currentNode=currentNode.next
			
		return length		


	def insertStart(self,data):
		newNode=Node(data)
		temporary=self.head
		self.head=newNode
		self.head.next=temporary
		del temporary 
				
	def insertAt(self,newNode,pos):
		if pos < 0 or pos > self.listlen():
			print("Invalid Position")	
			return
		if pos is 0:
			self.insertStart(newNode)
			return
		currentNode=self.head
		currentPos=0
		while True:
			if currentPos==pos:
				previousNode.next=newNode
				newNode.next=currentNode
				break
			previousNode=currentNode	
			currentNode=currentNode.next
			currentPos+=1		
	
	def deleteEnd(self):
		lastNode=self.head
		while True:
			if lastNode.next is None:
				del lastNode
				previousNode.next=None
				break
			previousNode=lastNode
			lastNode=lastNode.next		

	def deleteAt(self,pos):
		if pos<0 or pos>self.listlen():
			print("Invalid Position")
			print("-----------------\nfollowing are the inserted items:-\n------")
			return
		lastNode=self.head
		currentPos=0
		
		if currentPos==pos:
			temp=lastNode
			del lastNode
			self.head=temp.next
			print("deleted item is",temp.data)
			del temp
		else:	
			while True:
				if currentPos==pos:
					temp=lastNode
					del lastNode
					previousNode.next=temp.next
					print("deleted item is ",temp.data)
					del temp
					break
				previousNode=lastNode
				lastNode=lastNode.next
				currentPos+=1				
	def deleteData(self,num):
		currentNode=self.head
		# print(currentNode.data)
		while True:
			if currentNode==num:
				temp=currentNode
				del currentNode
				previousNode.next=temp.next
				del temp
			previousNode=currentNode
			currentNode=currentNode.next	

	def reverse(self):
		prev=None
		cur=self.head
		while cur is not None:
			nextnode=cur.next
			cur=prev
			prev=cur
			cur=nextnode.next
		# self.head=prev
	def sort(self):
		cur=self.head
		index=None
		while cur!=None:
			index=cur.next
			while index!=None:
				if cur.data>index.data:
					temp=cur.data
					cur.data=index.data
					index.data=temp
				index=index.next	
			cur=cur.next
	def middle(self):
		slow=self.head
		fast=self.head
		while fast!=None:
			fast=fast.next
			if fast==None:
				return slow
			fast=fast.next
			slow=slow.next
		return slow
	def breakl(self):
		slow=self.head
		fast=self.head
		while fast!=None and fast.next!=None:
			slow=slow.next
			fast=fast.next
			fast=fast.next
		middle=slow.next
		slow=None
		# return self.head, middle
		while self.head.next!=slow:
			print(self.head.data)
			self.head=self.head.next
		print("after first list")	
		while middle:
			print(middle.data)
			middle=middle.next					
	def printEnd(self,lst):
		if lst==None:
			return 0
		head=lst
		tail=lst.next
		self.printEnd(tail)
		print(head.data)	
	def moduular(self,k):
		currentNode=self.head
		module=None
		i=1
		if k<=0:
			return None
		while currentNode:
			if i%k==0:
				module=currentNode
			i+=1
			currentNode=currentNode.next
		print(module.data)
	def evenodd(self):
		evenlist=oddlist=None
		evenlistEnd=oddlistEnd=None
		itr=self.head
		if itr==None:
			return None
		else:
			while itr:
				if (itr.data%2==0):
					if evenlist==None:
						evenlist=evenlistEnd=itr
					else:
						evenlistEnd.next=itr
						evenlistEnd=itr
				else:
					if (oddlist==None):
						oddlist=oddlistEnd=itr
					else:
						oddlistEnd.next=itr
						oddlistEnd=itr
				itr=itr.next
			evenlistEnd.next=oddlist
			oddlist.next==None
		cur=evenlist
		while cur!=None:
			print(cur.data)
			cur=cur.next
			if cur.next==oddlist:
				break

			# cur=evenlistEnd
			# while evenlistEnd!=None:
				# print(cur.data)
				# cur=cur.data								

	def iseven(self):
		cur=self.head
		while cur!=None and cur.next!=None:
			cur=cur.next.next
			if cur==None:
				return 1
			return 0 				

		# print("length of list is odd")
	def addtwonode(self,list1,list2):
		pass	
	def printList(self):
		# if self.head is None:
			# print("List is empty")
		currentNode=self.head	
		while currentNode:
			# if currentNode is None:
				# break
			print(currentNode.data)
			currentNode=currentNode.next
										


link=LinkedList()
link1=LinkedList()
# first=Node("kashif")
link.insert(66)
# second=Node("anam")
link.insert(5)
# third=Node("iqbal")
# link.insertAt(third,9)
link.insert(89)
link.insert(74)
link.insert(88)
# fourth=Node("muhammad")
link.insertStart(65)
# link.printList()
# link.deleteData("kashif")
# print("remaining items are:--")
# link.listlen()
# link.reverse()
# link.sort()
# link.middle()
link.printList()	
print("--------------")
# link.breakl()
link1.insert(90)
link1.insert(46)
link1.insert(43)
link1.insert(78)
link1.insert(56)
link1.insertStart(65)
link1.printList()

# link.moduular(4)
# link.iseven()	
# link.printEnd(link.head)								 
# link.evenodd()

