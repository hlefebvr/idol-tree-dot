class Info:

    def before(): ""

    def after(): ""

    def node_label(node_id, parent_id, status, value, branching, event, sum_of_infeasibilities):
        return node_id

    def edge_label(node_id, parent_id, status, value, branching, event, sum_of_infeasibilities):
        return ""

# 
#            color = "white"
#            if event == "3":
#                color = "#f5ced5"
#            elif event == "1":
#                color = "#67c270"
#            label = (f'<table cellspacing="0">'
#                    f'<tr><td colspan="2" bgcolor="{color}">{node_id}</td></tr>'
#                    f'<tr><td bgcolor="#efefef">{status}</td><td bgcolor="#efefef">{value}</td></tr>'
#                    f'</table>')
            