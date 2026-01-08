# Python
# This script generates a visual representation of a binary search tree using ASCII characters.
# It attempts to create a somewhat aesthetically pleasing and readable output.

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def get_height(root):
    if root is None:
        return 0
    return 1 + max(get_height(root.left), get_height(root.right))

def draw_tree(root):
    if root is None:
        print("Tree is empty.")
        return

    lines = []
    nodes_at_level = {}
    max_width = 0

    def traverse(node, level, prefix=""):
        nonlocal max_width
        if node is not None:
            val_str = str(node.key)
            nodes_at_level.setdefault(level, []).append((val_str, prefix))
            max_width = max(max_width, len(val_str))

            traverse(node.left, level + 1, prefix + "L")
            traverse(node.right, level + 1, prefix + "R")

    traverse(root, 0)

    height = get_height(root)
    num_levels = height

    # Calculate spacing and positions
    for level in range(num_levels):
        current_level_nodes = sorted(nodes_at_level.get(level, []), key=lambda x: x[1])
        line = ""
        positions = {}
        current_pos = 0
        for val_str, prefix in current_level_nodes:
            # Simple heuristic for horizontal positioning
            spacing = (2 ** (num_levels - level - 1)) * max_width // 2
            if prefix.endswith("L"):
                offset = -spacing // 2
            elif prefix.endswith("R"):
                offset = spacing // 2
            else:
                offset = 0
            
            # Adjust positions to avoid overlap
            adjusted_pos = current_pos + offset
            
            # Find the nearest available slot
            best_fit = float('inf')
            for p in range(adjusted_pos, adjusted_pos + max_width + 5): # Search a range
                is_occupied = False
                for existing_pos, existing_len in positions.items():
                    if max(existing_pos, p) < min(existing_pos + existing_len, p + len(val_str)):
                        is_occupied = True
                        break
                if not is_occupied:
                    final_pos = p
                    break
            else:
                final_pos = adjusted_pos # Fallback if no clear spot

            positions[final_pos] = len(val_str)
            current_pos = final_pos + len(val_str)

            # Pad with spaces to align
            padding = " " * (final_pos - len(line))
            line += padding + val_str
        lines.append(line)

    # Add connecting lines
    for level in range(num_levels - 1):
        upper_line = lines[level]
        lower_line = lines[level + 1]
        new_lower_line = ""
        
        # Map node positions to their corresponding lower level connections
        node_map = {}
        current_char_index = 0
        for node_str, prefix in sorted(nodes_at_level.get(level, []), key=lambda x: x[1]):
            node_len = len(node_str)
            node_start = upper_line.find(node_str, current_char_index)
            if node_start != -1:
                node_map[node_start + node_len // 2] = prefix
                current_char_index = node_start + node_len
        
        current_lower_index = 0
        for i in range(len(upper_line)):
            if upper_line[i] != ' ':
                mid_point = i
                if mid_point in node_map:
                    prefix = node_map[mid_point]
                    # Try to find the corresponding child node's position
                    
                    # Find child node strings at the next level
                    children_at_next_level = sorted([ (v_str, p) for v_str, p in nodes_at_level.get(level + 1, []) ], key=lambda x: x[1])
                    
                    child_start_pos = -1
                    for child_val_str, child_prefix in children_at_next_level:
                        if prefix.endswith("L") and child_prefix.endswith("L"):
                            child_start_pos = lower_line.find(child_val_str)
                            break
                        elif prefix.endswith("R") and child_prefix.endswith("R"):
                            child_start_pos = lower_line.find(child_val_str)
                            break
                    
                    if child_start_pos != -1:
                        connection_point_in_lower = child_start_pos + len(child_val_str) // 2
                        
                        # Draw the connection line
                        for j in range(mid_point, connection_point_in_lower):
                            if j < len(new_lower_line):
                                if new_lower_line[j] == ' ':
                                    new_lower_line = new_lower_line[:j] + "|" + new_lower_line[j+1:]
                            else:
                                new_lower_line += " " * (j - len(new_lower_line)) + "|"
                        
                        # Draw the branch for left/right
                        if prefix.endswith("L"):
                            branch_pos = mid_point - 1
                            if branch_pos >= 0 and branch_pos < len(new_lower_line):
                                if new_lower_line[branch_pos] == ' ':
                                    new_lower_line = new_lower_line[:branch_pos] + "/" + new_lower_line[branch_pos+1:]
                            elif branch_pos >= 0:
                                new_lower_line += " " * (branch_pos - len(new_lower_line)) + "/"
                        elif prefix.endswith("R"):
                            branch_pos = mid_point + 1
                            if branch_pos < len(new_lower_line):
                                if new_lower_line[branch_pos] == ' ':
                                    new_lower_line = new_lower_line[:branch_pos] + "\\" + new_lower_line[branch_pos+1:]
                            else:
                                new_lower_line += " " * (branch_pos - len(new_lower_line)) + "\\"
            
            # Ensure lower_line is padded to match the length of new_lower_line as it grows
            while len(new_lower_line) < len(lower_line):
                new_lower_line += " "
            
            # Append characters from the original lower_line that haven't been overwritten
            for k in range(len(new_lower_line), len(lower_line)):
                new_lower_line += lower_line[k]

        lines.insert(level + 1, new_lower_line)

    for line in lines:
        print(line)

# Example Usage:
root = None
keys = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 90]
for key in keys:
    root = insert(root, key)

draw_tree(root)