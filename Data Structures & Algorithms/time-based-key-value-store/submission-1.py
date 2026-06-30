class TimeMap:

    def __init__(self):
        self.hs = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hs:
            self.hs[key].append((value, timestamp))
        else:
            self.hs[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hs:
            values = self.hs[key]
            if values[0][1] > timestamp:
                return ""
            else:
                i = 0
                while values[-1 -i][1] > timestamp:
                    i +=1
                return values[-1-i][0]
        else:
            return ""
