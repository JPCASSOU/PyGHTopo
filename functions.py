# -*-coding:utf-8 -*
import sys
from math import *
from types_donnees import *
from datetime import *



def AfficherMessage(Msg):
    print(Msg)

# un Trim
def Trim(S):
    Q = S.rstrip('\r\n\t ')
    return Q.lstrip('\r\n\t ')
#--- END PROC --------------------
     

def Conv(v):
    return v
#--- END PROC --------------------
        

def SortCompare(elem1,elem2):
    if (elem1 < elem2):
        return -1
    if elem1>elem2:
        return 1
    return 0
#--- END PROC --------------------
        

def skip_duplicates(iterable, key=lambda x: x): 
    # on va mettre l'empreinte unique de chaque element dans ce set
    fingerprints = set()
    for x in iterable:
        # chaque element voit son emprunte calculee. Par defaut l empreinte
        # est l element lui mÃªme, ce qui fait qu'il n'y a pas besoin de
        # specifier 'key' pour des primitives comme les ints ou les strings.
        fingerprint = key(x)
 
        # On verifie que l empreinte est dans la liste des empreintes  des
        # elements precedents. Si ce n'est pas le cas, on yield l element, et on
        # rajoute sont empreinte ans la liste de ceux trouves, donc il ne sera
        # pas yielde si on ne le yieldera pas une seconde fois si on le
        # rencontre a nouveau
        if fingerprint not in fingerprints:
            yield x
            fingerprints.add(fingerprint)
#--- END PROC --------------------
        

def strip_duplicates(iterable, equals=lambda x, y: x == y):
 
    # On transforme l iterable en iterateur sur lui mÃªme, cela va nous
    # permettre d appeler next() dessus et recuperer le premier element,
    # mÃªme sur un objet non indexable (sur lequel on ne peut utiliser [0])
    iterable = iter(iterable)
 
    res = []
    # Une petite boucle infinie est necessaire car la boucle 'for' ne nous
    # permet pas de recuperer le premier element independamment des autres,
    # et la boucle 'while' attend une condition de sortie, ce que nous n'avons
    # pas forcement (il n'est pas possible de verifier le nombre d elements
    # restant dans un generateur).
    while True:
 
        # on recupere le premier element de l iterable restant, si il n'y en
        # a plus, on sort de la boucle.
        try:
            elem = next(iterable)
        except StopIteration:
            break
 
        # Le premier element est ajoute au resultat sans doublons. Maintenant
        # on va recreer l iterable, mais en retirant tout ce qui etait egal
        # au premier element. Notez que 'Ãªtre egal  est une condition modifiable
        # en passant une fonction en parametre, comme l etait 'key' precedemment.
        res.append(elem)
 
        iterable = iter([x for x in iterable if not equals(elem, x)])
 
    return res
#--- END PROC --------------------
        

def GradToRad(X):
    return X * pi / 200
#--- END PROC --------------------
        

def DegToRad(X):
    return X * pi / 180
#--- END PROC --------------------
        

def rgb(R, G, B):
    return B + 256 * G + 65536 * R
#--- END PROC --------------------
        
    
# retourne un azimut
def GetAzimut(dx, dy, Unite):
    a = atan2(dy, dx) # la fonction atan2 est protegee contre les dx = 0
    if (a < 0):
        a = a + 2 * pi;
    a = 0.50 * pi - a;
    if (a < 0):
        a = a + 2 * pi;
    return a * 0.50 * Unite / pi
#--- END PROC --------------------
        

    
    # retourne la longueur, direction et pente pour dx, dy, dz
def GetBearingInc(dx, dy, dz, fUB, fUC):
    dp  = hypot(dx, dy)
    Result = TLongAzP()
    Result.oLongueur = hypot(dp, dz)
    Result.oAzimut   = GetAzimut(dx, dy, fUB)
    Result.oPente    = atan2(dz, dp) * 0.5 * fUC / pi
    return Result
