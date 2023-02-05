# generate permutations
# source: https://mathsanew.com/articles/permutations_with_recursion.pdf

n = 3
a = list(range(1, n+1))
print(a)
print('---')

def generate(s):
    if s == n - 1:
        print(a)
        return
    for i in range(n-s):
        if i > 0:
            # SWAP(s,s+i)
            a[s], a[s+i] = a[s+i], a[s]
        generate(s+1)

        if i > 0:
            # SWAP(s, s+i)
            a[s], a[s+i] = a[s+i], a[s]
            

generate(0)


