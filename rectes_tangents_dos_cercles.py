#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

# es demana calcular les rectes tangents a dos cercles i els  punts de tangència 
#
# Anàlisi del problema
# Donat un cercle C1 amb centre a (x1, y1) de radi r1
# i un cercle C2 amb centre a (x2, y2) de radi r2
# es demana trobar les rectes tangents a C1 i C2 i els punts de tangència 
# de les rectes tangents amb C1 i C2
#
# sigui d = distància(C1, C2)
# d = sqrt( (x1 - x2)² + (y1 - y28)² )
# cas 1) si d > r1 + r2, els dos cercles estan separats i són exteriors l'un de l'altre.
# aleshores hi han quatre rectes tangents i vuit punts de tangència
#
# cas 2) si d = r1 + r2, aleshores els dos cercles es toquen per un punt.
# hi han tres rectes tangents i cinc punts de tangència
#
# cas 3) si d < r1 + r2 i d > r1 i d > r2
# aleshores els dos cercles es tallen en dos punts.
# Hi han dues rectes tangents i quatre punts de tangència
#
# cas 4) si d = r1 - r2
# aleshores el cercle amb centre a C2 és interior i tangent a C1.
# hi ha una recta tangent, i un punt de tangència
#
# cas 5) si d = r2 - r1
# aleshores el cercle amb centre a C1 és interior i tangent a C2.
# hi ha una recta tangent, i un punt de tangència
#
# cas 6) si d < r1 - r2    
# aleshores un el cercle amb centre C2 és interior al cercle amb centre a C1
# sense cap punt de tangència. No hi ha sol·lució.
#
# cas 7) si d < r2 - r1  
# aleshores un el cercle amb centre C1 és interior al cercle amb centre a C2
# sense cap punt de tangència. No hi ha sol·lució.
#
# cas 8) si d = 0 i r1 = r2
# aleshores els dos cercles són iguals i estan superposats.
# hi han infinites rectes tangents i infinits punts de tangència

def distancia(p1, p2):
    d = math.hypot(p1[0] - p2[0], p1[1] - p2[1])

    return d

def producteEscalar(v1, v2):
    dot = v1[0]*v2[0] + v1[1]*v2[1]

    return dot

def vectorDirectorEntreDosPunts(p1, p2):
    d = distancia(p2, p1)
    vectorDirector = [(p2[0] - p1[0]) / d, (p2[1] - p1[1]) / d]

    return vectorDirector

def vectorOrtogonal(v):
    ortog = [-v[1], v[0]]
    
    return ortog

def analitza(c1, r1, c2, r2):
    d = distancia(c1, c2)

    if d < (r1 - r2):
        print "El cercle amb centre a C2 és interior al cercle C1, sense cap punt de tangència."
        print "no hi ha sol·lució."

        exit(0)

    if d < (r2 - r1):
        print "El cercle amb centre a C1 és interior al cercle C2, sense cap punt de tangència."
        print "no hi ha sol·lució."

        exit(0)

    if d == (r2 - r1):
        print "El cercle amb centre a C1 és interior i tangent al cercle  C2"
        print "Hi ha una recta tangent i un punt de tangència\n"
        cerclesTangents(c1, r1, c2, r2)

        exit(0)

    if d == (r1 - r2):
        print "El cercle amb centre a C2 és interior i tangent al cercle  C1"
        print "Hi ha una recta tangent i un punt de tangència\n"
        cerclesTangents(c1, r1, c2, r2)

        exit(0)

    if d == 0 and r1 == r2:
        print "Els dos cercles són iguals i estan superposats."
        print "Hi han infinites rectes tangents i infinits punts de tangència".
        print "Els punts de tangència són els punts dels cercles."
        print "Donat un punt de tangència Pt amb coordenades (xt, yt) "
        print "aleshores la recta tangent per aquest punt ve donada : (en paramètriques)"
        print "x = xt + L * (yt - cy) / d"
        print "y = yt + L * (cx - xt) / d"
        print "amb d = distancia(Pt, C1)"

        exit(0)


    if (d < (r1 + r2)) and  (d > r1) and (d > r2) :
        print "Els cercles es tallen en dos punts."
        print "Hi han dues rectes tangents i quatre punts de tangència"

        duesTangents(c1, r1, c2, r2)

        exit(0)

    if d > (r1 + r2):
        print "Els dos cercles estan separats i són exteriors l'un de l'altre."
        print "Hi han quatre rectes tangents i vuit punts de tangència"

        quatreTangents(c1, r1, c2, r2)

        exit(0)

    if d = (r1 + r2):
        print "Eels dos cercles es toquen per un punt."
        print "Hi han tres rectes tangents i cinc punts de tangència."

        tresTangents(c1, r1, c2, r2)

        exit(0)
        
def duesTangents(c1, r1, c2, r2):
    # TODO
    pass

def tresTangents(c1, r1, c2, r2):
    # TODO
    pass

def quatreTangents(c1, r1, c2, r2):
    # TODO
    pass

def cerclesTangents(c1, r1, c2, r2):
    d = distancia(c1, c2)
    v = vectorDirectorEntreDosPunts(c1, c2)
    print "Recta entre (%f, %f) i (%f, %f) :  (en paramètriques)" % (c1[0], c1[1], c2[0], c2[1])
    print "x = %f + L * (%f)" % (c1[0], v[0])
    print "y = %f + L * (%f)\n" % (c1[1], v[1])
    if r1 > r2:
        pt = [c1[0] + r1 * v[0], c1[1] + r1 * v[1]]
    else:
        pt = [c1[0] - r1 * v[0], c1[1] - r1 * v[1]]
    print "punt de tangència: (%f, %f)\n" % (pt[0], pt[1])
    vort = vectorOrtogonal(v)
    print "Recta tangent :  (en paramètriques)"
    print "x = %f + L * (%f)" % (pt[0], vort[0])
    print "y = %f + L * (%f)\n" % (pt[1], vort[1])
       
if __name__ == "__main__":
    print "Càlcul del les rectes tangents a dues circumferències i punts de tangència"
    print "--------------------------------------------------------------------------"

    # dades del problema
    # centres
    c1 = [0.0, 0.0]
    c2 = [4.0, 0.0]
    
    # radi dels cercles
    r1 = 1.0
    r2 = 5.0

    print "Dades del problema :"
    print "Cercle C1. centre : (%f, %f) ; radi : %f" % (c1[0], c1[1], r1)
    print "Cercle C2. centre : (%f, %f) ; radi : %f" % (c2[0], c2[1], r2)
    
    # analitza casos
    analitza(c1, r1, c2, r2)
