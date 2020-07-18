class Polynomial():
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        # return ' Polynomial({!r})'.format(self.coeffs)
        return f' Polynomials {self.coeffs}'

    # yield generator object Polynomial.......
    # def __add__(self, other):
    #     return Polynomial((x + y for x,y in zip(self.coeffs, other.coeffs)))

    # zip function returns iterator of tuples
    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))  

    def __len__(self):
        return len(self.coeffs)


p1 = Polynomial(1,2,-3) # x^2 + 2x -3
print(p1)   # Polynomials (1, 2, -3)

p2 = Polynomial(2,3,4) # 2x^2 + 3x + 4
print(p2)   # Polynomials (2, 3, 4)


print(p1 + p2)       #  (3, 5, 1)
print(p1 + p2 + p2)  #  (5, 8, 5)
