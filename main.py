#EXPRESSION EXECUTION

# .STRING & numeric value can operate together with *

a = 2,
b = 3,
Txt = "@"
print (2*Txt*3)            #@@@@@@

# .String & String can operate with +

a = "2"
b = 3
Txt = "@"
print ((a+Txt)*b)          #2@2@2@   string + string = concatination 

# .Numeric val can operate with all arithematic operators

a,b = 2,3
c=4
print(a+b*c)                #14

# .Arithematic expression with integer and float will result in float

a,b = 10,5.0
c = a*b
print (c)                   #50.0

# .Result of division operator with two integers will be float

a,b = 1,2
c = a/b
print (c)                   #0.5

# .Integer division (//) with float and int will give int displayed as float.

a,b = 1.5,3
c = a//b
print (c)                    #0.0
print (a/b)                  #0.5

