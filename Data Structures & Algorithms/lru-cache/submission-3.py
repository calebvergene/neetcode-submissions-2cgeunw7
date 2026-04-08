class Node:
    def __init__(self, val, key, prev=None, nxt=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.nxt = nxt

class LRUCache:
    # use a hash map for key value pairs. point to nodes that store the value
    # keep a doubly linked list to allow us to easily remove from anywhere in linked list 

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {}
        self.head = Node(-1, -1) # dummy node that always points to the head. delete from head
        self.tail = self.head # points to the last node, which is where you insert


    def get(self, key: int) -> int:
        if key in self.nodes:
            node = self.nodes[key]
            self.use_node(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        # existing node
        if key in self.nodes:
            node = self.nodes[key]
            node.val = value
            self.use_node(node)

        # new node
        else:
            node = Node(value, key)
            self.nodes[key] = node
            self.insert_node(node)
            self.capacity -= 1
            # here we have inserted the new node. So, we need to check for overflow. 
            self.check_overflow()
        

    def use_node(self, node: Node) -> None:
        # triggered when existing node has been used. remove and reinsert node
        if node == self.tail:
            return
        
        self.remove_node(node)
        self.insert_node(node)
        

    
    def insert_node(self, node: Node) -> None:
        # inserts node at the tail of the cache
        self.tail.nxt = node
        node.prev = self.tail
        node.nxt = None
        self.tail = node
    
    def remove_node(self, node: Node) -> None:
        # removes node from the cache. assumes node is in cache.
        if self.tail == node:
            node.prev.nxt = None
            self.tail = node.prev
        else:
            node.prev.nxt = node.nxt
            node.nxt.prev = node.prev
        # detatch current node
        node.prev = None
        node.nxt = None

        
    def check_overflow(self):
        if self.capacity < 0:
            del self.nodes[self.head.nxt.key]
            self.remove_node(self.head.nxt) # will always be a node to delete since cap > 1
            self.capacity += 1
        
