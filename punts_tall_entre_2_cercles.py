#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

# es demana calcular els punts de tall entre el cercle
# C1 amb centre a c1 = [c1x, c1y] de radi r1,
# i el cercle C2 amb centre a c2 = [c2x, c2y] de radi r2
#
# anàlisi del problema :
#
# sigui d = distancia(c1, c2)
# d = sqrt( (c1x - c2x)² + (c1y - c2y)² )
# 1) Si d = 0 i r1 <> r2, aleshores els cercles son concèntrics
# i no té sol·lució
# 2) Si d = 0 i r1 = r2, aleshores els cercles son iguals
# i té infinites sol·lucions
# 3) Si d > r1 + r2, aleshores els cercles no es toquen
# i no té sol·lució
# 4) si d = r1 + r2, aleshores els cercles són tangents
# i la sol·lució és el punt de tangència
# 5 )si d < r1 + r2, aleshores els cercles es tallen en dos punts
# que són la sol·lució
#
# Solució al cas 4
# El punt de tangència es troba a la recta que passa per c1 i c2
# a una distància r1 de c1 i a una distància r2 de c2.
#
# Per obtenir el punt de tangència, es pot fer servir l'expressió
# vectorial de la recta que passa per c1 i c2, que pren la forma
# (x,y) = (c1x, c1y) + L * (v1, v2) (veure https://ca.wikipedia.org/wiki/Recta)
# amb v = (v1, v2), vector director de la recta c1-c2
# On v1 = (c2x - c1x) / d; i v2 = (c2y - c1y) / d 
# El punt de tangència pren el valor :
# (xt, yt) = (c1x, c1y) + r1 * (v1, v2)
# és dir, aplicant la distància r1 sobre el vector director v al punt c1  
# També es pot trobar la sol·lució aplicant la distància r2 al punt c2
# sobre el mateix vector director -és la mateixa recta- però en sentit contrari (signe).
# (xt, yt) = (c2x, c2y) - r2 * (v1, v2)
#
# Sol·lució al cas 5
# pas 1. Sol·lució del problema equivalent simplificat 
# La solució del problema es pot construir a partir de la solució del
# problema equivalent de dos cercles amb centres sobre l'eix X 
# que es tallen en dos punts equidistants de (0,0)
# sobre l'eix Y.
# el centre de C'1 serà (x0,0); el de C'2, (x1, 0),
# Per construcció, faig que x1 > x0 és dir, x1 positiu i x0 negatiu.
# les solucions seran (0, ys) i (0, -ys)
# aleshores:
# per Pitàgores,     1) x0² + ys² = r1²
#             i      2) x1² + ys² = r2²
#       1) - 2)      3) x0² - x1² = r1² - r2²
# també coneixem d = + sqrt( (c1x - c2x)² + (c1y - c2y)² )
# per construcció x1 > x0, per tant  4)  d  = x1 - x0
#                   
# aleshores, de 4) obtinc x1 = d + x0.
# substitueixo x1 a 3 i trobo x0² - (d + x0)² = r1² - r2²
#                             x0² - d² -2 d x0 - x0² = r1² -r2²
# per tant x0 = (r2² - r1² - d²) / (2 d)
#          x1 = d + x0
#       i  ys = + sqrt( r1² - x0² )
#
# ja tinc, doncs, (x0, 0), (x1, 0), (0, ys) i (0, -ys)
#
# pas 2. Rotació intel·ligent
# aleshores caldrà fer una rotació sobre (0,0) dels cinc punts sol·lució.
# Aquesta rotació ha de fer que el cercle de radi r1 amb centre a (x0,0)
# quedi a la mínima distància del cercle de radi r1 centrat a (c1x, c1y);
# amb aquesta mateixa rotació, el cercle de radi r2 amb centre (x1, 0)
# també queda a la mínima distància del cercle de radi 2 centrat a (c2x, c2y)
# aquest angle A ve determinat pel vector director de la recta que uneix c1 i c2
# aleshores, cal aplicar la rotació A a la sol·lució. Les solucions rotades són
# (x0r, y0r), (x1r, y1r), (xs1r, ys1r), (xs2r, y2sr).
# Però cal verificar que l'orientació és correcta i, per tant, cal comprovar que
# el vector director entre (x0r, y0r), (x1r, y1r) té el mateix sentit
# que el vector director entre (c1x, c1y) i (c2x, c2y). En definitiva, que
# Cond1) x1r - x0r = c2x - c1x
# Cond2) y1r - y0r = c2y - c1y
# Si alguna de les dues igualtats no es cumpleix, vol dir que els cercles rotats no han
# quedat a la mínima distància, si no que han quedat en el mateix vector director, però amb
# les posicions relatives intercanviades, això vol dir que cal intercanviar-los aplicant una
# rotació addicional de mitja volta, o pi radians.
#
# pas 3. finalment, traslacionar les solucions a la posició original.
# La traslació a aplicar és la que converteix els punts
# (x0r, y0r) en (c1x, c1y) i  (x1r, y1r) en (c2x, c2y)
# per tant les equacions de la traslació són :
# xt = x + c1x - x0r ; o l'equivalent per Cond1) xt = x + c2x - x1r    
# yt = y + c1y - y0r ; o l'equivalent per Cond2) yt = y + c2y - y1r
#
# Per tant, la sol·lució final és :
# punt 1:
# xst1r = xs1r + c1x - x0r
# yst1r = ys1r + c1y - y0r 
#
# punt 2:
# xst2r = xs2r + c1x - x0r
# yst2r = ys2r + c1y - y0r 
#
#
# La rotació
# ----------
# La rotació en un angle B ve donada per la transformació
# ptrx = ptx * math.cos(B) - pty * math.sin(B)
# ptry = ptx * math.sin(B) + pty * math.cos(B)
# 
# o matricialment :
#
#   | ptrx |   | cos(B)  -sin(B)| | ptx|
#   |      | = |                | |    |
#   | ptry |   | sin(B)   cos(B)| | pty|
#

