class Node(object):
    
    def __init__(self, value):
        
        self.value = value
        self.nextnode = None


def cycle_check(node):
    
    if node.nextnode == None:
        return False
    
    current_node = node
    
    while True:
        next_node = current_node.nextnode
        if next_node.nextnode == None:
            return False
        
        elif next_node.nextnode == node:
            return True
        
        else:
            current_node = next_node