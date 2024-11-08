class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
v1 = Vector(6, 2)
v2 = Vector(5, 7)
v3 = v1 + v2
print(f"v1 + v2 = {v3}")
