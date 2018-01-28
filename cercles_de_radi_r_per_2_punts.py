#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

# es demana calcular els centres c1 i c2
# dels cercles de radi d
# que passen per dos punts p1 i p2
#
# sigui p1 = [x1, y1]
# i sigui p2 = [x2, y2]
# sigui d = distancia(p1, p2), i cm = punt_mig(p1, p2)
# d = math.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))
# cm = [cmx, cmy] = [ (x1 + x2) * 0.5, (y1 + y2) * 0.5 ]
# Si d = 0, aleshores els dos punts son el mateix punt p = p1 = p2
# i té infinites solucions. que corresponen als punts
# del cercle de radi rc centrat al punt p
# si rc < (d / 2), aleshores no té solució
# si rc = (d / 2), aleshores solució única i la solució és el punt mig
# entre els punts donats
# si rc > (d / 2) aleshores té dues solucions.
#
# La solució del problema es pot construir
# a partir de la solució del problema equivalent de trobar els cercles que
# passen per dos punts equidistants de (0,0)
# sobre l'eix Y, separats la distància d.
#
# per a construir el sistema equivalent simplificat, he de fer
# - un canvi d'eixos, o una translació
# - una rotació entorn de l'origen
#
# El canvi d'eixos
# ----------------
#
# El canvi d'eixos (x,y) --> (xt, yt) ve donat per la translació del punt mig cm
# a l'origen de coordenades
# 
# sigui P=[x, y] i Pt = [xt, yt], aleshores podem definir la funció translació
# Pt = translació(P, cm)
#
# xt = x - cmx  
# yt = y - cmy
#
# La translació de tornada, no es més que aplicar la translació amb signe canviat
# P = translació_tornada(Pt, cm)
#
# x = xt + cmx
# y = yt + cmy
#
# de forma que 
#
# O = translacio(cm, cm)
# - cm --> O --> [0, 0]
# p1t = translacio(p1, cm)
# - p1 --> p1t --> [p1tx, p1ty] = [x1 - cmx, y1 - cmy]
# p2t = translacio(p2, cm)
# - p2 --> p2t --> [p2tx, p2ty] =  [ x2 -cmx, y2 - cmy]
#
# La rotació
# ----------
# 
# El següent pas és rotar p1t i p2t fins que coincideixen amb l'eix y
#
# L'angle A que fa la recta que passa per p1t, O i p2t ve donat per l'expressió
# A = math.atan2(p1ty, p1tx)
# per tant cal rotar B =  (pi / 2) - A  amb pi = 4 * math.atan(1)
# i obtenir ptr = rotació(pt, B) 
# La rotació d'un angle B ve donada per la transformació
# ptrx = ptx * math.cos(B) - pty * math.sin(B)
# ptry = ptx * math.sin(B) + pty * math.cos(B)
# 
# o matricialment :
#
#   | ptrx |   | cos(B)  -sin(B)| | ptx|
#   |      | = |                | |    |
#   | ptry |   | sin(B)   cos(B)| | pty|
#
# Com la rotació va a buscar l'eix de les Y, i la rotació no altera les distancies entre punts
# aleshores, els punts rotats són:
# p1trx = [0, d * 0.5]
# p2trx = [0, -d * 0.5]
#
# Després de la rotació, la solució és trivial (Pitàgores) : el centre dels cercles de radi Rc
# que passen per p1tr i p2tr es trobaran sobre l'eix x i vindran donats per les expressions
#
# ps1 = [0.5 * math.sqrt( 4 * pow(Rc, 2) - pow(d, 2)), 0]
# ps2 = [ - 0.5 * math.sqrt( 4 * pow(Rc, 2) - pow(d, 2)), 0]
#
# ara cal desfer la rotació de B graus, per tant 
#
# ps1r = rotació(ps1, -B)
# ps2r = rotació(ps2, -B)
#
# i recuperar l'eix de coordenades original desfent la translació,
# trobant amb aquest darrer pas la solució del problema
#
# ps1rt = traslacio_tornada(ps1r, cm)
# ps2rt = traslacio_tornada(ps2r, cm)
#

def distancia(p1, p2):
    d = math.sqrt(pow((p1[0] - p2[0]), 2) + pow((p1[1] - p2[1]), 2))
    return d

