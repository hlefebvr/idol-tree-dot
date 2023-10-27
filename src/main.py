import csv
import argparse
from themes.Degradation import Degradation
from themes.BestEstimate import BestEstimate
from themes.Minimal import Minimal
from themes.Info import Info

def read_csv_file(path):
    result = []
    try:
    
        with open(path, "r") as input_file:
            reader = csv.reader(input_file)
            for row in reader:
                if len(row) == 7:
                    result.append(row)
                else:
                    raise IOError(row)
    
    except FileNotFoundError:
        print(f"Input data file '{path}' not found.")
        exit(1)
    
    return result

def generate_dot(input_data, dot_filename, theme):

    with open(dot_filename, "w") as dot_file:
        dot_file.write("digraph G {\n")

        before = theme.before()
        if before is not None:
            dot_file.write(before)

        #dot_file.write("  edge [fontsize=\"10px\"];\n")
        #dot_file.write("  node [shape=none];\n")

        for row in input_data:

            node_id, parent_id, status, value, branching, event, sum_of_infeasibilities = row

            node_label = theme.node_label(node_id, parent_id, status, value, branching, event, sum_of_infeasibilities)
            node_color = theme.node_color(node_id, parent_id, status, value, branching, event, sum_of_infeasibilities)
            node_shape = theme.node_shape(node_id, parent_id, status, value, branching, event, sum_of_infeasibilities)

            node_args = []

            if node_label is not None: node_args += [f'label=<{node_label}>']
            if node_color is not None: node_args += [f'fillcolor=<{node_color}>']
            if node_shape is not None: node_args += [f'shape={node_shape}']

            dot_file.write(f'   {node_id}')
            if len(node_args) > 0: dot_file.write("[" + ', '.join(node_args) + "]")
            dot_file.write(';\n')
            
            if node_id != "0":
                dot_file.write(f"   {parent_id} -> {node_id}")
                edge_label = theme.edge_label(node_id, parent_id, status, value, branching, event, sum_of_infeasibilities)
                if edge_label is not None:
                    dot_file.write(f'[label="{edge_label}"]')
                dot_file.write(";\n")

        after = theme.before()
        if after is not None:
            dot_file.write(after)

        dot_file.write("}")


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="This is a simple converter from idol branch-and-bound tree csv files to dot.\nRefer to https://github.com/hlefebvr/idol.")
    parser.add_argument("--path", required=True, help="Path to the csv file")
    parser.add_argument("--output", help="Output filename")
    parser.add_argument("--theme", choices=["minimal", "best-estimate", "info", "degradation"], help="Optional theme argument")
    args = parser.parse_args()

    input_data = read_csv_file(args.path)

    theme = None
    if args.theme == "best-estimate": theme = BestEstimate(input_data)
    elif args.theme == "info": theme = Info(input_data)
    elif args.theme == "degradation": theme = Degradation(input_data)
    else: theme = Minimal(input_data)

    dot_filename = args.output if args.output is not None else "branch_and_bound.dot"

    generate_dot(input_data, dot_filename, theme)

if __name__ == "__main__":
    main()
