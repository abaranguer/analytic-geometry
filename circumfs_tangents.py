#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

'''
Es demana calcular els centres Ct1, Ct2...  de les circumf. de radi Rt,
tangents amb la circumf. amb centre a C1 de radi R1 i amb la circumf
amb centre a C2 de radi R2; i els punts de tangència.

Anàlisi

Sigui d = distància(c1 , c2)

Si d = 0 aleshores c1 i c2 són concènctrics

    Sigui r2 > r1 aleshores

    cas 0 : si rt = (r2 - r1) / 2 el problema té infinites solucions.

        Els centres ct de les circumferències de radi rt es situen sobre la
        circumferència amb centre a cs = c1 = c2 i radi r1 + rt

        Paramètricament, sigui alfa variant entre 0 i 2*pi

        aleshores sigui cs = c1 = (c1x, c1y)
        una solució particular ct0 = (ct0x, ct0y) ve donada per :
        ct0x = c1x + (r1 + rt) * cos(alfa)
        ct0y = c1y + (r1 + rt) * sin(alfa)

        Aleshores, donada una circumferència ct0 situada sobre la
        circumferència cs (cs1, csy), els punts de tangència pt1 i pts
        venen donats per

        p1 :
        p1x = ct0x + rt * cos(alfa)
        p1y = ct0y + rt * sin(alfa)

        p2 :
        p2x = ct0x + rt * cos(alfa + pi)
        p2y = ct0y + rt * sin(alfa + pi)

    cas 1: si rt <> (r2 - r1) / 2 el problema no té solució


Si d > 0 aleshores d1 i d2 no són concèntrics

    cas 2 : si r1 + r2 = d, aleshores c1 i c2 són tangents externes
    i té dues solucions

    cas 3 : si r1 + d = r2, aleshores c1 és interna i tangent a c2

    cas 4 : si r2 + d = r1, aleshores c2 és interna i tangent a c1

    cas 5 : si r1 + r2 < d, aleshores c1 i c2 són extenes l'una a l'altre
    Si r1 + rt > d i r1

    cas 6 : si r1 + r2 > d, aleshores c1 i c2 són secants

    cas 7 : si r1 + d < r2, aleshores c1 és interna a c2

    cas 6 : si r2 + d < r1, aleshores c2 és interna a c1


Els casos es poden reduir a la solució del problema de calcular els angles
d'un triangle (A, B, C) coneguda la longituds dels tres costats (a, b, c)

Sigui A angle entre b i c; B angle entre a i c; C angle entre a i b.

Aleshores
cos A = (b² + c² - a²) / (2bc)
cos B = (a² + c² - b²) / (2ac)
cos C = (a² + b² - c²) / (2ab)
'''

def distancia(c1, c2):
    d = math.sqrt(pow((c1[0] - c2[0]), 2) + pow((c1[1] - c2[1]), 2))
    return d

def son_externs(c1, r1, c2, r2):
    ret = False

    d = distancia(c1 , c2)

    if (r1 + r2) < d :
        ret = True

    return ret

def son_tangents_exteriors(c1, r1, c2, r2):
    ret = False

    d = distancia(c1 , c2)

    if (d > 0) and ((r1 + r2) == d) :
        ret = True

    return ret

def son_secants(c1, r1, c2, r2):
    ret = False

    d = distancia(c1 , c2)


    if (d > 0) and (d > r1) and (d > r2) and ((r1 + r2) > d) :
        ret = True

    return ret

def es_c1_tangent_interior_a_c2(c1, r1, c2, r2):
    ret = False

    d = distancia(c1 , c2)


    if (d > 0) and (r2 == (d + r1)):
        ret = True

    return ret


def es_c2_tangent_interior_a_c1(c1, r1, c2, r2):
    ret = False

    d = distancia(c1 , c2)


    if (d > 0) and (r1 == (d + r2)):
        ret = True

    return ret

def es_c1_interior_no_concentrica_a_c2(c1, r1, c2, r2):
    ret = False

    d = distancia(c1 , c2)


    if (d > 0) and (r2 > (d + r1)):
        ret = True

    return ret

def es_c2_interior_no_concentrica_a_c1(c1, r1, c2, r2):
    ret = False

    d = distancia(c1 , c2)


    if (d > 0) and (r1 > (d + r2)):
        ret = True

    return ret

def es_c1_interior_concentrica_a_c2(c1, r1, c2, r2):
    ret = False

    d = distancia(c1 , c2)


    if (d == 0) and (r2 > r1):
        ret = True

    return ret

def es_c2_interior_concentrica_a_c1(c1, r1, c2, r2):
    ret = False

    d = distancia(c1 , c2)


    if (d == 0) and (r1 > r2):
        ret = True

    return ret

def c1_igual_c2(c1, r1, c2, r2):
    ret = False

    d = distancia(c1 , c2)


    if (d == 0) and (r1 == r2):
        ret = True

    return ret


