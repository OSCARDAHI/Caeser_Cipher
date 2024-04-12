import re

def password_strength (password):
    length= len(password)
    score=0
    if 8 <= length <= 12:
        score+=1
    elif 13 <= length <=16:
        score +=2
    elif length >16:
        score+=3
    if re.search(r"[A-Z]",password):
        score+=1
    if re.search(r"[a-z]",password):
        score+=1
    if re.search(r"[0-9]",password):
        score+=1
    if re.search(r"[!@$%&-_^#* ]",password):
        score +=1
  

    if 0<score<=3:
        print ("Password is weak")
    elif 3 <score<=5:
        print("Password is medium")
    elif 5 <score<=7:
        print ("Password is strong")

    return score

user_password=input("Enter your password:")
password_strength(user_password)
