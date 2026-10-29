import numpy as np

class RightTriangle:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2

    # Calculate the hypotenuse
    def hyp(self):
        return np.sqrt(self.l1**2 + self.l2**2)

    # Calculate the angle near leg l1
    def angle1(self):
        return np.degrees(np.arctan(self.l2 / self.l1))

    # Calculate the angle near leg l2
    def angle2(self):
        return np.degrees(np.arctan(self.l1 / self.l2))


# Test the class
t = RightTriangle(1, np.sqrt(3))

print(t.hyp())
print(t.angle1())
print(t.angle2())

t2 = RightTriangle(3, 4)

print(t2.hyp())
print(t2.angle1())
print(t2.angle2())

'''or use this to round them to 2 decimal places
t = RightTriangle(1, np.sqrt(3))
print(round(t.hyp(), 2))
print(round(t.angle1(), 2))
print(round(t.angle2(), 2))

t2 = RightTriangle(1, 1)
print(round(t2.hyp(), 2))
print(round(t2.angle1(), 2))
print(round(t2.angle2(), 2))'''