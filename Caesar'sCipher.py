

def caesar_cipher(x,y):
    import string
    returnstring = ""
    x = x.lower()
    for i in x:
        if string.ascii_lowercase.find(i) != -1:
            letter = ((string.ascii_lowercase.find(i)) + y) 
            while letter > 25:
                letter = letter - 26
            while letter < 0:
                letter = letter + 26
            returnstring = returnstring + string.ascii_lowercase[letter]
        
        else : #string.ascii_lowercase.find(i) == -1:
            if string.digits.find(i) != -1:
                number = ((string.digits.find(i)) + y)
                while number > 9:
                    number = number - 10
                while number < 0:
                    number = number + 10 
                returnstring = returnstring + string.digits[number]
                
            else:
                returnstring = returnstring + i
    
    return returnstring

 
# example testcase:  print(caesar_cipher("Hello World!", 7))


"""
Caesar's Cipher:
    
Define a function caesar_cipher, which takes two arguments:

a string containing a string to be encrypted, and
an integer representing the "shift" value.

caesar_cipher should return a string representing the encrypted form of the input string.

Slight variations on this technique exist, but in our version we will:

shift letters as described above (after converting upper-case letters 
in the input string to lower-case),
add the shift value to numeric characters in the input string 
(wrapping around to 0 if we get beyond 9), and
leave all other characters unchanged in the resulting string
    
    
Created on Wed Jan 16 15:16:29 2019
@author: skylargordon
"""

