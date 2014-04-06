class Person:

  def __init__(self,firstName,lastName):
    self.firstName = firstName
    self.lastName = lastName


  def setFirstName(self,firstName):
    if firstName is not None and isinstance(firstName,str) and len(firstName) > 0:
      self.firstName = firstName
    else:
      print "First Name is None. Do not pass a none or pass a string"

  def setLastName(self,lastName):
    if lastName is not None and isinstance(lastName, str) and len(lastName) > 0:
      self.lastName = lastName
    else:
      print "Last Name is None. Do not pass a none. Always pass a string"


  def __hash__(self):
    return hash((self.firstName,self.lastName))


  def __str__(self):
    return self.firstName + " "+self.lastName
