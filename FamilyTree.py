from Person import Person

class FamilyTree:
  def __init__(self):
    self.adjList = dict()
    self.rootParent = None

  def findParent(self,person):
    for parent, children in self.adjList.iteritems():
      for child in children:
        if child == person:
          return parent
    return None

  def getGrandParentNode(self,person):
    if person in self.adjList:
      parent = self.findParent(person)
      if parent is not None:
        grandParent = self.findParent(parent)
        return grandParent 
      else:
        return None

  def addPerson(self,person):
   if person not in self.adjList:
      self.adjList[person] = []
   else:
     print str(person)+ " already present"
 
  def setRootParent(self,person):
    if person is not None:
      self.rootParent = person

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

  def removePersonAndChildren(self,person):
      if person in self.adjList:
        children = self.adjList[person]
        self.removePerson(person)
        for child in children:
          self.removeParentAndChildren(child)
      
  def removePerson(self,person):
    if person in self.adjList:
      parent = self.findParent(person)
      if parent is not None:
        children = self.adjList[parent]
        children.remove(person)
      del self.adjList[person]

  def printTreeHelperFunction(self,person,spaces):
    if person is not None:
      print spaces + str(person)
      children = self.adjList[person]
      for child in children:
        self.printTreeHelperFunction(child,spaces + '\t')


  def printTree(self):
    self.printTreeHelperFunction(self.rootParent,'')

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
