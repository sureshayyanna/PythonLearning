# Program to write Fibonacci series for given number
"""
Fibonacci series :   0,1,1,2,3,5,8,13,21.....
"""
n1 = 0
n2 = 1
num = int(input("Enter the number:"))

print(n1)
print(n2)

for i in range (2, num):
    sum =n1 + n2
    print (sum)
    n1 = n2
    n2 = sum