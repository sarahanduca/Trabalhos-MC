import numpy as np
import math

class Receptor:
    def __init__(self, x, y, p0, l, p):
        self.coord = [x, y]
        self.p0 = p0
        self.l= l
        self.p= p

def calcDk(entry):
    numerator = entry.p0 - entry.p
    denumerator = 10 * entry.l
    exp = numerator/denumerator
    return math.pow(10, exp)

def calcCk(coords: np.matrix, dks):
    cks = []
    for i in range(len(dks)):
        valueOnIndex = coords[i].getA1()
        cks.append((math.pow(valueOnIndex[0], 2) + math.pow(valueOnIndex[1], 2)) - math.pow(dks[i], 2))

    return cks

def MatrixA(coords: np.matrix):
    f1 = coords[0].getA1()
    A = []

    for i in range(1, len(coords)):
        fk = coords[i].getA1()
        xk = 2 * (fk[0] - f1[0])
        yk = 2 * (fk[1] - f1[1])
        A.append([xk, yk])

    return np.matrix(A)

def MatrixB(cks):
    c1 = cks[0]
    B = []
    for i in range(1, len(cks)):
        ck = cks[i] - c1
        B.append(ck)

    return np.matrix(B).getT()

def calcTrangulation(matrixA, matrixB):
    matrixAT = matrixA.getT()
    ATimesAT = matrixAT * matrixA
    inverseATimesAT = ATimesAT.getI()
    inverseTimesAT = inverseATimesAT * matrixAT

    return inverseTimesAT * matrixB

def Matrix(receptors):
    coords = []
    dks = []
    for i in range(len(receptors)):
        coords.append(receptors[i].coord)
        dks.append(calcDk(receptors[i]))
    return np.matrix(coords), dks

def printResult(receptors):
    coords, dks = Matrix(receptors) 
    cks = calcCk(coords, dks)
    matrixA = MatrixA(coords)
    matrixB = MatrixB(cks)
    print("Resultados: \n", calcTrangulation(matrixA, matrixB))


if __name__ == "__main__":
    receptor1 = Receptor(1.55, 17.63, -26.0, 2.1, -48.4)
    receptor2 = Receptor(-4.02, 0.00, -33.8, 1.8, -50.6)
    receptor3 = Receptor(-4.40, 9.60, -29.8, 1.3, -32.2)
    receptor4 = Receptor(9.27, 4.64, -31.2, 1.4, -47.4)
    receptor5 = Receptor(9.15, 12.00, -33.0, 1.5, -46.3)
    receptors = [receptor1, receptor2, receptor3, receptor4, receptor5]
    print("---------------------------------------------")
    print("x, y = (0.00, 9.00)")
    print("pk(dBm)[-48.4, -50.6, -32.2, -47.4, -46.3]")
    print("---------------------------------------------")
    printResult(receptors)
    receptor1 = Receptor(1.55, 17.63, -26.0, 2.1, -46.9)
    receptor2 = Receptor(-4.02, 0.00, -33.8, 1.8, -46.4)
    receptor3 = Receptor(-4.40, 9.60, -29.8, 1.3, -41.2)
    receptor4 = Receptor(9.27, 4.64, -31.2, 1.4, -45.8)
    receptor5 = Receptor(9.15, 12.00, -33.0, 1.5, -48.7)
    receptors = [receptor1, receptor2, receptor3, receptor4, receptor5]
    print("---------------------------------------------")
    print("x, y = (3.00, 3.00)")
    print("pk(dBm)[-46.9, -46.4, -41.2, -45.8, -48.7]")
    print("---------------------------------------------")
    printResult(receptors)
 
