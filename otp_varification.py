import math
import random
import smtplib

digits = "0123456789"
OTP = ""
for i in range(6):
    OTP += digits[math.floor(random.random() * 10)]
otp = OTP + " is your OTP"
msg = otp

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("anandrajpatel134@gmail.com", "baslhoyvmczcufob")
emailid = input("Enter your email :- ")
s.sendmail('&&&&&&&&&&&', emailid, msg)
a = input("Enter your OTP :- ")
if a == OTP:
    print("OTP Verified")
else:
    print("Sorry OTP is not match")
