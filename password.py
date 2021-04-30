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
    pass
class Checker():
    pass
class Generator():
    def __init__(self):
        #Another class that has not been completed/worked on yet
        self.generated_password_list = []
        
    def generate(self, password_type):
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
    user_data = int(input("Select option to use our program \n 1. Store Password \n 2. Check Password \n 3. Generate Password: "))
    
    newGen = Generator()
    
    if user_data == 1:
        pass
    if user_data == 2:
        pass
    if user_data == 3:
        testNewGen = newGen.generate(input("Enter password type (short, medium, long): "))
        print("Your generated password is " + testNewGen)

if __name__ == '__main__':
    main()