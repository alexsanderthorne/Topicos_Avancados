
class Meta(type):
    def __new__(self, class_name, bases, attrs):
       #S print(attrs)

        a = {}
        for name, val in attrs.items():
            if name.startswith("__"):
                a[name] = val
            else:
                a[name.upper()] = val
        #print(a)
        return type(class_name, bases, a)


class Dog(metaclass=Meta):

    x = 9
    e = 3

    def hello(self):
        print("hello")

d = Dog()
print(d.X)
print(d.HELLO())