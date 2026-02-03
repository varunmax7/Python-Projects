# Week10- Program 1
# Method Resolution Order
class father:
    def display(self):
        print("I enjoy cycling")
class mother:
    def display(self):
        print("I enjoy jogging")
class child(father, mother):
    def show(self):
        print("I enjoy running")
p=child()
p.display()
p.show()
