from datetime import datetime


class CollectionMemento:
    def __init__(self, collect):
        self._collect = collect

    @property
    def get_collect(self):
        return self._collect

    @property
    def name(self):
        return f'{self.date} / ({self._collect})'

    @property
    def date(self):
        return str(datetime.now())[:19]
    

    