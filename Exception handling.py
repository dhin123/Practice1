class A:
    def add(self, a=3, b=0):
        self.a = a
        self.b = b
        res = self.a + self.b
        print(res)
class B(A):
    try:
        def add(self, a=3, b=0):
            res = a/b
    except ZeroDivisionError:
        print("Zero not allowed")

aobj = A()
bobj = B()
aobj.add()
bobj.add()

