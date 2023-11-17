# made by tarık eren adalan for a high school project

import math

def kompleks_topla_yaz(c1, c2):
    a1, b1 = c1
    a2, b2 = c2
    reelparca = a1+a2
    sanalparca = b1+b2
    print(f"reel parçası:{reelparca} sanal parçası:{sanalparca}i")

def kompleks_topla(c1, c2):
    a1, b1 = c1
    a2, b2 = c2
    reelparca = a1+a2
    sanalparca = b1+b2
    return reelparca, sanalparca

def kompleks_cikar_yaz(c1, c2):
    a1, b1 = c1
    a2, b2 = c2
    reelparca = a1 - a2
    sanalparca = b1 - b2
    print(f"reel parçası:{reelparca} sanal parçası:{sanalparca}i")

def kompleks_cikar(c1, c2):
    a1, b1 = c1
    a2, b2 = c2
    reelparca = a1 - a2
    sanalparca = b1 - b2
    return reelparca, sanalparca

def kompleks_carp_yaz(c1, c2):
    a1, b1 = c1
    a2, b2 = c2
    reelparca = a1*a2 - b1*b2
    sanalparca = a1*b2 + a2*b1
    print(f"reelparçası:{reelparca} sanal parçası:{sanalparca}i")

def kompleks_carp(c1, c2):
    a1, b1 = c1
    a2, b2 = c2
    reelparca = a1*a2 - b1*b2
    sanalparca = a1*b2 + a2*b1
    return reelparca, sanalparca

def kompleks_bol_yaz(c1, c2):
    a1, b1 = c1
    a2, b2 = c2
    reelparca = (a1*a2) + (b1*b2) / (b2**2) + (a2**2)
    sanalparca = (b1*a2) - (a1*b2) / (b2**2) + (a2**2)
    print(f"reelparçası:{reelparca} sanal parçası:{sanalparca}i")

def kompleks_bol(c1, c2):
    a1, b1 = c1
    a2, b2 = c2
    reelparca = (a1*a2) + (b1*b2) / (b2**2) + (a2**2)
    sanalparca = (b1*a2) - (a1*b2) / (b2**2) + (a2**2)
    return reelparca, sanalparca

