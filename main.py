import math

MAX = 10000

primes = []

def sieveSundaram():
    marked = [0] * ((MAX / 2) + 100)
    i = 1
    while i <= ((math.sqrt(MAX) - 1) / 2):
        j = (i * (i + 1)) << 1
        while j <= MAX / 2:
            marked[j] = 1
            j = j + 2 * i + 1
        i = i + 1
    primes.append(2)

    i = 1
    while i <= MAX / 2:
        if marked[i] == 0:
            primes.append(2 * i + 1)
        i = i + 1

def isSmith(n):
    originalNo, pDigitSum, i = n, 0, 0

    while (primes[i] <= n / 2):
        while n % primes[i] == 0:
            p = primes[i]
            n = n / p
            while p > 0:
                pDigitSum += (p % 10)
                p = p / 10
        i = i + 1

    if not n == 1 and not n == originalNo:
        while n > 0:
            pDigitSum = pDigitSum + n % 10
            n = n / 10

    sumDigits = 0
    while originalNo > 0:
        sumDigits = sumDigits + originalNo % 10
        originalNo = originalNo / 10

    return pDigitSum == sumDigits

def SN( n ):
    print("!________________TASK_1________________!")
    sieveSundaram()
    i, j, = 0, 1
    while i < n:
        if isSmith(j):
            print j,
            i += 1
        j+=1



n = int(input('Enter N value: '))

SN(n)

