import math

def komplekstopla(a1, b1, a2, b2):
    reelparca = a1+a2
    sanalparca = b1+b2
    print(f"reel parçası:{reelparca} sanal parçası:{sanalparca}i")
def komplekscikar(a1, b1, a2, b2):
    reelparca = a1 - a2
    sanalparca = b1 - b2
    print(f"reel parçası:{reelparca} sanal parçası:{sanalparca}i")
def komplekscarp(a1, b1, a2, b2):
    reelparca = a1*a2 - b1*b2
    sanalparca = a1*b2 + a2*b1
    print(f"reelparçası:{reelparca} sanal parçası:{sanalparca}i")
def kompleksbol(a1, b1, a2, b2):
    reelparca = (a1*a2) + (b1*b2) / (b2**2) + (a2**2)
    sanalparca = (b1*a2) - (a1*b2) / (b2**2) + (a2**2)
    print(f"reelparçası:{reelparca} sanal parçası:{sanalparca}i")

def kuaterniyoncarp(w1, x1, y1, z1, w2, x2, y2, z2):
    reelparca = (w1*w2) - (x1*x2) - (y1*y2) - (z1*z2)
    sanalparcai = (w1*x2) + (x1*w2) + (y1*z2) - (z1*y2)
    sanalparcaj = (w1*y2) - (x1*z2) + (y1*w2) + (z1*x2)
    sanalparcak = (w1*z2) + (x1*y2) - (y1*x2) + (z1*w2)
    print(f"reel parça:{reelparca}, i'li sanal parça:{sanalparcai}i, j'li sanal parca:{sanalparcaj}, k'li sanal parça:{sanalparcak} ")