def translacio(p, t):
    xt = p[0] - t[0]  
    yt = p[1] - t[1]

    return [xt, yt]   


def desfer_translacio(p, t):

    return translacio(p, -t)   


def rotacio(p, b):
    prx = p[0] * math.cos(b) - p[1] * math.sin(b)
    pry = p[0] * math.sin(b) + p[1] * math.cos(b)
    
    return [prx, pry]

def reduccio(c1, c2):
    ct = [c2[0] - c1[0], c2[1] - c1[1]] 
    
    # angle rotat, a partir de la diferència entre p1 i p2,
    # o, més senzill, fent servir un dels punts translacionats 
    angle = math.atan2(ct[1], ct[0])
    angle_rotacio =  (math.pi * 0.5) - angle
    
    cr1 = [0,0]
    cr2 = rotacio(ct, angle_rotacio)
    
    return [cr1, cr2]


def solucio_casos_2_5_reduits(c1, r1, c2, r2, rt):
    a = distancia(c1, c2)
    b = r1 + rt
    c = r2 + rt

    angle_bc = math.acos( (pow (b, 2) + pow(c, 2) - pow(a, 2)) / (2 * b *c ) )
    angle_ac = math.acos( (pow (a, 2) + pow(c, 2) - pow(c, 2)) / (2 * a *c ) )
    angle_ab = math.pi - angle_bc  - angle_ac

    csx = (r1 + rt) * math.cos(angle_ab)
    csy = (r1 + rt) * math.sin(angle_ab)

    pt1x = r1 * math.cos(angle_ab)
    pt1y = r1 * math.sin(angle_ab)
    pt2x = c2[1] - r2 * math.cos(angle_ac)
    pt2y = r2 * math.sin(angle_ac)

    return ((csx, csy), (csx, -csy),
            (pt1x, pt1y), (pt1x, -pt1y),
            (pt2x, pt2y), (pt2x, -pt2y))

if __name__ == "__main__":
    print "Càlcul de circumferències tangents a dues circumferències"
    print "---------------------------------------------------------\n"
    print "Dades: "
    print " c1 i c2, centres d eles circumferències"
    print " r1 i r2, radis respectius"
    print " rt, radi de la circumferència tangent"
    print "Solució: "
    print " centres de les circumferències tangents"
    print " punts de tangència"

    # dades del problema
    # punts
    c1 = [1.0, 1.0]
    c2 = [10.0, 10.0]
    r1 = 5.0
    r2 = 3.0
    rt = 12.0

    print "\nDades del problema :"
    print "Circumf. 1 : (%f, %f), radi : %f " % (c1[0], c1[1], r1)
    print "Circumf. 2 : (%f, %f), radi : %f" % (c2[0], c2[1], r2)
    print "Radi circumf. tangent: %f" % rt


    # cercles iguals
    if c1_igual_c2(c1, r1, c2, r2):
        print "Les dues circumferències són iguals." 
        
    
    if es_c1_interior_concentrica_a_c2(c1, r1, c2, r2) or es_c2_interior_concentrica_a_c1(c1, r1, c2, r2):
        if rt <> ((r1 + r2) / 2):
            if es_c1_interior_concentrica_a_c2(c1, r1, c2, r2):
                print "C1 és concèntrica a C2. Rt diferent de (r1 + r2) / 2. No té solucions"
            else:
                print "C2 és concèntrica a C1. Rt diferent de (r1 + r2) / 2. No té solucions"        
        else:
            if es_c1_interior_concentrica_a_c2(c1, r1, c2, r2):
                print "C1 és concèntrica a C2. Rt igual a (r1 + r2) / 2. Té infinites solucions"
            else:
                print "C2 és concèntrica a C1. Rt igual a (r1 + r2) / 2. Té infinites solucions"
                
            print "La circumferència amb centre a (%f, %f) de radi rs = %f" % (c1[0], c1[1], r1 + ((r1 + r2) / 2))
            print "és el lloc geomètric de les solucions.\n"
            print "Donat un anle alfa, amb alfa variant entre 0 i 2*Pi"
            print "els centres de les solucions venen donats per "
            print "    Csx _= %f + %f * cos(alfa)" % (c1[0], r1 + ((r1 + r2) / 2))
            print "    Csy _= %f + %f * sin(alfa)" % (c1[1], r1 + ((r1 + r2) / 2))
            print "i els punts de tangència, per :"
            print "    Pt1x = %f + %f * cos(alfa)" % (c1[0], r1)
            print "    Pt1y = %f + %f * sin(alfa)" % (c1[1], r1)            
            print "    Pt2x = %f + %f * cos(alfa)" % (c1[0], r2)
            print "    Pt2y = %f + %f * sin(alfa)" % (c1[1], r2)
    
