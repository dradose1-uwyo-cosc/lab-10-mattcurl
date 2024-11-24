# Matthew Curl
# UWYO COSC 1010
# 11/24/2024
# Lab 10
# Lab Section: 13
# Sources, people worked with, help given to: Braeden Kirby

#import modules you will need 

from hashlib import sha256 
from pathlib import Path
# given function that will translate a string to a hash to check against later
def get_hash(to_hash):
    """You can use """
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()



# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.

#prepare paths for both files
file_path = Path('hash')
rockyou_path = Path('rockyou.txt')


# - Read in the value stored within `hash`.
#   - You must use a try and except block.

# have a try except block check if the file is there
try:
    # if so, open and read the file and strip it to make sure it can be compared later
    hash_file = file_path.open('r') 
    hash_password = hash_file.read().strip()
except:
    print('The nessecary file was not found')
    

# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.

# have another try except block to check for the second nessecary file
try:
    #if the file exists, open and read the lines(so that it doesn't come out as one big string)
    rockyou_file = rockyou_path.open('r')
    pos_passwords = rockyou_file.readlines()
        
except:
    print('The nessecary file was not found')
    
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.

# make a loop that will go through all the lines of the rock you text
for password in pos_passwords:
    # strip the password so that it doesn't have unessecary spaces
    password = password.strip()
    # use the given get hash function to get the hash of the possible password
    hashed_password = get_hash(password)
    # have an if statement check if the passwords match
    if hashed_password == hash_password:
        # if so, print off the text version of the password that was correct
        print(f"Password was: {password}")
        break
        