#--- END PROC --------------------
        
    
#  calcul des accroissements pour une visee
# OK
def CalculerUneVisee(MaVisee, QUniteAzimut, QUnitePente, QDeclinaison, QInclinaison):
    # NOTA: TOUJOURS INITIALISER LES VARIABLES
    TWOPI  = 2 * pi
    PI_2   = pi / 2
    PI_180 = pi / 180    
    PI_200 = pi / 200    
    ubb = floor(QUniteAzimut)
    ucc = floor(QUnitePente)
    udd = 400.00;
    RX = 0.00
    RY = 0.00
    RZ = 0.00
    LP = 0.00
    UC = 0.00
    UB = 0.00
    if (ubb == 359) or (ubb == 360): #  visees directes en degres
        UB  = TWOPI / 360
        Az1 = MaVisee.Azimut * UB + QDeclinaison  * PI_180
    elif (ubb == 399) or (ubb == 400): #  visees directes en grades
        UB  = TWOPI / 400
        Az1 =MaVisee.Azimut * UB + QDeclinaison  * PI_200
    elif (ubb == 349) or (ubb == 350): #  visees inverses en degres
        UB  = TWOPI / 360
        Az1 = MaVisee.Azimut * UB + QDeclinaison  * PI_180
        Az1 = pi + Az1
    elif (ubb == 389) or (ubb == 390): #  visees inverses en grades
        UB  = TWOPI / 400
        Az1 = MaVisee.Azimut * UB + QDeclinaison  * PI_200
        Az1 = pi + Az1
    else:
        UB  = TWOPI / 360
        Az1 = MaVisee.Azimut * UB + QDeclinaison  * PI_180
        
    # Determiner si on travaille en zenithal*)
    ucc = floor(QUnitePente)
    # Correction erreurs systematiques des pentes
    CorrectionPenteInRadians = GradToRad(QInclinaison / 10.00)
    if (ucc == 360) or (ucc == 400): # zero a l horizontale
        UC  = TWOPI / ucc
        Pente1 = CorrectionPenteInRadians + MaVisee.Pente  * UC
        LP = MaVisee.Longueur * cos(Pente1)
        RX = LP * sin(Az1)
        RY = LP * cos(Az1)
        RZ = MaVisee.Longueur * sin(Pente1)
    elif (ucc == 361) or (ucc == 401): # zero zenithal
        UC = TWOPI/(ucc - 1)
        Pente1 = PI_2 - (CorrectionPenteInRadians + MaVisee.Pente * UC)
        LP = MaVisee.Longueur * cos(Pente1)
        RX = LP * sin(Az1)
        RY = LP * cos(Az1)
        RZ = MaVisee.Longueur * sin(Pente1)
    elif (ucc == 359) or (ucc == 399): # zero nadiral
        UC = TWOPI/(ucc + 1)
        LP = MaVisee.Longueur * cos(-(PI_2 - (MaVisee.Pente * UC)))
        RX = LP * sin(Az1)
        RY = LP * cos(Az1)
        Pente1 = -(PI_2 - (CorrectionPenteInRadians + MaVisee.Pente * UC))
        RZ = MaVisee.Longueur * sin(Pente1); # Fixe le 31/05.
    elif (ucc == 370): #DONE: Pourcentages sont exprimes sous la forme 59.11 pour 59.11%
        udd = atan(MaVisee.Pente / 100.0)
        LP  = MaVisee.Longueur * cos(udd)
        RX  = LP * sin(Az1)
        RY  = LP * cos(Az1)
        RZ  = MaVisee.Longueur * sin(udd);
    elif (ucc == 380): # // dans ce mode, les donnees sont 'Longueur VISEE et DENIVELEE
        try:
            LP = sqrt(MaVisee.Longueur * MaVisee.Longueur - MaVisee.Pente * MaVisee.Pente)
            RX = LP * Sin(Az1)
            RY = LP * Cos(Az1)
            RZ = MaVisee.Pente
        except:
            pass
    elif (ucc == 350) or (ucc == 390): # visees inverses en degres/grades (ucc = UniteClino -10);   
        UC     = TWOPI/(ucc + 10)
        Pente1 = CorrectionPenteInRadians - MaVisee.Pente * UC
        LP     = MaVisee.Longueur * cos(Pente1) 
        RX     = LP * sin(Az1)
        RY     = LP * cos(Az1)
        RZ     = MaVisee.Longueur * cos(Pente1)
    elif (ucc == 790) or (ucc == 800): # lasermetre TLM330
        LP     = MaVisee.Longueur #  longueur projetee est dans Long
        RX     = LP * sin(Az1)
        RY     = LP * cos(Az1)
        RZ     = MaVisee.Pente  # denivelee est dans Pente
        # visee inverse ?
        if (ucc == 790):
            RZ = -RZ
    else: # zero horizontal par default
        UC     = TWOPI/360.00
        Pente1 = CorrectionPenteInRadians + MaVisee.Pente * UC
        LP = MaVisee.Longueur * cos(Pente1)
        RX = LP * sin(Az1)
        RY = LP * cos(Az1)
        RZ = MaVisee.Longueur * sin(Pente1)
    #==============
    MaVisee.QDeltaX = RX
    MaVisee.QDeltaY = RY
    MaVisee.QDeltaZ = RZ
    MaVisee.QLongDev = sqrt(RX ** 2 + RY ** 2 + RZ ** 2) 
    return MaVisee
#--- END PROC --------------------
        
#---------------------------------------------------------------------------------------------------------    
def IIF(Cond, VT, VF):
    if (Cond):
        return VT
    else:   
        return VF
#--- END PROC --------------------
        
#----------------------------------------------------------------------------------------------------------
def ProduitVectoriel(Vect1, Vect2, Normalized):
    V = TPoint3Df(Vect1.Y * Vect2.Z - Vect1.Z * Vect2.Y, \
                  Vect1.Z * Vect2.X - Vect1.X * Vect2.Z, \
                  Vect1.X * Vect2.Y - Vect1.Y * Vect2.X)
    # if (Normalized):
    r = sqrt(V.X ** 2 + V.Y ** 2 + V.Z ** 2) + 1E-18
    V.X = V.X / r
    V.Y = V.Y / r
    V.Z = V.Z / r
    return V
#--- END PROC --------------------
        
#----------------------------------------------------------------------------------------------------------
# calcul de l'angle bissecteur de deux segments
def CalculerAngleBissecteur(dX1, dY1, dX2, dY2):
    V1 = TPoint3Df(dX1, dY1, 0.00)
    V2 = TPoint3Df(dX2, dY2, 0.00)
    W  = TPoint3Df(0.00, 0.00, 1.00) 
    # produits vectoriels
    V1 = ProduitVectoriel(V1, W, True)
    V2 = ProduitVectoriel(V2, W, True)
    #composition Vectorielle
    W.X = V1.X + V2.X 
    W.Y = V1.Y + V2.Y
    W.Z = V1.Z + V2.Z
    # angles
    return atan2(W.Y+1E-12, W.X +1E-12)
#--- END PROC --------------------
        
#--------------------------------------------------------------------------
# ID station
def GetIDStation(N, St: TStation):
  miaou = Trim(St.IDTerrainStation)
  if (miaou == ""):
    return "%d.%d" % (N, St.NumPoint)
  else:
    return miaou
#--- END PROC --------------------
        
#-----------------------------------------
# wrappers pour dates
def GetSecuredDate(Y, M, D):
    return datetime(Y, M, D)
#--- END PROC --------------------
        
#--------------------------------------------------------------------------
    
