class Gen:
    def __init__(self, n):
        self.n = n
        self.last = 0

        def __next__(self):
            return self.next()

