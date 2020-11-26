
class Smith():
    def __primeDiv(self, n):
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

    def __sumD(self, n):
        sum = 0
        while n > 0:
            digit = n % 10
            sum += digit
            n = n // 10
        return sum

    def __isSmith(self, n):
        div = self.__primeDiv(n)
        sumOfNum = 0
        for i in div:
            if len(div) > 1:
                sumOfNum += self.__sumD(i)

        return sumOfNum == self.__sumD(n)

    
    def __init__(self, index = 4):
        self.num = index

    def __iter__(self):
        return self

    def __next__(self):
        num = self.num
        current = num + 1
        while self.__isSmith(current) == False:
            current += 1
        self.num = current
        return num