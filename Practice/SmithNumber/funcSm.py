
def primeDiv(n):
    i, a = 2, n
    div = []
    while i < a:
        if a % i == 0:
            div.append(i)
            a /= i
        else:
            i += 1
    div.append(a)
    return div

def sumD(n):
    sum = 0
    while n > 0:
        dig = n % 10
        sum += dig
        n = n // 10
    return sum

def isSmith(n):
    div = primeDiv(n)
    sumOfNum = 0
    for i in div:
        if len(div) > 1:
            sumOfNum += sumD(i)

    return sumOfNum == sumD(n)


def funcNum(n = 1):
    i, current = 0, 3
    list = []
    while i < n:
        if isSmith(current):
            list.append(current)
            i +=1
        current+=1
    return list
