simppassword = input()
password=''
for x in simppassword:
    if(x == 'i'):
        password += "!"
    elif(x == 'a'):
        password += "@"
    elif(x == 'm'):
        password += "M"
    elif(x == 'B'):
        password += "8"
    elif(x == 'o'):
        password += "."
    else:
        password += x

password += "q*s"
print(password)
