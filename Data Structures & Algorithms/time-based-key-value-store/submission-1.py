class TimeMap:
    # use a dictionary to store key value pairs.
    # values in dict are tuples, with (time, value)
    # then binary search for highest viable time < timestamp
    def __init__(self):
        self.hsh = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hsh[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # where I do binary search in the key's array
        l, r = 0, len(self.hsh[key]) - 1
        found = False
        while l <= r:
            mid = (l+r)//2
            val = self.hsh[key][mid]
            # remember, val is in (timestamp, value)
            if val[0] == timestamp:
                return val[1]
            elif val[0] < timestamp:
                found = True
                l = mid + 1
            else:
                r = mid - 1
        # if not exactly found, return the closest val with time that is <= timestamp
        return self.hsh[key][r][1] if found else ""