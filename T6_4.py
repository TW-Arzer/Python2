

class Observable:

    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_all(self, message):
        for observer in self._observers:
            observer.update(message)


class Observer:

    def update(self, message):
        pass


class Tabloid(Observer):

    def __init__(self, nom: str):
        super().__init__()
        self.__nom = nom

    def update(self, message):
        print(f"[{self.__nom}] Scoop! '{message}'")
