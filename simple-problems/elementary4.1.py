'''
Write a program that asks the user for a number n and prints the sum of the numbers 1 to n
'''

try:
    n = input("Please input a number:")
    print(n)
    n = int(n)
    for i in range(1, n+1):
        print(i)
except ValueError:
    print("Some exc occured")
    