def kuaterniyon_carp_yaz(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    reelparca = (w1*w2) - (x1*x2) - (y1*y2) - (z1*z2)
    sanalparcai = (w1*x2) + (x1*w2) + (y1*z2) - (z1*y2)
    sanalparcaj = (w1*y2) - (x1*z2) + (y1*w2) + (z1*x2)
    sanalparcak = (w1*z2) + (x1*y2) - (y1*x2) + (z1*w2)
    print(f"reel parça:{reelparca}")
    print(f"i'li sanal parça:{sanalparcai}i, j'li sanal parca:{sanalparcaj}j, k'li sanal parça:{sanalparcak}k")

def kuaterniyon_carp(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    reelparca = (w1*w2) - (x1*x2) - (y1*y2) - (z1*z2)
    sanalparcai = (w1*x2) + (x1*w2) + (y1*z2) - (z1*y2)
    sanalparcaj = (w1*y2) - (x1*z2) + (y1*w2) + (z1*x2)
    sanalparcak = (w1*z2) + (x1*y2) - (y1*x2) + (z1*w2)
    return reelparca, sanalparcai, sanalparcaj, sanalparcak

def kuaterniyon_topla_yaz(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    reelparca = (w1+w2)
    sanalparcai = (x1+x2)
    sanalparcaj = (y1 + y2)
    sanalparcak = (z1 + z2)
    print(f"reel parça:{reelparca}")
    print(f"i'li sanal parça:{sanalparcai}i, j'li sanal parca:{sanalparcaj}j, k'li sanal parça:{sanalparcak}k")

def kuaterniyon_topla(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    reelparca = (w1+w2)
    sanalparcai = (x1+x2)
    sanalparcaj = (y1 + y2)
    sanalparcak = (z1 + z2)
    return reelparca, sanalparcai, sanalparcaj, sanalparcak

def kompleks_rotasyon_yaz(q1, aci):
    x, y = q1
    c = math.cos(aci)
    s = math.sin(aci)
    reelparca = (c*x)-(s*y)
    sanalparca = (c*y)+(s*x)
    print(f"reel parça:{reelparca}, sanal parça{sanalparca}i, {aci} derece döndürüldü")

def kompleks_rotasyon(q1, aci):
    x, y = q1
    c = math.cos(aci)
    s = math.sin(aci)
    reelparca = (c*x)-(s*y)
    sanalparca = (c*y)+(s*x)
    return reelparca, sanalparca

def oktaniyon_carp(o1, o2):
    a, b, c, d, e, f, g, h = o1
    i, j, k, l, m, n, o, p = o2
    reelparca = a*i - b*j - c*k - d*l - m*e - n*f - o*g - p*h
    birincisanal = a*j + b*i + c*l - d*k - m*f + n*e + o*h - p*g
    ikincisanal = a*k - b*l + c*i + d*j - m*g - n*h + o*e + p*f
    ucuncusanal = a*l + b*k - c*j + d*i - m*h + n*g - o*f + p*e
    dorduncusanal = m*a - n*b - o*c - p*d + e*i + f*j + g*k + h*l
    besincisanal = m*b + n*a + o*d - p*c - e*j + f*i - g*l + h*k
    altincisanal = m*c - n*d + o*a + p*b - e*k + f*l + g*i - h*j
    yedincisanal = m*d + n*c - o*b + p*a - e*l - f*k + g*j + h*i
    return reelparca, birincisanal, ikincisanal, ucuncusanal, dorduncusanal, besincisanal, altincisanal, yedincisanal

def oktaniyon_topla(o1, o2):
    a, b, c, d, e, f, g, h = o1
    i, j, k, l, m, n, o, p = o2
    reelparca = a+i
    birincisanal = b+j
    ikincisanal = c+k
    ucuncusanal = d+l
    dorduncusanal = e+m
    besincisanal = f+n
    altincisanal = g+o
    yedincisanal = h+p
    return reelparca, birincisanal, ikincisanal, ucuncusanal, dorduncusanal, besincisanal, altincisanal, yedincisanal

def oktaniyon_topla_yaz(o1, o2):
    a, b, c, d, e, f, g, h = o1
    i, j, k, l, m, n, o, p = o2
    reelparca = a+i
    birincisanal = b+j
    ikincisanal = c+k
    ucuncusanal = d+l
    dorduncusanal = e+m
    besincisanal = f+n
    altincisanal = g+o
    yedincisanal = h+p
    print(f"reel parça:{reelparca}e0, birinci sanal parça:{birincisanal}e1, ikinci sanal parça:{ikincisanal}e2,")
    print(f"üçüncü parça:{ucuncusanal}e3, dördüncü sanal parça:{dorduncusanal}e4, ikinci sanal parça:{besincisanal}e5,")
    print(f"reel parça:{altincisanal}e6, birinci sanal parça:{yedincisanal}e7,")

def oktaniyon_carp_yaz(o1, o2):
    a, b, c, d, e, f, g, h = o1
    i, j, k, l, m, n, o, p = o2
    reelparca = a*i - b*j - c*k - d*l - m*e - n*f - o*g - p*h
    birincisanal = a*j + b*i + c*l - d*k - m*f + n*e + o*h - p*g
    ikincisanal = a*k - b*l + c*i + d*j - m*g - n*h + o*e + p*f
    ucuncusanal = a*l + b*k - c*j + d*i - m*h + n*g - o*f + p*e
    dorduncusanal = m*a - n*b - o*c - p*d + e*i + f*j + g*k + h*l
    besincisanal = m*b + n*a + o*d - p*c - e*j + f*i - g*l + h*k
    altincisanal = m*c - n*d + o*a + p*b - e*k + f*l + g*i - h*j
    yedincisanal = m*d + n*c - o*b + p*a - e*l - f*k + g*j + h*i
    print(f"reel parça:{reelparca}e0, birinci sanal parça:{birincisanal}e1, ikinci sanal parça:{ikincisanal}e2,")
    print(f"üçüncü parça:{ucuncusanal}e3, dördüncü sanal parça:{dorduncusanal}e4, ikinci sanal parça:{besincisanal}e5,")
    print(f"reel parça:{altincisanal}e6, birinci sanal parça:{yedincisanal}e7,")

def kuaterniyon_ters(c1):
    w1, x1, y1, z1 = c1
    ters = [w1, -x1, y1, z1]
    return ters

def kuaterniyon_rotasyon(q1, donusvektoru, aci):

    sinacisi = math.sin(aci/2)
    cosacisi = math.cos(aci/2)

    rotasyonkuaterniyonu = [
        cosacisi,
        donusvektoru[0] * sinacisi,
        donusvektoru[1] * sinacisi,
        donusvektoru[2] * sinacisi
    ]

    sonuc = kuaterniyon_carp(rotasyonkuaterniyonu, q1)

    return sonuc
