
class Logger:
    
    def log(methodName: str, data):
        if data[3] == 'l1':
            fileName = 'logs1.txt'
        else:
            fileName = 'logs2.txt'
        with open(fileName, 'a') as f:
            f.write('\nMethod - {} ( {}, {}, {} )'.format(methodName, data[0], data[1], data[2]))


        

