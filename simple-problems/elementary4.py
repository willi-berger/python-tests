'''
Write a program that asks the user for a number n and
prints the sum of the numbers 1 to n
'''

try:
    n = input("Please input a number:")
    print(n)
    n = int(n)
    for i in range(1, n+1):
        print(i)
    print("Joined: " + ', '.join((str(i) for i in range(1, n+1))))

    sum =  0
    for i in range(n+1):
        sum = sum + i


    print(sum)

    print("directly with Gauss formula:",  (n*(n+1)//2))
          
except ValueError:
    print("ValueError  occured")
#except:
#    print("Something else happened")    
    
