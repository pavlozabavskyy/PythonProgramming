
class Logger:
    def log(methodName: str, data):
        with open('logs.txt', 'a') as f:
            f.write('\nMethod - {}\n  List before: {} \n  Position: {} \n  List after: {} \n '.format(methodName, data[0], data[1], data[2]))
            f.write('_'*60)

        

