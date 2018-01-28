#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

# es demana calcular els punts de tangència de les
# rectes tangents a un cercle que passen per un punt exterior al cercle
#
# Anàlisi del problema
# Donat un cercle C (x0, y0) de radi r1
# i un punt P (px, py)
# es demana trobar les els punts de tangència amb C1
# de les rectes tangents a C1 que passen per P
#
# sigui d = distància(C, P)
# d = sqrt( (x0 - cx)² + (y0 - cy)² )
# si d > r1, aleshores el punt P és exterior al cercle i hi han dues sol·lucions
# si d = r1, aleshores el punt P és troba sobre el cercle i és la sol·lució
# si d < r1, aleshores no hi ha sol·lució perquè el punt és dins del cercle

def distancia(p1, p2):
    d = math.hypot(p1[0] - p2[0], p1[1] - p2[1])

    return d

def producteEscalar(v1, v2):
    dot = v1[0]*v2[0] + v1[1]*v2[1]

    return dot
    
def analitza(p, c, r):
    d = distancia(p, c)

    if d < r:
        print "El punt és dins del cercle. No hi ha sol·lució"
        exit(0)

    if d == r:
        print "El punt es troba sobre el cercle. El mateix punt és la sol·lució."
        print "La recta tangent és : (en paramètriques)\n"
        print "x = %f + L * %f" % (p[0], -(c[1] - p[1]) / d)
        print "y = %f + L * %f" % (p[1],  (c[0] - p[0]) / d)        
        exit(0)

    if d > r:
        print "El punt és exterior el cercle."
        print "Hi han dos rectes tangents que passen pel punt"
        print "i cada recta té un punt de tangència amb el cercle.\n"
        alfa = math.atan(r / math.sqrt(d * d - r * r))
        beta = math.atan2(c[1] - p[1], c[0] - p[0])
        vt1 = [math.cos(beta + alfa), math.sin(beta + alfa)]
        vt2 = [math.cos(beta - alfa), math.sin(beta - alfa)]
        print "vdt1, vector director recta tangent 1 = (%f, %f)" % (vt1[0], vt1[1])
        print "vdt2, vector director recta tangent 2 = (%f, %f)\n" % (vt2[0], vt2[1])
        print "Recta tangent 1 : (en paramètriques)"
        print "  x = %f + L * %f" % (p[0], vt1[0])
        print "  y = %f + L * %f\n" % (p[1], vt1[1])
        print "Recta tangent 2 : (en paramètriques)"
        print "  x = %f + L * %f" % (p[0], vt2[0])
        print "  y = %f + L * %f\n" % (p[1], vt2[1])
        rx = math.sqrt(d * d - r * r)
        pt1 = [p[0] + rx * vt1[0], p[1] + rx * vt1[1]]
        pt2 = [p[0] + rx * vt2[0], p[1] + rx * vt2[1]]
        print "punt tangent 1 T1 : (%f, %f)" % (pt1[0], pt1[1]) 
        print "punt tangent 2 T2 : (%f, %f)\n" % (pt2[0], pt2[1])
        print "Comprovació : "
        print "distància C-T1 : %f" % distancia(c, pt1)
        print "distància C-T2 : %f" % distancia(c, pt2)
        vdt1 = [(pt1[0] - c[0]) / distancia(c, pt1), (pt1[1] - c[1]) / distancia(c, pt1)]
        vdt2 = [(pt2[0] - c[0]) / distancia(c, pt2), (pt2[1] - c[1]) / distancia(c, pt2)]        
        print "vd1, Vector director recta C-T1 = (%f, %f) " % (vdt1[0], vdt1[1])
        print "vd2, Vector director recta C-T2 = (%f, %f) " % (vdt2[0], vdt2[1])
        print "producte escalar (vdt1 · vt1) = %f" % producteEscalar(vdt1, vt1)
        print "producte escalar (vdt2 · vt2) = %f" % producteEscalar(vdt2, vt2)
        
        exit(0)


if __name__ == "__main__":
    print "Càlcul dels punt de tangència (recta tangent que passa per un punt exterior)"
    print "----------------------------------------------------------------------------"

    # dades del problema
    # centre
    c = [0.0, 0.0]
    
    # radi dels cercles
    r1 = 5.0

    p = [10.0, 10.0]
    

    print "Dades del problema :"
    print "Cercle C. centre : (%f, %f) ; radi : %f" % (c[0], c[1], r1)
    print "Punt P : (%f, %f)" % (p[0], p[1])   

    # analitza casos
    analitza(p, c, r1)