def distancia(p1, p2):
    d = math.hypot(p1[0] - p2[0], p1[1] - p2[1])

    return d

def puntMig(p1, p2):     
    cx = (p1[0] + p2[0]) / 2.0 
    cy = (p1[1] + p2[1]) / 2.0

    return [cx, cy]

def analitza(c1, r1, c2, r2):
    d = distancia(c1, c2)

    if d == 0 and r1 <> r2:
        print "Els cercles son concèntrics. No té sol·lució."
        exit(0)
        
    if d == 0 and r1 == r2:
        print "Els cercles son iguals. Té infinites sol·lucions."
        print "Els mateixos cercles són la sol·lució."
        exit(0)

    if d > (r1 + r2):
        print "Els cercles no es toquen. No té sol·lució."
        exit(0)
        
    if d == (r1 + r2):
        print "Els cercles són tangents."
        print "La sol·lució és el punt de tangència."
        puntDeTangencia(c1, r1, c2, r2)
        exit(0)
        
    if d < (r1 + r2):
        print "Els cercles es tallen en dos punts. "
        puntsDeTall(c1, r1, c2, r2)
        exit(0)

def puntDeTangencia(c1, r1, c2, r2):
    # Solució al cas 4
    # El punt de tangència es troba a la recta que passa per c1 i c2
    # a una distància r1 de c1 i a una distància r2 de c2.
    #
    # Per obtenir el punt de tangència, es pot fer servir l'expressió
    # vectorial de la recta que passa per c1 i c2, que pren la forma
    # (x,y) = (c1x, c1y) + L * (v1, v2) (veure https://ca.wikipedia.org/wiki/Recta)
    # amb v = (v1, v2), vector director normalitzat de la recta c1-c 2
    # On v1 = (c2x - c1x) / d; i v2 = (c2y - c1y) / d 
    # El punt de tangència pren el valor :
    # (xt, yt) = (c1x, c1y) + r1 * (v1, v2)
    # és dir, aplicant la distància r1 sobre el vector director v al punt c1  
    # També es pot trobar la sol·lució aplicant la distància r2 al punt c2
    # sobre el mateix vector director -és la mateixa recta- però en sentit contrari (signe).
    # (xt, yt) = (c2x, c2y) - r2 * (v1, v2)

    v = vectorDirector(c1, c2)

    xt = c1[0] + r1 * v[0]
    yt = c1[1] + r1 * v[1]
    pt = [xt, yt]

    print " Punt de tangència a (%f, %f)" % (xt, yt)
    print " Comprovació : distància c1 a Pt : %f, i r1 = %f " % (distancia(c1, pt), r1)
    print " Comprovació : distància c2 a Pt : %f, i r1 = %f " % (distancia(c2, pt), r2)    


