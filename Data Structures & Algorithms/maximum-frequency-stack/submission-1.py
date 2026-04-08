class FreqStack:

    def __init__(self):
        # tricky becuase need to keep track of frequency and most current
        self.stacks = [] 
        self.freq = collections.defaultdict(int)
        # keep a list of stacks for each frequency
        # the list of stacks is a stack itself, stacks[-1] are the elments with highest freq
        

    def push(self, val: int) -> None:
        self.freq[val] += 1
        if len(self.stacks) < self.freq[val]:
            # then need to add to stacks
            self.stacks.append([])
        # now add it to that frequency stack
        self.stacks[self.freq[val]-1].append(val)
        

    def pop(self) -> int:
        # get the last stack in the list of stacks
        highest = self.stacks[-1]
        popped = highest.pop()
        self.freq[popped] -= 1
        # remove that list if its now empty
        if not highest:
            self.stacks.pop()
        return popped
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()