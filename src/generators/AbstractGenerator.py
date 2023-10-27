from abc import abstractclassmethod

class AbstractGenerator:

    def __init__(self, data):
        self.data = data

    @abstractclassmethod
    def build(self, filename): pass
