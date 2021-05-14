import string
import random
import re

"""
Assignment: Final Project

Members: Aaron Methratta
         Michael Kwakye
         Biruk Tamiru

"""
class Password():
    """
    This class, Password(), will take in a password entered by the user
    and store it into a list called passwords.
    
    Attributes:
            passwords (list): List of password dictionaries
            count (int): Counter to identify passwords being inputed
    """
    def __init__(self):
        """
        This __init__() holds password dictionaries in a list called passwords
        
        Attributes:
            passwords (list): see class documentation
            count (int): see class documentation
        """
        self.passwords = []
        self.count = 1
        
    def store_password(self, words):
        """
        Agrs:
            words (string): User's input for new password
            
        This method will take in the parameter words, which represents the
        user's inputted password. Everytime this function is called the attribute
        in the __init__() method called count will be added to, representing the
        number of the password being stored. count and words will be used to create
        a dictionary that contains the password. The dictionary will then be appended
        to the attribute passwords (list)
        """
        
        passDict = {
                    "#": self.count,
                    "Value": words
                }
        
        self.passwords.append(passDict)
        self.count+=1
        
        return passDict
    
    def display_list(self):
        """
        This method will be used to return the values within the passwords list
        
        Return:
            userPass (list): Returns a list of user's passwords based on the attribute passwords (list)
        """
        
        userPass = self.passwords
        
        return userPass
    

class Checker(Password):
    """
    Agrs:
        tryPassword: User's input for the password they want to check
    This class Checker() will check the passwords given and indicate whether
    they are valid or not. 
    """
    def __init__(self, tryPassword):
        """
        """
        
        #An empty list that will store passwords that pass the check
        self.good_passwords_list = []
        self.tryPassword = tryPassword
        
    def word_check(self):
        """
        """
        reSymbols = re.compile('[^0-9a-zA-Z]+')
        reDigits = re.compile('[A-Z]+')
        reNums = re.compile('[0-9]+')
        
        #Will test
        if len(self.tryPassword) >= 8 and len(self.tryPassword) < 12:
            print("\nThis password type is short")
        elif len(self.tryPassword) >= 12 and len(self.tryPassword) < 16:
            print("\nThis password type is medium")
        elif len(self.tryPassword) > 16:
            print("\nThis password type is long")
        else:
            print("\nThis password is too short. Your password must atleast be 8 characters long.")
            
        #Checkss to see if the password contains a special character
        if reSymbols.search(self.tryPassword):
            print("This password contains special characters")
        else:
            print("This password does not contain special characters")
        #Checks to see if the password contains a capital letter
        if reSymbols.search(self.tryPassword):
            print("This password contains capital letters")
        else:
            print("This password does not contain capital letters")
        #Checks to see if the password contains a number
        if reNums.search(self.tryPassword):
            print("This password contains numbers")
        else:
            print("This password does not contain numbers")
            
        #Will print this message if all three conditions for a valid password have been satisfied
        if reSymbols.search(self.tryPassword) and reSymbols.search(self.tryPassword) and reNums.search(self.tryPassword) and len(self.tryPassword) > 8:
            print("\nThis password is valid to use!")
            self.good_passwords_list.append(self.tryPassword)
        
        
    def display_good_password(self):
        """
        """
        #Will store the good password into the appropriate list
        goodPass = []
        
        for x in self.good_passwords_list:
            goodPass.append(x)
        
        return goodPass
        
        
class Generator(Password):
    """
    This class will generate random passwords for the user, using
    the "generate" method to accomplish this.
    """
    def __init__(self):
        """
        The __init__() will store passwords created from generate()
        method into a list.
        """
        self.generated_password_list = []
        
    def generate(self, password_type):
        """
        Agrs:
            password_type (string): A string representing the user's input
            for password (short, medium or long)

            
        The generate() method take in a value "password_type", which is
        a string that represent how long the password will be based on
        input (short, medium, long). Depending on the answer, a password 
        will be generated using capital letters, lowercase letters, numbers
        and sybmols. Once this is done, the complete password will be stored
        into "generated_password", which is then appended to the list
        created in the __init__()
        
        Return:
            pass_str (string): String containing the randomly generated password
        """
        symbols_list = "$%_+*)#^!(&@"
        generated_password = ""
        
        if password_type == "short":
            capital_letters = random.choices(string.ascii_uppercase, k = 1)
            lowercase_letters = random.choices(string.ascii_lowercase, k = 3)
            numbers = random.choices(string.digits, k = 3)
            symbols = random.choices(symbols_list, k = 1)
            
            generated_password = capital_letters + lowercase_letters + numbers + symbols
            
        elif password_type == "medium":
            capital_letters = random.choices(string.ascii_uppercase, k = 2)
            lowercase_letters = random.choices(string.ascii_lowercase, k = 4)
            numbers = random.choices(string.digits, k = 3)
            symbols = random.choices(symbols_list, k = 3)
            
            generated_password = capital_letters + lowercase_letters + numbers + symbols
            
        elif password_type == "long":
            capital_letters = random.choices(string.ascii_uppercase, k = 3)
            lowercase_letters = random.choices(string.ascii_lowercase, k = 5)
            numbers = random.choices(string.digits, k = 4)
            symbols = random.choices(symbols_list, k = 4)
            
            generated_password = capital_letters + lowercase_letters + numbers + symbols
            
        else:
            print("You must input 'short', 'medium', or 'long' into the generate function")
            
        pass_str = ''.join(generated_password)
        
        self.generated_password_list.append(pass_str)
        
        return pass_str


def main():
    """
    The main function will display a prompt for the user to select what function they
    want to use. Based on their selection (1,2 or 3), the program will either
    store a passed in password using the Password class, check a passed in password
    using the Checker class, or generate a random password using the Generator class.
    """
    user_data = int(input("Select option to use our program \n 1. Store Password \n 2. Check Password \n 3. Generate Password: "))
    
    newPass = Password()
    newGen = Generator()
    
    if user_data == 1:
        length_pass = int(input("How many passwords do you want to store? (Numeric): "))
        
        for x in range(length_pass):
            testNewPass = newPass.store_password(input("Enter password you wish to store: "))
            print(testNewPass)
        
        viewList = input("\nDo you want to view your password list? (Yes or No): ")
        
        if viewList == "Yes" or viewList == "yes":
            displayPass = newPass.display_list()
            print("\nPASSWORDS LIST: \n \n", displayPass)
        
    elif user_data == 2:
        length_good = int(input("How many passwords do you want to check? (Numeric): "))
        
        for x in range(length_good):
            newCheck = Checker(input("Enter the password you wish to check: "))
            wordCheck = newCheck.word_check()
        
        viewGood = input("\nDo you want to view your good passwords? (Yes or No): ")
        
        if viewGood == "Yes" or viewGood == "yes":
            displayGoodPass = newCheck.display_good_password()
            print(displayGoodPass)
        

    elif user_data == 3:
        testNewGen = newGen.generate(input("Enter password type (short, medium, long): "))
        print("Your generated password is " + testNewGen)
    
    elif user_data !=1 or user_data !=2 or user_data !=3:
        print("You must enter 1, 2 or 3")


if __name__ == '__main__':
    """
    This class calls the main() method to execute the prompt/commands for our program.
    """
    main()