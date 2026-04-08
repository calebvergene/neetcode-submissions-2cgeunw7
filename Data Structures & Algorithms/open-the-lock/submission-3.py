class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # use bfs

        # need this because we dont check "0000" in the bfs
        if target == "0000": return 0
        if "0000" in deadends: return -1

        # init
        seen = set(deadends)
        q = collections.deque()
        q.append('0000')

        level = 0
        while q:
            # for loop tracks each level of bfs 
            level += 1
            for _ in range(len(q)):
                code = q.popleft()
                # 4 different slots, 2 directions
                for slot in range(4):
                    # this basically simulates turning the slots of the code
                    up = code[:slot] + str((int(code[slot])+1)%10) + code[slot+1:]
                    down = code[:slot] + str((int(code[slot])-1)%10) + code[slot+1:]

                    # if they havent been seen yet, add to seen then add to q
                    if up not in seen:
                        seen.add(up)
                        if up == target: return level
                        q.append(up)
                    if down not in seen:
                        seen.add(down)
                        if down == target: return level
                        q.append(down)
        return -1
