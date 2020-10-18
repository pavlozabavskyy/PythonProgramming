
def sumD(n):
    sumDigits = 0
    while n > 0:
        sumDigits = sumDigits + n % 10
        n = n / 10
    return sumDigits


def isSmith(n):
    i, number, sum1, temp = 2, n, 0, 0
    while i < number:
        if number % i == 0:
            temp += 1
            sum1 += sumD(i)
            number /= i
        else:
            i += 1
    if temp == 0:
        sum1 = 0
    else:
        sum1 += sumD(number)

    return sum1 == sumD(n)


def SmithNumber():
    while True:
        try:
            n = int(input("Enter n (n > 0) : "))
            if n < 1:
                raise Exception()
            else:
                i, j = 2, 0
                while j < n:
                    if isSmith(i):
                        print i,
                        j += 1
                    i += 1
            break
        except Exception as e:
            print('Number < 0 =( ')

SmithNumber()
