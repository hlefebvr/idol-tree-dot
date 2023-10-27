from .AbstractDotGenerator import AbstractDotGenerator
from .colors import RED, GREEN, scale, get_color_between, as_hex

class Infeasible(AbstractDotGenerator):

    def __init__(self, data): 
        super().__init__(data)

        self.min = 0
        self.max = 0
        for entry in data:
            if entry.sum_of_infeasibilities < 1e20 and self.max < entry.sum_of_infeasibilities: 
                self.max = entry.sum_of_infeasibilities

    def before(self):
        return (
            "   splines=false;\n"
            "   node [shape=ellipse, style=filled];\n"
            "   edge [dir=none]\n"
            ) 

    def get_node_fillcolor(self, entry):

        if entry.sum_of_infeasibilities >= 1e20: return "white"

        score = scale(entry.sum_of_infeasibilities, self.min, self.max)
        rgb = get_color_between(RED, GREEN, score)
        
        return as_hex(rgb) 

    def get_node_shape(self, entry):
        return "diamond" if entry.event == "1" else None
