from .Degradation import Degradation
from .colors import GREEN, WHITE, RED, scale, get_color_between, as_hex

class CenteredDegradation(Degradation):

    def __init__(self, data): 
        super().__init__(data)

        self.best_obj = None
        for entry in data:
            if entry.event == "3" and (self.best_obj is None or self.best_obj > entry.value):
                self.best_obj = entry.value

    def get_node_fillcolor(self, entry):

        if self.best_obj is None:
            return Degradation.get_node_fillcolor(entry)

        if entry.value <= self.best_obj:
            score = scale(entry.value, self.min, self.best_obj)
            rgb = get_color_between(WHITE, GREEN, score)
            return as_hex(rgb)
        
        score = scale(entry.value, self.best_obj, self.max)
        rgb = get_color_between(GREEN, RED, score)

        return as_hex(rgb) 