def vectorDirector(c1, c2):
    d = distancia(c1, c2)
    v = [(c2[0] - c1[0]) / d, (c2[1] - c1[1]) / d ]

    return v

def puntsDeTall(c1, r1, c2, r2):
    # Sol·lució al cas 5
    # pas 1. Sol·lució del problema equivalent simplificat 
    # La solució del problema es pot construir a partir de la solució del
    # problema equivalent de dos cercles amb centres sobre l'eix X 
    # que es tallen en dos punts equidistants de (0,0)
    # sobre l'eix Y.
    # el centre de C'1 serà (x0,0); el de C'2, (x1, 0),
    # Per construcció, faig que x1 > x0 és dir, x1 positiu i x0 negatiu. 
    # les solucions seran (0, ys) i (0, -ys)
    # aleshores:
    # per Pitàgores,     1) x0² + ys² = r1²
    #             i      2) x1² + ys² = r2²
    #       1) - 2)      3) x0² - x1² = r1² - r2²
    # també coneixem d = + sqrt( (c1x - c2x)² + (c1y - c2y)² )
    # per construcció x1 > x0, per tant  4)  d  = x1 - x0
    #                   
    # aleshores, de 4) obtinc x1 = d + x0.
    # substitueixo x1 a 3 i trobo x0² - (d + x0)² = r1² - r2²
    #                             x0² - d² -2 d x0 - x0² = r1² -r2²
    # per tant x0 = (r2² - r1² - d²) / (2 d)
    #          x1 = d + x0
    #       i  ys = + sqrt( r1² - x0² )
    #
    # ja tinc, doncs, (x0, 0), (x1, 0), (0, ys) i (0, -ys)
    #
    # pas 2. Rotació 
    # aleshores cal fer una rotació sobre (0,0) dels punts sol·lució.
    # Aquesta rotació ha de fer que el cercle de radi r1 amb centre a (x0,0)
    # quedi a la mínima distància del cercle de radi r1 centrat a (c1x, c1y);
    # amb aquesta mateixa rotació, el cercle de radi r2 amb centre (x1, 0)
    # també queda a la mínima distància del cercle de radi 2 centrat a (c2x, c2y)
    # aquest angle A ve determinat pel vector director de la recta que uneix c1 i c2
    # aleshores, cal aplicar la rotació A a la sol·lució. Les solucions rotades són
    # (x0r, y0r), (x1r, y1r), (xs1r, ys1r), (xs2r, y2sr).
    # 
    # pas 3. finalment, traslacionar les solucions a la posició original.
    # La traslació a aplicar és la que converteix els punts
    # (x0r, y0r) en (c1x, c1y) i  (x1r, y1r) en (c2x, c2y)
    # per tant les equacions de la traslació són :
    # xt = x + c1x - x0r ; o l'equivalent per Cond1) xt = x + c2x - x1r    
    # yt = y + c1y - y0r ; o l'equivalent per Cond2) yt = y + c2y - y1r
    #
    # Per tant, la sol·lució final és :
    # punt 1:
    # xst1r = xs1r + c1x - x0r
    # yst1r = ys1r + c1y - y0r 
    #
    # punt 2:
    # xst2r = xs2r + c1x - x0r
    # yst2r = ys2r + c1y - y0r 

    # pas 1. solució a l'escenari simplificat
    d = distancia(c1, c2)
    x0 = (pow(r2, 2) - pow(r1, 2) - pow(d, 2)) / (2 *d)
    x1 = d + x0
    ys = math.sqrt( pow(r1, 2) - pow(x0, 2) )

    cs1 = [x0, 0]
    cs2 = [x1, 0]
    s1 = [0, ys]
    s2 = [0, -ys]

    # qui és qui?
    #rr1 = math.hypot(x0, ys)
    #rr2 = math.hypot(x1, ys)
    #epsilon = 1e-5
    #if math.fabs(r1 - rr1) < epsilon:
    #    cs1 = [x0, 0]
    #    cs2 = [x1, 0]
    #else:
    #    print "reordena"
    #    cs1 = [x1, 0]
    #    cs2 = [x0, 0]

    print "centres simplificada: (%f, %f), (%f, %f)" % (cs1[0],cs1[1],cs2[0],cs2[1])
    print "solucions simplificada: (%f, %f), (%f, %f)" % (s1[0],s1[1],s2[0],s2[1])
        
    # pas 2. rotar
    # l'angle ve donat pel vector director que va de c1 a c2
    v = vectorDirector(c1, c2)
    print "vector director : (%f, %f)" % (v[0], v[1])
    
    A = math.atan2(v[1], v[0])
    print "rotació angle: %f" % A

    sr1 = rotacio(s1, A)
    sr2 = rotacio(s2, A)
    csr1 = rotacio(cs1, A)
    csr2 = rotacio(cs2, A)
    print "centres rotats: (%f, %f), (%f, %f)" % (csr1[0],csr1[1],csr2[0],csr2[1])
    print "solucions rotades: (%f, %f), (%f, %f)" % (sr1[0],sr1[1],sr2[0],sr2[1])

    v2 = vectorDirector(csr1, csr2)
    print "vector director sol·lució : (%f, %f)" % (v2[0], v2[1])

    # translació
    delta = [csr1[0] - c1[0], csr1[1] - c1[1]]
    csrt1 = translacio(csr1, delta)
    csrt2 = translacio(csr2, delta)
    srt1 = translacio(sr1, delta)
    srt2 = translacio(sr2, delta)

    # mostrar resultats
    print "El problema té dues solucions: "
    print "El cercle amb centre (%f, %f) i radi %f" % (csrt1[0], csrt1[1], r1)
    print "talla el cercle amb centre (%f, %f) i radi %f" % (csrt2[0], csrt2[1], r2)   
    print "als punts (%f, %f) i (%f, %f)" % (srt1[0], srt1[1], srt2[0], srt2[1])

    print "Comprovació:"
    print "distància centre (%f, %f) i radi %f a (%f, %f) : %f" % (csrt1[0], \
                                                                   csrt1[1], \
                                                                   r1, \
                                                                   srt1[0], \
                                                                   srt1[1], \
                                                                   distancia(csrt1, srt1))

    print "distància centre (%f, %f) i radi %f a (%f, %f) : %f" % (csrt1[0], \
                                                                   csrt1[1], \
                                                                   r1, \
                                                                   srt2[0], \
                                                                   srt2[1], \
                                                                   distancia(csrt1, srt2))

    print "distància centre (%f, %f) i radi %f a (%f, %f) : %f" % (csrt2[0], \
                                                                   csrt2[1], \
                                                                   r2, \
                                                                   srt1[0], \
                                                                   srt1[1], \
                                                                   distancia(csrt2, srt1))

    print "distància centre (%f, %f) i radi %f a (%f, %f) : %f" % (csrt2[0], \
                                                                   csrt2[1], \
                                                                   r2, \
                                                                   srt2[0], \
                                                                   srt2[1], \
                                                                   distancia(csrt2, srt2))

def translacio(p, delta):
    xt = p[0] - delta[0]  
    yt = p[1] - delta[1]

    return [xt, yt]   
   
def rotacio(p, b):
    prx = p[0] * math.cos(b) - p[1] * math.sin(b)
    pry = p[0] * math.sin(b) + p[1] * math.cos(b)
    
    return [prx, pry]
    
if __name__ == "__main__":
    print "Càlcul dels punts de tall entre dos cercles"
    print "-------------------------------------------"

    # dades del problema
    
    # centres
    c1 = [1.0, 0.0]
    c2 = [ 6.0, 0.0]

    # radis dels cercles
    r1 = 5.0
    r2 = 4.0

    print "Dades del problema :"
    print "Cercle 1. centre : (%f, %f) ; radi : %f" % (c1[0], c1[1], r1)
    print "Cercle 2. centre : (%f, %f) ; radi : %f" % (c2[0], c2[1], r2)   

    # analitza casos
    analitza(c1, r1, c2, r2)

