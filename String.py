# Strings

a = 'Hello Dear'                   #slicing string
print(a[2:8])
print(a[:9])
print(a[4:])
print(a[-5:-8])



a = '  nothng is better than python!!!!   '
print(a.upper())                                
print(a.lower())                                    #modify string
print(a.strip())
print(a.split('i'))
print(a.replace("p","P"))

A = 'MY '
B = 'NAME '                                #concatenation
C = 'IS '
D = 'DOLLY'

print(A+B+C+D)

age = 24                                      #format()
bfor = 23
form = ('I am {} years old and my age before was {}')    
print(form.format(age,bfor))

print("I have studied at \'OIET\'")           #use of escape character
