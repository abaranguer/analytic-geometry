#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

# es demana calcular el centre C (cx, cy) del cercle que passa per tres punts P0, P1, P2
# P0 (x0, y0)
# P1 (x1, y1)
# P2 (x2, y2)
#
# anàlisi del problema :
#
# cas 1:
# 1) Els tres punts són iguals : tots els punts del plà són sol·lució. Infinites sol·lucions.
# 2) Els tres punts estan alineats : el problema no té sol·lució
# 3) Dos  punts són iguals, i el tercer diferent : o sigui, cercle que passa per dos punts.
#     té infinites sol·lucions que es troben a la recta que equidista entre els dos punts
# 4) Tres punts diferents. Té solució única
#
# Sol·lució al cas 1.
# Trivial.
# Si P0 = P1 = P2 = (x0, y0)
# aleshores donat un punt C qualsevol (x1, y1), el cercle determinat per
# (x - x1)² + (y - y1)² = (x1 -x0)² + (y1 - y0)² passa per P0 = P1 = P2
#
# Solució al cas 2
# Per verificar si els tres punts estan alineats potser el més senzill és comprovar
# que el punt P2 pertany a la recta  determinada per P0-P1
# és dir, que P2 = P0 + L * v  
# on v el vector director de la recta entre P0 i P1.
# paramètricament :
# a)   x2 = x0 + L * (x0 - x1)  --> L = (x2 - x0) / (x0 - x1)
# b)   y2 = y0 + L * (y0 - y1)  --> L = (y2 - y0) / (y0 - y1)
# Si L calculada per a) coincideix amb L calculdada per b), aleshores els tres punts 
# estan alineats i es pot afirmar que no té sol·lució
#
# Sol·lució al cas 3
# Siguin dos punts P0 (x0, y0) i P1(x1, y1)
# aleshores la recta que equidista de tots dos és la recta de vector director
# perpendicular al vector director definit per P0 i P1
# i que passa pel punt mig entre P0 i P1
# Punt mig Pm = (Pmx, Pmy) = ((x1 - x0) / 2, (y1 - y0) /2)
# Vector director Entre P0 i P1 es v = (vx, vy) = (x1 - x0, y1 - y0)
# i el vector director perpendicular és vp  = (vpx, vpy) =  (y0 - y1, x1 - x0)
# per tant, la recta és, en format paramètric :
#  x = pmx + L * vpx
#  y = pmy + L * vpy
#
# o desenvolupat :
#
# x = ((x1 -x0) / 2) + L * (y0 - y1)
# y = ((y1 -y0) / 2) + L * (x1 - x0)
#
# Sol·lució al cas 4
# Es pot resoldre plantejant un sistema d'equacions amb dues incògnites (xc, yc)
# que corresponen a les coordenades del centre del cercle que passa per P0, P1 i P2. Sigui
# a) (x - x0)² + (y - y0)² = r²
# b) (x - x1)² + (y - y1)² = r²
# c) (x - x2)² + (y - y2)² = r²
#
# desenvolupo :
#
# a) x² - 2 x x0 + x0² + y² - 2 y y0 + y0² = r²
# b) x² - 2 x x1 + x1² + y² - 2 y y1 + y1² = r²
# c) x² - 2 x x2 + x2² + y² - 2 y y2 + y2² = r²
#
# a) - b)   - 2 x x0 + 2 x x1 + x0² - x1² - 2 y y0 + 2 y y1 + y0² - y1² = 0
# a) - c)   - 2 x x0 + 2 x x2 + x0² - x2² - 2 y y0 + 2 y y2 + y0² - y2² = 0
#
# reordeno :
#
#  - 2 x x0 + 2 x x1  - 2 y y0 + 2 y y1 = y1² -  y0² - x0²  + x1²
#  - 2 x x0 + 2 x x2  - 2 y y0 + 2 y y2 = y2² -  y0² - x0²  + x2²
#
# 2 x (x1 - x0) + 2 y (y1 - y0) = x1² + y1² - (x0² + y0²) 
# 2 x (x2 - x0) + 2 y (y2 - y0) = x2² + y2² - (x0² + y0²)
#
# Siguin :  
# A = 2 (x1 - x0)
# B = 2 (y1 - y0)
# C = 2 (x2 - x0)
# D = 2 (y2 - y0)
# R1 = x1² + y1² - (x0² + y0²)
# R2 = x2² + y2² - (x0² + y0²)
# 
# Aleshores, per la regla de Cramer, la sol·lució és :
# x = (R1 * D - C * R2) / (A * D - B * C) 
# y = (A * R2 - R1 * B) / (A * D - B * C)

def distancia(p1, p2):
    d = math.sqrt(pow((p1[0] - p2[0]), 2) + pow((p1[1] - p2[1]), 2))
    
    return d

def puntMig(p1, p2):     
    cx = (p1[0] + p2[0]) / 2.0 
    cy = (p1[1] + p2[1]) / 2.0

    return [cx, cy]

