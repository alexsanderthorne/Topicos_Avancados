
class Person:
    
    def __init__(self,name):
        self.name = name
        
    def __repr__(self) -> str:
        return f"Person({self.name})"
    
    def __mul__(self,x):
        if type(x) is not int:
            raise Exception("Argumento inválido")
        
        self.name = self.name * x
        
    def __call__(self, y):
        print("Called theis function", y)
        
    def __len__(self):
        return len(self.name)
    
p = Person("Sander\n")
p*4
print(p)

print(len(p))