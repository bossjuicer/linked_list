class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class LinkedList:
	def __init__(self):
		self.head=None
# class AddingList:
# 	def addlist(self,list1,list2):
# 		if list1==None:
# 			return list2
# 		if list2==None:
# 			return list1
# 		len1=len2=0
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
	def seriesinsert(self):
			n=int(input("How many node you want to enter\n"))
			if n<=0:
				return 
			else:
				for i in range(n):
					value=int(input("enter node\n"))
					self.insert(value)	
	def sumall(self):
		lastNode=self.head
		summ=0
		while lastNode:
			summ=summ+lastNode.data
			lastNode=lastNode.next
		print(summ)
	def reform(self,x):
		lesser=lesserHead=Node(0)
		greater=greaterHead=Node(0)
		cur=self.head
		while cur:
			if cur.data<x:
				lesser.next=cur
				lesser=lesser.next
			else:
				greater=cur
				greater=greater.next
			cur=cur.next
		greater.next=None
		lesser.next=greaterHead.next			
	def printL(self):
		print("following are the nodes\n")
		cur=self.head
		while cur!=None:
			print(cur.data)
			cur=cur.next					

link=LinkedList()
link.seriesinsert()

# link.sumall()
print("---------------")
link.reform(4)
link.printL()
