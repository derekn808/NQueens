class Node:

	def __init__(self, data, parent=None):
		self.data = data 
		self.parent = parent
		self.children = []

	def getData(self):
		return self.data

	def setData(self, data):
		self.data = data
		return 

	def getChildren(self):
		return self.children

	def addChild(self, node):
		self.children.append(node)
		return node

	def getParent(self):
		return self.parent

	def setParent(self, par):
		self.parent = par
		return 
