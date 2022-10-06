#email validation in python (using regEx)
 # condition  (a-z)  (0-9)    ( . _ @ time in 1) (pos . 2,3)
# starting letter is always alpha, show use the  ^ op starting value
#\ => uses char searching for string  
# ? => at time one  hi hona chiye work  0 ya 1
# group of char a-z and 0-9 alg bhi  de skte ya sth mein bhi
#\w use for searching particular char in str
#kisi particular pos pe searching krni hai to use{}
 #searching back se ho to $
import re
# email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,5}$"
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+(\.[A-Z|a-z]{2,})+"
user_email=input("enter your email : ")
#use this regex fun for matching the condition to input 
if re.search(email_condition,user_email):
     print("email is valid")
else:
    print("wrong email")     