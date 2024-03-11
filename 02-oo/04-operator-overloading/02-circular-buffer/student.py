class CircularBuffer():
    def __init__(self, n):
        self.n=n
        self.list = []

    def __len__(self):
        return len(self.list)
        

    def add(self, value):
        if len(self.list) == self.n:
            self.list.remove(self.list[0])
            self.list.append(value)
        else:
            self.list.append(value)

    def indexing(self, index):
        if index >= len(self.list):
            raise IndexError("Index out of range")
        return self.list[index]
    
    def __getitem__(self, index):
        return self.indexing(index)
    

