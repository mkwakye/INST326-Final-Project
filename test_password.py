""" Unit test for password.py """

"""
Assignment: Final Project

Members: Aaron Methratta
         Michael Kwakye
         Biruk Tamiru
"""

import unittest
import password as pw

class TestPassword(unittest.TestCase):
    """
    Agrs:
        unittest.TestCase: Component within unittest module
        
    This class TestPassword will run unit tests on our three classes for
    password.py using test_store(), test_checker() and test_generate().
    """
    def test_store(self):
        """ 
        function that tests some
        cases in the Password class within the password program
        
        TEST 1: 
            Determine whether or not the object being returned from the
            store_password() method is a dictionary
            
            INFO: This test will create an instance of the Password class
                and call the store_password() method
        """
        newPass = pw.Password()
        
        testPass = newPass.store_password("Password123!@#")
        
        #TEST 1
        self.assertEqual(type(testPass), dict)
        
    def test_checker(self):
        """ 
        function that tests some
        cases in the Checker class within the password program
        
        TEST 1:
            Tests the type of the variable being passed into the Checker() class
            to verify that it is a string.
        """
        tryPassword = "p01x@"
        
        newCheckOne = pw.Checker(tryPassword)
        wordCheck = newCheckOne.word_check()
        
        self.assertEqual(type(tryPassword), str)

    def test_generate(self):
        """ 
        function that tests some
        cases in the Generator class within the password program
        
        TEST 1: 
            Determine whether or not the different password types are 
            producing appropriate length
            
            INFO: This test will create an instance of the Generator class
                and call the generate method
        TEST 2:
            Asserts that the first half of the generated password is 
            composed of only letters (lowercase and capital)
            
            INFO: This test will loop through three generated password types
                and store their values into three variables. It will then
                test to see if the variables are type string
        """
        newGen = pw.Generator()
        
        shortStr = ""
        mediumStr = ""
        longStr = ""
        
        newShort = newGen.generate("short")
        newMedium = newGen.generate("medium")
        newLong = newGen.generate("long")
        
        st = 0
        md = 0
        lg = 0
        
        #TEST 1
        self.assertEqual(len(newShort), 8)
        self.assertEqual(len(newMedium), 12)
        self.assertEqual(len(newLong), 16)
        
        #TEST 2
        while st < 4: 
            for x in newShort:
                shortStr+=x
                st+=1
            
        while md < 6:
            for x in newMedium:
                mediumStr+=x
                md+=1
            
        while lg < 8:
            for x in newLong:
                longStr+=x
                lg+=1
                
        self.assertEqual(type(shortStr), str)    
        self.assertEqual(type(mediumStr), str)
        self.assertEqual(type(longStr), str)
        
if __name__ == "__main__":
    unittest.main()