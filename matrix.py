import sympy as sym
class Matrix():
    a = None

    def __init__(self, a):
        self.a = a

    def __str__(self):
        s = ""
        for i in range(len(self.a)):
            for j in range(len(self.a[i])):
                s += f"{self.a[i][j]} "
            s = s[:-1] + "\n"
        return s[:-1]

    def __add__(self, other):
        if len(self.a) != len(other.a) or len(self.a[0]) != len(other.a[0]):
            raise ValueError("Matrix dimension error!")
        plus = [[0 for _ in range(len(self.a[0]))] for _ in range(len(self.a))]
        for i in range(len(self.a)):
            for j in range(len(self.a[i])):
                plus[i][j] = self.a[i][j] + other.a[i][j]
        return Matrix(plus)

    def det(self):
        detM = 0
        if len(self.a) != len(self.a[0]):
            raise ValueError("Matrix isn't square!")
        if len(self.a) == 0:
            raise ValueError("Matrix is empty!")
        elif len(self.a) == 1:
            return self.a[0][0]
        elif len(self.a) == 2:
            detM = self.a[0][0] * self.a[1][1] - self.a[1][0] * self.a[0][1]
        else:
            for j in range(len(self.a[0])):
                detM += (1-2*(j%2)) * self.a[0][j]*self.minor(0,j).det()
        return detM

    def minor(self, m, n):
        return Matrix([row[:n]+row[n+1:] for row in (self.a[:m] + self.a[m+1:])])
    
    def tr(self):
        return Matrix([[self.a[i][j] for i in range(len(self.a))] for j in range(len(self.a[0]))])

    def inv(self):
        return Matrix([[sym.Rational(((1-2*((i+1)%2))*self.minor(i, j).det()), self.det()) for i in range(len(self.a))] for j in range(len(self.a[0]))])

matA = Matrix([[6,-5,8,4,3,5,7], [9,7,5,2,5,2,4], [7,5,3,7,3,1,1], [-4,8,-8,-3,8,9,5], [3,2,5,6,1,0,6], [1,4,2,6,4,3,3] ])
matB = Matrix([[1]*3]*3)
print(matA)
print(matA.inv())


