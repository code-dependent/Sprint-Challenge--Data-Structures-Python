
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None for i in range(capacity)]


    def append(self, item):
        self.storage.pop(0)
        self.storage.append(item)
        print(self.storage)


    def get(self):
        rtn = []

        for i in self.storage:

            if i is not None:
                rtn.insert(0,i)
        return rtn

b = RingBuffer(5)

b.append('a')
b.append('b')
b.append('c')
b.append('d')
b.append('e')
b.append('f')
b.append('g')
b.get()
