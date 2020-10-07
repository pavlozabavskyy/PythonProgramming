import funcSm as func



def generate(n):
    current = 3
    while current < n:
        while not func._isSmith(current):
            current +=1
        yield current
        current += 1
