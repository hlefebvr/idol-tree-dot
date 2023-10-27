from abc import abstractclassmethod
from .AbstractGenerator import AbstractGenerator

class AbstractDotGenerator(AbstractGenerator):

    def __init__(self, data):
        super().__init__(data)

    def before(self): None

    def get_node_label(self, entry): None

    def get_node_color(self, entry): None

    def get_node_fillcolor(self, entry): None

    def get_node_shape(self, entry): None 

    def get_edge_label(self, entry): None

    def after(self): None

    def build(self, filename):
            
        with open(filename, "w") as dot_file:

            dot_file.write("digraph G {\n")

            before = self.before()
            if before is not None: dot_file.write(before)

            for entry in self.data:

                node_label = self.get_node_label(entry)
                node_color = self.get_node_color(entry)
                node_fillcolor = self.get_node_fillcolor(entry)
                node_shape = self.get_node_shape(entry)

                node_args = []

                if node_label is not None: node_args += [f'label=<{node_label}>']
                if node_color is not None: node_args += [f'color=<{node_color}>']
                if node_shape is not None: node_args += [f'shape={node_shape}']
                if node_fillcolor is not None: node_args += [f'fillcolor=<{node_fillcolor}>']

                dot_file.write(f'   {entry.node_id}')
                if len(node_args) > 0: dot_file.write("[" + ', '.join(node_args) + "]")
                dot_file.write(';\n')
                
                if entry.node_id == 0: continue
                
                edge_label = self.get_edge_label(entry)

                edge_args = []

                if edge_label is not None: edge_args += [f'[label="{edge_label}"]']
                
                dot_file.write(f"   {entry.parent_id} -> {entry.node_id}")
                if len(node_args) > 0: dot_file.write("[" + ', '.join(edge_args) + "]")
                dot_file.write(";\n")

            after = self.after()
            if after is not None: dot_file.write(after)

            dot_file.write("}")

