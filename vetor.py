class Vetor:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vetor (%r,%r)' % (self.x, self.y)

    def __mul__(self, escalar):
        x = self.x * escalar
        y = self.y * escalar
        return Vetor(x, y)

    def __add__(self, outro):
        x = self.x + outro.x
        y = self.y + outro.y
        return Vetor(x, y)


v = Vetor(3, 5)
print(v*3)

v1 = Vetor(9, 4)
v2 = Vetor(8, 2)
print(v1+v2)
