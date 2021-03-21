'''
4. Write a program that asks the user for a number n and
prints the sum of the numbers 1 to n
5. Modify the previous program such that only multiples of
three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17
'''

def sumoflist(ll):
    print(ll.__class__)
    s = 0
    for i in ll:
        s = s + i
    return s

def isMultipleOfOneOf(i, ll):
    for j in ll:
        if i % j == 0:
            return True
    return False

def sumOfMultiplesInList(ll, l2):
    s = 0
    for i in ll:
        if isMultipleOfOneOf(i, l2):
            s = s + i
    return s
        

try:
    n = input("Please input a number:")

    n = int(n)
    print("Joined: " + ', '.join((str(i) for i in range(1, n+1))))

    sum =  0
    for i in range(n+1):
        sum = sum + i

    print('sum is {}'.format(sum))
    print("directly with Gauss formula:",  (n*(n+1)//2))
    ll = list(range(n+1))
    print(ll)

    print('pass list: sum with fun {} '.format(sumoflist(ll)))

    ll = range(n+1)
    print(ll)

    print('pass generator: sum with fun {}'.format(sumoflist(ll)))

    ll2 = (3, 5)
    print('sum of multiples of {} is: {}'.format(','.join(str(l) for l in ll2), sumOfMultiplesInList(ll, ll2)))


          
except ValueError:
    print("ValueError  occured")
#except:
#    print("Something else happened")    
    