def puntMig(p1, p2):     
    cx = (p1[0] + p2[0]) / 2.0 
    cy = (p1[1] + p2[1]) / 2.0

    return [cx, cy]

def analitza(d, Rc, p, cm):
    # Si d = 0, aleshores els dos punts son el mateix punt p = p1 = p2
    # i té infinites solucions. que corresponen als punts
    # del cercle de radi rc centrat al punt p
    # si rc < (d / 2), aleshores no té solució
    # si rc = (d / 2), aleshores solució única i la solució és el punt mig
    # entre els punts donats
    # si rc > (d / 2) aleshores té dues solucions.

    if d == 0 :
        print "Punt 1 igual al punt 2." 
        print " Té infinites solucions que corresponen als punts"
        print " del cercle de radi %f centrat al punt (%f, %f)" % (Rc, p[0], p[1])
        exit(0)

    if (d * 0.5) == Rc :
        print "distància entre el punt 1 i el punt 2 és igual a dos cops el radi." 
        print " Només té una solució que és el punt mig dels punts 1 i 2"
        print " Solució única :  cercle de radi %f centrat a (%f, %f)" % (Rc, cm[0], cm[1])
        exit(0)
        
    if (d * 0.5) > Rc :
        print "distància entre el punt 1 i el punt 2 és més gran que dos cops el radi." 
        print " No té solució"
        exit(0)

def translacio(p, cm):
    xt = p[0] - cm[0]  
    yt = p[1] - cm[1]

    return [xt, yt]   

def translacioTornada(p, cm):
    xtt = p[0] + cm[0]  
    ytt = p[1] + cm[1]

    return [xtt, ytt]   

def rotacio(p, b):
    prx = p[0] * math.cos(b) - p[1] * math.sin(b)
    pry = p[0] * math.sin(b) + p[1] * math.cos(b)
    
    return [prx, pry]
    
if __name__ == "__main__":
    print "Càlcul de cercle que passa per dos punts i té un radi donat"
    print "-----------------------------------------------------------"

    # dades del problema
    
    # punts
    p1 = [0.0, 3.0]
    p2 = [0.0, -3.0]

    # radi del cercle
    Rc = 5.0

    print "Dades del problema :"
    print "Punt 1 : (%f, %f)" % (p1[0], p1[1])
    print "Punt 2 : (%f, %f)" % (p2[0], p2[1])
    print "Radi : %f" % Rc
 
    # distància entre els dos punts
    d = distancia(p1, p2)

    # punt mig entre els punts donats
    cm = puntMig(p1, p2)

    # analitza casos
    analitza(d, Rc, p1, cm)

    # Si arriba fins aquí, pot procedir
    p1t = translacio(p1, cm)
    p2t = translacio(p2, cm)

    # angle rotat, a partir de la diferència entre p1 i p2,
    # o, més senzill, fent servir un dels punts translacionats 
    A = math.atan2(p1t[1], p1t[0])
    B =  (math.pi * 0.5) - A

    # solucions a l'espai rotat i translacionat
    ps1 = [0.5 * math.sqrt( 4 * pow(Rc, 2) - pow(d, 2)), 0]
    ps2 = [ - 0.5 * math.sqrt( 4 * pow(Rc, 2) - pow(d, 2)), 0]

    # desfer la rotació
    ps1r = rotacio(ps1, -B)
    ps2r = rotacio(ps2, -B)

    # i desfer la translació
    ps1rt = translacioTornada(ps1r, cm)
    ps2rt = translacioTornada(ps2r, cm)

    # mostrar resultats
    print "El problema té dues solucions: "
    print "\nSolució 1 :"
    print "Cercle de radi %f, centrat a (%f, %f)" % (Rc, ps1rt[0], ps1rt[1])
    print "\nSolució 2 :"
    print "Cercle de radi %f, centrat a (%f, %f)" % (Rc, ps2rt[0], ps2rt[1])

    # comprovació
    print "\nComprovació"
    print "distància p1 a centre sol 1 : %f " % distancia(p1, ps1rt)
    print "distància p1 a centre sol 2 : %f " % distancia(p1, ps2rt)
    print "distància p2 a centre sol 1 : %f " % distancia(p2, ps1rt)
    print "distància p2 a centre sol 2 : %f " % distancia(p2, ps2rt)
