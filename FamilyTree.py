from Person import Person
import pickle

class FamilyTree:
  def __init__(self):
    self.adjList = dict()
    

  """
    Given a person, this method returns the parent, if its a root of the familyTree returns None
  """
  def findParent(self,person):
    if person is None:
      return None
    for parent, children in self.adjList.iteritems():
      for child in children:
        if child == person:
          return parent
    return None

  """
    Returns the grandParent of the person or None if the grandParent is not present
  """
  def getGrandParentNode(self,person):
    if person in self.adjList:
      parent = self.findParent(person)
      if parent is not None:
        grandParent = self.findParent(parent)
        return grandParent 
      else:
        return None

  """
    Adds a person to a family Tree
  """
  def addPerson(self,person):
    if person is None:
      print "Person is None"
      return
    if person not in self.adjList:
      self.adjList[person] = []
    else:
     print str(person)+ " already present"
 
  """
    Sets a person as a root of the familyTree
  """
  def setRootParent(self,person):
    if person is not None and person in self.adjList:
      self.rootParent = person

  """
    Connects two persons. If the second person is connected to another parent, removes the connection and connects with a first person
  """
  def connectPersons(self,personA,personB):
    if personA == personB:
      print "Same Person"
      return
    if personA in self.adjList and personB in self.adjList:
       parent = self.findParent(personB)
       if parent is not None:
         children = self.adjList[parent]
         children.remove(personB)
       vals = self.adjList[personA]
       if personB not in vals:
          vals.append(personB)
    else:
       print "Add " + str(personA)

  """
    Private Method. Removes a person from the Tree
  """
  def __removePerson(self,person):
    if person in self.adjList:
      parent = self.findParent(person)
      if parent is not None:
        children = self.adjList[parent]
        children.remove(person)
      del self.adjList[person]

  """
    Recursively removes a person and their children
  """
  def removePersonAndChildren(self,person):
      if person in self.adjList:
        children = self.adjList[person]
        self.__removePerson(person)
        for child in children:
          self.removePersonAndChildren(child)
   
  """
    Private Method that does the printing work
  """
  def __printTreeHelperFunction(self,person,spaces):
    if person is not None:
      print spaces + str(person)
      children = self.adjList[person]
      for child in children:
        self.__printTreeHelperFunction(child,spaces + '\t')

  """
    Public method for printing the tree
  """
  def printTree(self):
    if hasattr(self,"rootParent") is True:
      self.__printTreeHelperFunction(self.rootParent,'')
    else:
      print "Please set the rootParent using setRootParent method"

  """
    Returns a string representation of the family tree
  """
  def __str__(self):
   objStr=''
   for key,value in self.adjList.iteritems():
     objStr = objStr + str(key) + ":["
     for person in value:
         objStr=objStr+ str(person)+", "
     objStr = objStr + "]\n"
   return objStr
  

if __name__ == "__main__":

  ftree = FamilyTree() 
  Randall = Person("Randall","Jack")
  Betty = Person("Betty","Lisa")
  Charles = Person("Charles","Robert")
  Rebecca = Person("Rebecca","Banks")
  David = Person("David","Beckham")
  Sam = Person("Sam","Anderson")
  Sophia = Person("Sophia","Princess")
  Mary = Person("Mary","Jesus")
  Thomas = Person("Thomas","Muller")
  Frank = Person("Frank","Ribery")
  FamilyMembers=[Randall,Betty,Charles,Rebecca,David,Sam,Sophia,Mary,Thomas,Frank] 
  for member in FamilyMembers:
    ftree.addPerson(member)

  ftree.connectPersons(Randall,Charles)
  ftree.connectPersons(Randall,David)
  ftree.connectPersons(Randall,Betty)
  ftree.connectPersons(Charles,Rebecca)
  ftree.connectPersons(David,Sam)
  ftree.connectPersons(David,Sophia)
  ftree.connectPersons(Sam,Mary)
  ftree.connectPersons(Rebecca,Thomas)
  ftree.connectPersons(Rebecca,Frank)
  ftree.setRootParent(Randall)
  ftree.printTree()
