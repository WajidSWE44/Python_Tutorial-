# Expression Execution

# String & Numeric values can operate togather with * 
A, B = 2, 3
Txt = "@"
print(2 * Txt * 3)

# String & String can Operate With +
A , B = "2",3
Txt = "@"
print((A + Txt)* 3)

#Numeric Values can operate with all Arithmetic operators
A, B = 2, 3
C = 4
print( A+B*C)

# Arithmetic expression with Integer and Float will result in float 
A , B = 10 ,5.0
C = A * B
print(C)

# Result of Divion Operator with two integers will be Float
A , B = 1,2
C = A/B
print(C)

# Integer Divion with Float and Int will give int displayed as Float
A,B = 1.5,3
C = A//B
print(C , A/B)

#Floor give closest integer ,which is lesser than or equal to the float value
#Result of (A//B) is same as floor (A/B)
#floor: It's not just the "closest" number; it always rounds down to the nearest whole number.
#For example:⌊3.7⌋=3, ⌊−2.3⌋=−3 .It "rounds down" even for negative numbers.
A ,B = 12 , 5
C= A//B
print(C,A/B)

A ,B = -12 , 5
C= A//B
print(C,A/B)

A ,B = 12 , -5
C= A//B   #integer devision
print(C,A/B)

#Remainder is negative when denominator is negative
A ,B = 5 , 2
C= A%B
print(C)# Answer is positive (1)

A ,B = -5 , -2
C= A%B
print(C)# Answer is negative (-1)

A ,B = -5 , 2
C= A%B
print(C)# Answer is positive (1)

A ,B = 5 , -2
C= A%B
print(C)# Answer is negative (-1)


