class A:
    def method(self):
        print("Class A method")

class B(A):
    pass

class C(A):
    def method(self):
        print("Class C method")

class D(B,C):
    pass

d = D()
d.method() # Output: "Class C method"
help(D)