class Person:

  def __init__(self,firstName,lastName):
    self.firstName = firstName
    self.lastName = lastName


  def setFirstName(self,firstName):
    self.firstName = firstName

  def setLastName(self,lastName):
    self.lastName = lastName


  def __hash__(self):
    return hash((self.firstName,self.lastName))


  def __str__(self):
    return self.firstName + " "+self.lastName
