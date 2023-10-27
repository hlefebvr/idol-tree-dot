from .AbstractDotGenerator import AbstractDotGenerator
from .colors import WHITE, BLUE, scale, get_color_between, as_hex

class Temporal(AbstractDotGenerator):

    def __init__(self, data): 
        super().__init__(data)

        self.min = 0
        self.max = 0
        for entry in data:
            if self.max < entry.time: 
                self.max = entry.time

    def before(self):
        return (
            "   splines=false;\n"
            "   node [shape=ellipse, style=filled];\n"
            "   edge [dir=none]\n"
            ) 

    def get_node_fillcolor(self, entry):

        score = scale(entry.time, self.min, self.max)
        rgb = get_color_between(WHITE, BLUE, score)
        
        return as_hex(rgb) 

    def get_node_shape(self, entry):
        return "diamond" if entry.event == "1" else None