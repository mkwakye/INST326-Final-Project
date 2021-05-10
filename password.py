import string
import random
import sys
import argparse

"""
Assignment: Final Project Class 3

Members: Aaron Methratta
         Michael Kwakye
         Biruk Tamiru

"""
class Password():
    """
    This class will take in passwords from the user's input and 
    store them into a list of passwords. The method "pass_length"
    will return the length of the list.
    """
    pass
class Checker():
    """
    This class will check the passwords given and indicate whether
    they are valid or not. 
    """
    pass
class Generator():
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
        The generate() method take in a value "password_type", which is
        a string that represent how long the password will be based on
        input (short, medium, long). Depending on the answer, a password 
        will be generated using capital letters, lowercase letters, numbers
        and sybmols. Once this is done, the complete password will be stored
        into "generated_password", which is then appended to the list
        created in the __init__()
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
    
    newGen = Generator()
    
    if user_data == 1:
        pass
    if user_data == 2:
        pass
    if user_data == 3:
        testNewGen = newGen.generate(input("Enter password type (short, medium, long): "))
        print("Your generated password is " + testNewGen)
    else:
        print("You must enter 1, 2 or 3")

if __name__ == '__main__':
    """
    This class calls the main() method to execute the prompt/commands for our program.
    """
    main()