import unittest
from base import *

print()
# https://docs.python.org/3/library/unittest.html  referencias 
class SimpleTest(unittest.TestCase):

    # Returns True or False. 
    def test(self):        
        self.assertTrue(confirm('cruz', "1234"))
    
    
  
if __name__ == '__main__':
    unittest.main()