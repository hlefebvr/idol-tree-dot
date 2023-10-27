from .AbstractDotGenerator import AbstractDotGenerator
from .colors import LIGHTBLUE, RED, scale, get_color_between, as_hex

class Degradation(AbstractDotGenerator):

    def __init__(self, data): 
        super().__init__(data)

        self.min = 1e20
        self.max = -1e20
        for entry in data:
            if entry.node_id == 0: 
                self.min = entry.value
            if entry.value < 1e20 and self.max < entry.value: 
                self.max = entry.value

    def before(self):
        return (
            "   splines=false;\n"
            "   node [shape=ellipse, style=filled];\n"
            "   edge [dir=none]\n"
            ) 

    def get_node_fillcolor(self, entry):

        score = scale(entry.value, self.min, self.max)
        rgb = get_color_between(LIGHTBLUE, RED, score)
        
        return as_hex(rgb) 

    def get_node_shape(self, entry):
        return "diamond" if entry.event == "1" else None
