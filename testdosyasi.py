import hiperkompleks

c1 = [1, 2]
c2 = [3, 4]
q1 = [1, 2, 3, 4]
q2 = [5, 6, 7, 8]
o1 = [1, 2, 3, 4, 5, 6, 7, 8]
o2 = [8, 7, 6, 5, 4, 3, 2, 1]
########################################################
hiperkompleks.kompleks_topla_yaz(c1, c2)
print(hiperkompleks.kompleks_topla(c1, c2))

hiperkompleks.kompleks_cikar_yaz(c1, c2)
print(hiperkompleks.kompleks_cikar(c1, c2))

hiperkompleks.kompleks_carp_yaz(c1, c2)
print(hiperkompleks.kompleks_carp(c1, c2))

hiperkompleks.kompleks_bol_yaz(c1, c2)
print(hiperkompleks.kompleks_bol(c1, c2))

hiperkompleks.kompleks_rotasyon_yaz(c1, 45)
print(hiperkompleks.kompleks_rotasyon(c1, 45))

#########################################################
hiperkompleks.kuaterniyon_topla_yaz(q1, q2)
print(hiperkompleks.kuaterniyon_topla(q1, q2))

hiperkompleks.kuaterniyon_carp_yaz(q1, q2)
print(hiperkompleks.kuaterniyon_carp(q1, q2))

print(hiperkompleks.kuaterniyon_rotasyon(q1, q2, 45))

print(hiperkompleks.kuaterniyon_ters(q1))
##########################################################
hiperkompleks.oktaniyon_topla_yaz(o1, o2)
print(hiperkompleks.oktaniyon_topla(o1, o2))

hiperkompleks.oktaniyon_carp_yaz(o1, o2)
print(hiperkompleks.oktaniyon_carp(o1, o2))
