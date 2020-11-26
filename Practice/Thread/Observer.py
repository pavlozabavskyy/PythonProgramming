
class Observer:
    
    observers = dict()

    @staticmethod
    def attach(methodName: str, callback) -> None:
        Observer.observers[methodName] = callback

