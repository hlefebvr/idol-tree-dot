class Degradation:

    def __init__(self, input_data):
        
        self.min_color = (0, 0, 255)
        self.best_color = (0, 255, 0)
        self.max_color = (255, 0, 0)

        self.root_node_value = None
        self.max_value = None
        self.best_obj = None

        for node_id, parent_id, status, value, branching, event, sum_of_infeasibilities in input_data:
            if (node_id == "0"): self.root_node_value = float(value)
            if (self.max_value is None or float(value) > self.max_value): self.max_value = float(value)
            if (event == "3" and (self.best_obj is None or float(value) < self.best_obj)): self.best_obj = float(value)


    def before(self): 
        return (
            "   splines=false;\n"
            "   node [shape=ellipse, style=filled];\n"
            "   edge [dir=none]\n"
            ) 

    def after(self): return ""

    def node_label(self, node_id, parent_id, status, value, branching, event, sum_of_infeasibilities): 
        return node_id

    def get_score(self, min, max, value):
        return (value - min) / (max - min + 1e-10)

    def get_color(self, color1, color2, score):

        r1, g1, b1 = color1
        r2, g2, b2 = color2
        r = int(r1 + (r2 - r1) * score)
        g = int(g1 + (g2 - g1) * score)
        b = int(b1 + (b2 - b1) * score)

        return "#{:02x}{:02x}{:02x}".format(r, g, b)

    def node_shape(self, node_id, parent_id, status, value, branching, event, sum_of_infeasibilities):
        if event == "3": return "square"
        return None

    def node_color(self, node_id, parent_id, status, value, branching, event, sum_of_infeasibilities):

        if value == "Inf": 
            return "#{:02x}{:02x}{:02x}".format(self.max_color[0], self.max_color[1], self.max_color[2])

        value = float(value)

        if self.best_obj is None:
            score = self.get_score(self.root_node_value, self.max_value, value)
            return self.get_color(self.min_color, self.max_color, score)

        if value <= self.best_obj:
            score = self.get_score(self.root_node_value, self.best_obj, value)
            return self.get_color(self.min_color, self.best_color, score)

        score = self.get_score(self.best_obj, self.max_value, value)
        return self.get_color(self.best_color, self.max_color, score)

    def edge_label(self, node_id, parent_id, status, value, branching, event, sum_of_infeasibilities): return None