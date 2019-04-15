from node import *
import queue

class NQueens:


	def __init__(self, n):

		if n<4:
			print ("Solution not possible for board smaller than 4x4.")
			return False
		
		self.solutions = []
		self.possibleSolnStates(n)


	def possibleSolnStates(self, n):
		emptyBoard = (-1,)*n
		
		root = Node(emptyBoard, parent=None)
		self.q = queue.LifoQueue()
		self.q.put(root)

		while not self.q.empty():
			temp = self.q.get()
			newData = list(temp.getData())
			f=0
			for j in range(n-1, -1, -1):
				for i,x in enumerate(newData):
					if x == -1:
						f=1
						break
				if f == 1:
					tempData = newData.copy()
					tempData[i] = j
					if self.checkBoard(tempData):
						self.solutions.append(tuple(tempData))
					newNode = Node(tuple(tempData), temp)
					temp.addChild(newNode)
					self.q.put(newNode)


	def checkBoard(self, board): #checks a list to see if it passes the n queens problem
		f=0
		for i in range(len(board)):
			if f == 1:
				break
			if board[i] == -1:
				f=1
				break
			for j in range(0, i):
				if board[j]==board[i]:
					f=1
					break
				if abs((board[i]-board[j])/(i-j))==1:
					f=1
					break
		if f == 0:
			return True
		else:
			return False

	def printSolutions(self):
		for i in range(len(self.solutions)):
			print (self.solutions[i])