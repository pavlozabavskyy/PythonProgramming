
def factor(n):
    if n == 0:
        return 1
    return factor(n-1) * n

def permutation(n, k):
    temp, i = 0.0, 0
    while i <= n - k:
        temp += float((-1)**i) / float(factor(i))
        i += 1
    return factor(n) / factor(k) * temp

def numberOfPermutations():
    while True:
        try:
            n = int(input("Enter n (1 <= n <= 9) : "))
            k = int(input("Enter n (1 <= k <= n) : "))
            if n < 1 or n > 9:
                raise Exception("Incorrect N ")
            elif k < 1 or k > n:
                raise Exception("Incorrect K ")
            else:
                result = permutation(n, k)
                print "Number of permutations with N = ", n, " and K = ", k, "  -  ", result
                break
        except Exception as e:
            print e

numberOfPermutations()











