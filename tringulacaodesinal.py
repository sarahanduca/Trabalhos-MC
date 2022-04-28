import numpy
import math

class Receptor:
    def __init__(self, x, y, z, p0, l, p):
        self.coord = [x, y, z]
        self.p0 = p0
        self.l= l
        self.p= p

ex1 = Receptor(1.55, 17.63, 1.35, -26.0, 2.1, -48.4)
ex2 = Receptor(-4.02, 0.00, 1.35, -33.8, 1.8, -50.6)
ex3 = Receptor(-4.40, 9.60, 1.35, -29.8, 1.3, -32.2)
ex4 = Receptor(9.27, 4.64, 1.35, -31.2, 1.4, -47.4)
ex5 = Receptor(9.15, 12.00, 1.35, -33.0, 1.5, -46.3)
receptors = [ex1, ex2, ex3, ex4, ex5]

def calcDk(entry):
    numerator = entry.p0 - entry.p
    denumerator = 10 * entry.l
    exp = numerator/denumerator
    return math.pow(10, exp)

def Matrix(receptors):
    coord = []
    dks = []
    for i in range(len(receptors)):
        coord.append(receptors[i].coord)
        dks.append(calcDk(receptors[i]))
    return numpy.matrix(coord), dks

print(Matrix(receptors))
print(calcDk(ex1))