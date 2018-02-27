class Parent(object):
    def override(self):
        print("Fuck you")

class Child(Parent):
    def override(self):
        print("No Fuck me")

dad = Parent()
son = Child()

dad.override()
son.override()
