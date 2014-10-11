#1
def sumDivs(n):
    p = 0
    if n <= 0:
        return 0
    for i in range(1,n):
       if (n%i == 0):
           p += i
    return (p)
#2
def findAmicable(a,b):
    p = 0
    l = 0
    if a == 0 or b == 0:
        return 0
    for i in range(a,b):
        if sumDivs(i) == i:
                p = i
                l  =sumDivs(i)
    return ((p,l))

#3
def encrypt(ch,num):
    if sumDivs(num) == 0:
        return "Not Valid"
    else:
        p = ord(ch)
        p += sumDivs(num)
        return chr(p)

#4
def decrypt(ch,num):
    if sumDivs(num) == 0:
        return "Not Valid"
    else:
        p = ord(ch)
        p -= sumDivs(num)
        return chr(p)

#5
def encryptMessage(string,num):
    p = ''
    if sumDivs(num) == 0 or string == '':
        return ""

    else:
        p += encrypt(string[0],num)
        return p + encryptMessage(string[1:],num)

#6
def decryptMessage(string,num):
    p = ''
    if sumDivs(num) == 0 or string == '':
        return ""

    else:
        p += decrypt(string[0],num)
        return p + decryptMessage(string[1:],num)
