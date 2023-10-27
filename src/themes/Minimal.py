class Minimal:

    def __init__(self, input_data):
        pass

    def before(self): 
        return (
            "   splines=false;\n"
            "   node [shape=point];\n"
            "   edge [dir=none]\n"
            ) 

    def after(self): return ""

    def node_label(self, node_id, parent_id, status, value, branching, event, sum_of_infeasibilities): return None

    def node_color(self, node_id, parent_id, status, value, branching, event, sum_of_infeasibilities): return None

    def edge_label(self, node_id, parent_id, status, value, branching, event, sum_of_infeasibilities): return None