def analitza(p0, p1, p2):
    if p0 == p1 and p0 == p2:
        print "Els tres punts són iguals. P0 = P1 = P2"
        print "Infinites sol·lucions."
        print "Donat un punt C (x1, y1) qualsevol diferent de P0" 
        print "És sol·lució el cercle determinat per "
        print "(x - x1)² + (y - y1)² = (x1 - %f)² + (y1 - %f)²" % (p0[0], p0[1])
        exit(0)

    if ((p0 == p1) and (p0 != p2)) or \
       ((p0 == p2) and (p0 != p1)) or \
       ((p1 == p2) and (p0 != p1)):
        print "Dos punts iguals i un de diferent."
        print "Es tracta del problema de trobar els centres i radis dels cercles "
        print "que passen per dos punts Pa i Pb."
        print "Infinites sol·lucions."
        print "Els centres dels cercles sol·lució es troben a la recta que equidista entre Pa i Pb."
        print "Donat un punt Ps sobre aquesta recta, el radi del cercle buscat "
        print "és la distància entre Pa i Ps (o entre Pb i Ps)."
        if p0 == p1:
            pa = p0
            pb = p2

        if (p0 == p2) or (p1 == p2): 
            pa = p0
            pb = p1

        cerclePerDosPunts(pa, pb)
        exit(0)

    if tresPuntsAlineats(p0, p1, p2):
        print "Els tres punts estan alineats. No hi ha sol·lució"
        exit(0)
    else:
        cerclePerTresPunts(p0, p1, p2)
        exit(0)

def cerclePerTresPunts(p0, p1, p2):
    A = 2.0 * (p1[0] - p0[0])
    B = 2.0 * (p1[1] - p0[1])
    C = 2.0 * (p2[0] - p0[0])
    D = 2.0 * (p2[1] - p0[1])
    R1 = pow(p1[0],2) + pow(p1[1],2) - (pow(p0[0],2) + pow(p0[1],2))
    R2 = pow(p2[0],2) + pow(p2[1],2) - (pow(p0[0],2) + pow(p0[1],2))
    # 
    # Aleshores, per la regla de Cramer, la sol·lució és :
    c = [(R1 * D - B * R2) / (A * D - B * C), (A * R2 - R1 * C) / (A * D - B * C)]
    r = distancia(c, p0)

    print "Sol·lució : "
    print "cercle de radi %f" % r
    print "amb centre a (%f, %f)" % (c[0], c[1])
    print "Comprovació: "
    print "distància entre (%f, %f) i (%f, %f) és %f" % (p0[0], p0[1], c[0], c[1], distancia(p0, c))
    print "distància entre (%f, %f) i (%f, %f) és %f" % (p1[0], p1[1], c[0], c[1], distancia(p1, c))
    print "distància entre (%f, %f) i (%f, %f) és %f" % (p2[0], p2[1], c[0], c[1], distancia(p2, c))
        
def tresPuntsAlineats(p0, p1, p2):
    # Per verificar si els tres punts estan alineats potser el més senzill és comprovar
    # que el punt P2 pertany a la recta  determinada per P0-P1
    # és dir, que P2 = P0 + L * v  
    # on v el vector director de la recta entre P0 i P1.
    # paramètricament :
    # a)   x2 = x0 + L * (x1 - x0)  --> L = (x2 - x0) / (x1 - x0)
    # b)   y2 = y0 + L * (y1 - y0)  --> L = (y2 - y0) / (y1 - y0)
    # Per tant, si (x2 - x0)(y1 - y0) = (y2 - y0)(x1 -x0)
    # aleshores els tres punts estan alineats i es pot afirmar que no té sol·lució

    L1 = (p2[0] - p0[0]) * (p1[1] - p0[1])
    L2 = (p2[1] - p0[1]) * (p1[0] - p0[0])

    return (L1 == L2)
    
def cerclePerDosPunts(p0, p1):
    # La recta que equidista de tots dos és la recta de vector director
    # perpendicular al vector director definit per P0 i P1
    # i que passa pel punt mig entre P0 i P1
    # Punt mig Pm = (Pmx, Pmy) = ((x1 - x0) / 2, (y1 - y0) /2)
    # Vector director Entre P0 i P1 es v = (vx, vy) = (x1 - x0, y1 - y0)
    # i el vector director perpendicular és vp  = (vpx, vpy) =  (y0 - y1, x1 - x0)
    # per tant, la recta és, en format paramètric :
    #  x = pmx + L * vpx
    #  y = pmy + L * vpy
    #
    # o desenvolupat :
    #
    # x = ((x1 -x0) / 2) + L * (y0 - y1)
    # y = ((y1 -y0) / 2) + L * (x1 - x0)

    pm = puntMig(p0, p1)
    print "punt mig entre (%f, %f) i (%f, %f) : (%f, %f)" % (p0[0], p0[1], p1[0], p1[1], pm[0], pm[1])
    print "Recta Rs sol·lució (en forma paramètrica) :"
    print " x = %f + L * %f" % (pm[0], (p0[1] - p1[1])) 
    print " y = %f + L * %f" % (pm[1], (p1[0] - p0[0])) 
    print "Donat un punt C (x1, y1) que pertany a la recta Rs, "
    print "el cercle que pasa pels punts Pa i Pb ve donat per :  "
    print "(x - x1)² + (y - y1)² = (x1 - %f)² + (y1 - %f)²" % (p0[0], p0[1])
    
if __name__ == "__main__":
    print "Càlcul de cercle que passa per tres punts"
    print "-----------------------------------------"

    # dades del problema
    
    # punts
    p1 = [0.0, 0.0]
    p2 = [0.0, 0.0]
    p3 = [2.0, 2.0]

    print "Dades del problema :"
    print "Punt 1 : (%f, %f)" % (p1[0], p1[1])
    print "Punt 2 : (%f, %f)" % (p2[0], p2[1])
    print "Punt 3 : (%f, %f)" % (p3[0], p3[1])
 
    # analitza casos
    analitza(p1, p2, p3)
