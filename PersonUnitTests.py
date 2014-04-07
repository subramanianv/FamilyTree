import unittest
from Person import Person

class PersonUnitTestBaseClass(unittest.TestCase):
  def setUp(self):
    self.person = Person("Subramanian","Venkatesan")

class PersonUnitTest(PersonUnitTestBaseClass):
  def testsetFirstName(self):

    self.person.setFirstName("Subbu")
    assert self.person.firstName == "Subbu", "Incorrect first name"
    
    self.person.setFirstName(None)
    assert self.person.firstName != None ,"Should not set None"

    self.person.setFirstName(23)
    assert isinstance(self.person.firstName,str) == True

    self.person.setFirstName("")
    assert len(self.person.firstName) > 0,"Length of the string must be greater than 0" 
  
  def testsetLastName(self):
    self.person.setLastName("Subbu")
    assert self.person.lastName == "Subbu", "Incorrect first name"
    
    self.person.setLastName(None)
    assert self.person.lastName != None ,"Should not set None"

    self.person.setLastName(23)
    assert isinstance(self.person.lastName,str) == True

    self.person.setLastName("")
    assert len(self.person.lastName) > 0,"Length of the string must be greater than 0" 

  def testHashFunction(self):
    assert self.person.__hash__() == hash((self.person.firstName,self.person.lastName)),"Hash function is wrong"

  def testStringFunction(self):
    assert self.person.__str__() == self.person.firstName + " " + self.person.lastName,"str is wrong"

if __name__ == "__main__":
  unittest.main() 
