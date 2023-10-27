from .AbstractDotGenerator import AbstractDotGenerator
from .colors import WHITE, GREEN, scale, get_color_between, as_hex

class Debug(AbstractDotGenerator):

    def __init__(self, data): 
        super().__init__(data)

        self.min = -1e20
        self.max = +1e20
        for entry in data:
            if entry.event != "3": continue 
            if self.max < entry.value: self.max = entry.value
            if self.min > entry.value: self.min = entry.value

    def before(self):
        return (
            "   splines=false;\n"
            "   node [shape=none, style=filled];\n"
            "   edge [dir=none]\n"
            ) 

    def get_node_label(self, entry):
        
        color = "white"
        
        if entry.event == "3": color = as_hex(get_color_between(WHITE, GREEN, scale(entry.value, self.min, self.max)))
        elif entry.event == "1": color = "red"

        return (f'<table cellspacing="0">'
                f'<tr><td colspan="2" bgcolor="{color}">{entry.node_id}</td></tr>'
                f'<tr><td bgcolor="#efefef">{entry.status}</td><td bgcolor="#efefef">{entry.value}</td></tr>'
                f'</table>')
        
    def get_edge_label(self, entry):
        return entry.branching