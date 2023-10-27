from abc import abstractclassmethod
from .AbstractGenerator import AbstractGenerator

class TexGenerator(AbstractGenerator):

    def __init__(self, data):
        super().__init__(data)
        
        self.scaling_factor = 10

        self.min_infeas = 0
        self.max_infeas = 0
        self.min_obj = -1e15
        self.best_obj = +1e15
        self.best_node = None
        self.max_obj = -1e20

        for entry in data:

            if entry.sum_of_infeasibilities >= 1e15: continue
            if entry.value >= 1e15: continue

            if self.max_infeas < entry.sum_of_infeasibilities: 
                self.max_infeas = entry.sum_of_infeasibilities
            if entry.node_id == 0:
                self.min_obj = entry.value
            if entry.value > self.max_obj:
                self.max_obj = entry.value
            if entry.event == "1" and self.best_obj > entry.value:
                self.best_obj = entry.value
                self.best_node = entry.node_id

        if self.best_node is None:
            raise Exception("Cannot make plot if no feasible point has been found.")

    def get_point(self, entry):
        y = (entry.value - self.min_obj) / (self.max_obj - self.min_obj) * self.scaling_factor
        x = (entry.sum_of_infeasibilities - self.min_infeas) / (self.max_infeas - self.min_infeas) * self.scaling_factor
        return (x, y)

    def build(self, filename):
            
        with open(filename, "w") as tex_file:

            tex_file.write("\\documentclass{standalone}\n")
            tex_file.write("\\usepackage{tikz}\n")
            tex_file.write("\\begin{document}\n")

            tikz_code = self.generate_tikz_code()
            tex_file.write(tikz_code)

            tex_file.write("\\end{document}\n")


    def generate_tikz_code(self):
        tikz_code = "\\begin{tikzpicture}[bullet/.style={circle, fill, minimum size=2pt, inner sep=0pt, outer sep=0pt}]\n"

        out = {}

        for entry in self.data:
            if entry.level < 0: 
                continue
            if entry.sum_of_infeasibilities >= 1e15: 
                out[entry.node_id] = None
                continue
            point = self.get_point(entry)
            tikz_code += "\\node[bullet] (node" + str(entry.node_id) + ") at (" + str(point[0]) + ", " + str(point[1]) + ") {};\n"

        for entry in self.data:
            if entry.node_id == 0: continue
            if entry.level < 0: continue
            if entry.node_id in out: continue
            tikz_code += "\\draw (node" + str(entry.parent_id) + ") -- (node" + str(entry.node_id) + ");\n"

        tikz_code += "\\draw[<->] (0, 11) |- (11, 0);\n"

        tikz_code += "\\draw[white] (-1, 12) |- (12, -1);\n"

        tikz_code += "\\node[below] at (node0) {C};\n"
        tikz_code += "\\node[left] at (node" + str(self.best_node) + ") {I};\n"

        tikz_code += "\\end{tikzpicture}\n"

        return tikz_code

