import unittest
from FamilyTree import FamilyTree
from Person import Person

class FamilyTreeBaseClass(unittest.TestCase):
	def setUp(self):
		self.ftree = FamilyTree()

class FamilyTreeUnitTest(FamilyTreeBaseClass):
	def testaddPersons(self):

		# Test 1
		self.ftree.addPerson(None)
		assert len(self.ftree.adjList.keys()) == 0,"None should not be added"

		# Test 2
		p = Person("Subbu","Venkatesan")
		self.ftree.addPerson(p)
		assert len(self.ftree.adjList.keys()) == 1,"Person not added"

		# Test 3
		self.ftree.addPerson(p)
		assert len(self.ftree.adjList.keys()) == 1,"Duplicate person added"

		# Test 4
		p = Person("S","V")
		self.ftree.addPerson(p)
		assert len(self.ftree.adjList.keys()) == 2,"Unable to add a person with the same name"

	def testsetRootParent(self):

		# Test 1
		p = Person("S","V")
		self.ftree.setRootParent(p)
		assert hasattr(self.ftree, 'rootParent')==False,"Person not in family, but still its the root parent"

		# Test 2
		self.ftree.addPerson(p)
		self.ftree.setRootParent(p)
		assert self.ftree.rootParent==p,"Unable to set the root parent"

	def testfindParent(self):

		# Test 1
		p = Person("S","V")
		self.ftree.addPerson(p)
		parent = self.ftree.findParent(p)
		assert parent == None,"Parent must be none"

		# Test 2
		parent = self.ftree.findParent(None)
		assert parent == None,"Parent must be none"

		# Test 3
		o = Person("Subbu","V")
		self.ftree.addPerson(o)
		self.ftree.connectPersons(p,o)
		parent = self.ftree.findParent(o)
		assert parent == p,"Parent is wrong"

		# Test 4
		x = Person("X","Y")
		self.ftree.addPerson(x)
		self.ftree.connectPersons(o,x)
		parent = self.ftree.findParent(x)
		assert parent == o,"Parent is wrong"

	def testconnectPerson(self):
		
		# Test 1
		p = Person("S","V")
		self.ftree.addPerson(p)
		o = Person("Subbu","V")
		self.ftree.addPerson(o)
		self.ftree.connectPersons(p,o)
		assert self.ftree.findParent(o) == p,"ConnectPersons is wrong"

		# Test 2
		self.ftree.connectPersons(o,o)
		assert self.ftree.findParent(o)!=o,"Should not connect the same person"

		# Test 3
		x = Person("x","z")
		self.ftree.addPerson(x)
		self.ftree.connectPersons(x,o)
		assert self.ftree.findParent(o) == x,"ConnectPersons is wrong"

	def testgetGrandParentNode(self):

		# Test 1
		grandParent = self.ftree.getGrandParentNode(None)
		assert grandParent==None,"GrandParent should be none"

		# Test 2
		p = Person("S","V")
		self.ftree.addPerson(p)
		o = Person("Subbu","V")
		self.ftree.addPerson(o)
		self.ftree.connectPersons(p,o)
		grandParent = self.ftree.getGrandParentNode(p)
		assert grandParent==None,"GrandParent should be none"

		# Test 3
		grandParent = self.ftree.getGrandParentNode(o)
		assert grandParent==None,"GrandParent should be none"

		# Test 4
		grandParent = self.ftree.getGrandParentNode(p)
		assert grandParent==None,"GrandParent should be none"

		# Test 5
		x = Person("x","z")
		self.ftree.addPerson(x)
		self.ftree.connectPersons(o,x)
		grandParent = self.ftree.getGrandParentNode(x)
		assert grandParent==p,"GrandParent Method is wrong"

	def testremovePersonAndChildren(self):

		# Test 1
		c = len(self.ftree.adjList.keys())
		self.ftree.removePersonAndChildren(None)
		assert c==len(self.ftree.adjList.keys()),"Nothing should be removed when None is passed"

		# Test 2
		p = Person("S","V")
		self.ftree.addPerson(p)
		o = Person("Subbu","V")
		self.ftree.addPerson(o)
		self.ftree.connectPersons(p,o)
		x = Person("x","z")
		self.ftree.addPerson(x)
		self.ftree.connectPersons(o,x)
		children = self.ftree.adjList[p]
		self.ftree.removePersonAndChildren(p)
		assert o not in self.ftree.adjList,"Person not removed"
		for child in children:
			assert child not in self.ftree.adjList,"Children not removed"

		# Test 3
		p = Person("S","V")
		self.ftree.addPerson(p)
		o = Person("Subbu","V")
		self.ftree.addPerson(o)
		self.ftree.connectPersons(p,o)
		x = Person("x","z")
		self.ftree.addPerson(x)
		self.ftree.connectPersons(o,x)
		children = self.ftree.adjList[o]
		self.ftree.removePersonAndChildren(o)
		assert o not in self.ftree.adjList,"Person not removed"
		for child in children:
			assert child not in self.ftree.adjList,"Children not removed"



if __name__ == "__main__":
	unittest.main() 
