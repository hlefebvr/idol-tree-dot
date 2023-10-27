class Entry:

    def __init__(self, row):
        time, node_id, parent_id, level, status, value, branching, event, sum_of_infeasibilities = row 
        
        self.time = float(time)
        self.node_id = int(node_id)
        self.parent_id = int(parent_id)
        self.level = int(level)
        self.status = status
        self.value = float(value) if value != "Inf" else None
        self.branching = branching 
        self.event = event 
        self.sum_of_infeasibilities = float(sum_of_infeasibilities)
        