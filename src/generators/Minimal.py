from .AbstractDotGenerator import AbstractDotGenerator

class Minimal(AbstractDotGenerator):

    def __init__(self, data): 
        super().__init__(data)

    def before(self):
        return (
            "   splines=false;\n"
            "   node [shape=point];\n"
            "   edge [dir=none]\n"
            )
