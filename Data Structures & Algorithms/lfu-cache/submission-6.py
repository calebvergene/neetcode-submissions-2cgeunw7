    #feats:
    # track frequency of usages (  )
    # track how recent it was used ( doubly linked list )

class Node:
    def __init__(self, val, key, prev=None, nxt=None):
        self.prev = prev
        self.nxt = nxt
        self.val = val
        self.key = key

class LFUCache:
    # FINAL: 
    # have a hashmap to store frequencies and the nodes at those frequencies.
        # at each frequency in the hashmap, store (head, tail). this allows you to track recently used
        # ( pop at the head, insert at tail)
    # each time a node is used, then it moves up frequency nodes. 
    # always track the lowest frequency:
    # if you are moving node up and it is the current lowest frequency, then check if its now empty.

    def __init__(self, capacity: int):
        self.capacity = capacity
        # stores the nodes at each frequency
        self.cache = collections.defaultdict(lambda : [Node(None, None), None]) # freq : head, tail
        # stores each of the nodes for individual access
        self.nodes = {} # key : node, freq
        self.leastused = 0

    def remove(self, node, freq):
        # removes node from its freq list
        head, tail = self.cache[freq]
        if node == tail:
            node.prev.nxt = node.nxt
            self.cache[freq][1] = node.prev
            if self.cache[freq][1].val == None:
                self.cache[freq][1] = None
        else:
            node.prev.nxt = node.nxt
            node.nxt.prev = node.prev
        self.check_least(freq) # maintains the lowest frequency
    
    def insert(self, node, freq):
        # inserts node at the tail
        head, tail = self.cache[freq]
        if not tail: # list is empty
            head.nxt = node
            node.prev = head
            node.nxt = None
        else:
            tail.nxt = node
            node.prev = tail
            node.nxt = None
        self.cache[freq][1] = node # set new node to the tail

        
    def get(self, key: int) -> int:
        res = self.nodes.get(key, -1)
        print(-1 if res == -1 else res[0].val)
        if res != -1:
            self.remove(res[0], res[1]) # node, freq
            res[1] += 1
            self.insert(res[0], res[1]) # moves up one frequency
        return -1 if res == -1 else res[0].val

    def put(self, key: int, value: int) -> None:
        res = self.nodes.get(key, -1)
        print(-1 if res == -1 else res[0].val)
        # node not found, so add it
        if res == -1:
            new = Node(value, key)
            self.nodes[key] = [new, 1]

            # capacity check before adding new node, need to remove one if full
            if self.capacity == 0:
                self.capacity += 1
                removed = self.cache[self.leastused][0].nxt
                print(removed.key, self.leastused)
                self.remove(removed, self.leastused) # removes head.nxt at least used freq
                del self.nodes[removed.key]
            
            self.leastused = 1
            self.capacity -= 1
        else:
            res[0].val = value # edit the found node
            self.remove(res[0], res[1])
            res[1] += 1 # increment frequency

        # by here we will have the node we need to edit 
        node, freq = self.nodes[key]
        self.insert(node, freq)
    
    def check_least(self, freq):
        if freq == self.leastused:
            head = self.cache[self.leastused][0]
            if head.nxt == None:
                # then we know its now empty, so least is now freq + 1
                self.leastused += 1

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)