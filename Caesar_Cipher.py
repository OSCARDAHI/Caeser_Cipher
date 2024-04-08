last_char_code = ord("Z")
first_char_code = ord("A")
char_range = last_char_code - first_char_code + 1

#define a function to encrypt a message
def Encryption (message,cipher_key):
  
  cipher_message = ""
#looping through each characters in message
  for char in message.upper():
    if char.isalpha():
     #convert charachters to ASCII code
     char_code = ord(char)
     new_char_code= char_code + cipher_key
     if new_char_code > last_char_code :
        new_char_code -= char_range
     if new_char_code < first_char_code:
       new_char_code += char_range
     new_char =chr(new_char_code)
     cipher_message += new_char 
    else:
     cipher_message = cipher_message + char
  return cipher_message

user_message = input("Enter your message:")
user_key = int(input("Enter cipher key:"))

# call encryption function
Encrypted_Message =Encryption (user_message,user_key)
print (f"Encrypted_Message:{Encrypted_Message}")


def Decryption (message,cipher_key):
  
  cipher_message = ""
#looping through each characters in message
  for char in message.upper():
    if char.isalpha():
     #convert charachters to ASCII code
     char_code = ord(char)
     new_char_code= char_code - cipher_key
     if new_char_code > last_char_code :
        new_char_code -= char_range
     if new_char_code < first_char_code:
       new_char_code += char_range
     new_char =chr(new_char_code)
     cipher_message += new_char 
    else:
     cipher_message = cipher_message + char
  return cipher_message

user_message = input("Enter your message:")
user_key = int(input("Enter cipher key:"))

# call decryption function
Decrypted_Message =Decryption(user_message,user_key)
print (f"Decrypted_Message:{Decrypted_Message}")