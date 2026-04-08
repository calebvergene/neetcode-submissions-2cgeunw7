class Node:
    def __init__(self, val, key, prev=None, nxt=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.nxt = nxt

class LRUCache:
    # basically need to implement a queue
    # BUT, the problem is that we need O(1) time for each operation, so a queue wouldn't work
    # so, we use a doubly linked list for O(1) removal time! Doubly allows us to reconnect the nodes.
    # then use a hashmap to store each key and its node
    def __init__(self, capacity: int):
        self.capacity = capacity
        # have a hash map to store key nodes. this can give us O(1) lookup for nodes
        self.node_hash = {}
        # keep a node at the start to init the doubly linked list
        self.head = Node(-1, -1)
        self.tail = self.head
    
    def insert(self, node):
        # insert at tail
        node.nxt = None
        node.prev = self.tail
        self.tail.nxt = node
        self.tail = node
    
    def remove(self, node):
        # removes specific node where ever it is and connects
        if node == self.tail:
            node.nxt = None
            self.tail = node.prev
            return
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.node_hash:
            self.remove(self.node_hash[key])
            self.insert(self.node_hash[key])
            return self.node_hash[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        # update node if its already in there
        if key in self.node_hash:
            self.remove(self.node_hash[key])
            self.insert(self.node_hash[key])
            self.node_hash[key].val = value  
        # else, add the key value
        else:
            new = Node(value, key)
            self.node_hash[key] = new
            self.insert(new)
        # if full, remove from back of the hash
        if len(self.node_hash) > self.capacity:
            del self.node_hash[self.head.nxt.key]
            self.remove(self.head.nxt)





    