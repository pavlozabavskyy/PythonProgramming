from Observer import Observer

class Event:

    @staticmethod
    def do_some(methodName: str, data) -> None:
        try:
            Observer.observers[methodName](methodName, data)
        except Exception as e:
            raise e
        