# CaesarCipher

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
