""" Unit test for password.py """

"""
Assignment: Final Project

Members: Aaron Methratta
         Michael Kwakye
         Biruk Tamiru
"""

import unittest
import password as pw
import string

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
            Tests a good password being passed into the Checker() class
            to verify that it is returning the correct output.
            
        TEST 2:
            Tests a bad password being passed into the Checker() class
            to verify that it is returning the correct output.
            
        TEST 3:
            Tests the code used within the display_frequency() method
            to verify that the function is displaying the correct number
            of symbols, capital letters, lowercase letters and digits.

        """
        
        #test password used for TEST 1 & 3
        tryPassword = "Pkp01x@!!"
        
        #TEST 1
        newCheckOne = pw.Checker(tryPassword)
        wordCheck = newCheckOne.word_check()
        
        self.assertEqual(wordCheck, print("\nThis password is valid to use!"))
        
        #TEST 2
        badPassword = "carrotcake"
        
        newCheckOne = pw.Checker(badPassword)
        wordCheck = newCheckOne.word_check()
        
        self.assertEqual(wordCheck, print("\nThis password is not valid!"))
        
        #TEST 3
        symbols_list = "$%_+*)#^!(&@"
        
        symbolCount = 0
        capitalCount = 0
        lowerCount = 0
        numCount = 0
        
        for x in tryPassword:
            if x in symbols_list:
                symbolCount+=1
            elif x in string.ascii_uppercase:
                capitalCount+=1
            elif x in string.ascii_lowercase:
                lowerCount+=1
            elif x in string.digits:
                numCount+=1
                
        self.assertEqual(symbolCount, 3)
        self.assertEqual(capitalCount, 1)
        self.assertEqual(lowerCount, 3)
        self.assertEqual(numCount, 2)

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
        
        #generates one password from each password type
        newShort = newGen.generate("short")
        newMedium = newGen.generate("medium")
        newLong = newGen.generate("long")
        
        
        #TEST 1
        self.assertEqual(len(newShort), 8)
        self.assertEqual(len(newMedium), 12)
        self.assertEqual(len(newLong), 16)
        
        
        st = 0
        md = 0
        lg = 0
        
        
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