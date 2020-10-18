import funcSm as fun

def generate(n):
    num = 0
    current = 3
    while True:
        if num == n:
            break
        while not fun.isSmith(current):
            current +=1
        yield current
        current +=1
        num+=1
