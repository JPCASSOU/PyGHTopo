# -*-coding:utf-8 -*
import time
from datetime import date
from functions import *

# CONSTANTES

#types de visée
tgDEFAULT     = 0
tgENTRANCE    = 1
tgFOSSILE     = 2
tgVADOSE      = 3
tgENNOYABLE   = 4
tgSIPHON      = 5
tgFIXPOINT    = 6
tgSURFACE     = 7
tgTUNNEL      = 8
tgMINE        = 9
tgTYPE_ENTITES_VISEES_ANTENNE = 10             


# Rappels sur les equivalences avec les 'record  du Pascal
# - Les membres sont modifiables
# - Le constructeur est indispensable et permet de
#   * definir les membres
#   * les initialiser
#
# couleurs
def rgb(R, G, B):
    return B + 255 * G + 65535 * R
#-----------------------------------------------------------------
class TPoint2Di:
    def __init__(self, QX, QY):
        self.X = QX
        self.Y = QY
#-----------------------------------------------------------------
class TPoint2Df:
    def __init__(self, QX, QY):
        self.X = QX
        self.Y = QY
#-----------------------------------------------------------------
class TPoint3Df:
    def __init__(self, QX, QY, QZ):
        self.X = QX
        self.Y = QY
        self.Z = QZ    
#------------------------------------------------------------------        
class TLongAzP:
    def __init__(self):
        self.oLongueur = 0.00
        self.oAzimut   = 0.00
        self.oPente    = 0.00
        
class TEntree:
    def __init__(self):
        self.eNumEntree = 0
        self.eNomEntree = ""
        self.eXEntree   = 0.00
        self.eYEntree   = 0.00
        self.eZEntree   = 0.00
        self.eRefSer    = 0
        self.eRefSt     = 0
        self.eObserv    = ""
#-----------------------------------------------------------------
class TReseau:
    def __init__(self):
        IdxReseau    = 0
        ColorReseau  = 0
        TypeReseau   = 0
        NomReseau    = ""
        ObsReseau    = ""
# Faible nombre de membres = on instancie avec des valeurs
class TSecteur:
    def __init__(self, IDSecteur, ColR, ColG, ColB, NomSecteur):
        self.IDSecteur = IDSecteur
        self.ColR      = ColR
        self.ColG      = ColG
        self.ColB      = ColB
        self.NomSecteur = NomSecteur
#-----------------------------------------------------------------
class TAntenne:
    def __init__(self):
        self.ID     = 0
        self.Reseau = 0
        self.Secteur= 0
        self.SerDep = 0
        self.PtDep  = 0
        self.Code   = 0
        self.Expe   = 0
        self.IDTerrain = ""
        self.Longueur = 0.00
        self.Azimut   = 0.00
        self.Pente    = 0.00
        self.Commentaire = ""
        X1            = 0.00
        Y1            = 0.00
        Z1            = 0.00
        X2            = 0.00
        Y2            = 0.00
        Z2            = 0.00
        
#-----------------------------------------------------------------
class TCode:
    def __init__(self, IDCode, UAzimut, UPente, PrecLong, PrecAzimut, PrecPente, QCommentaire):
        self.IDCode     = IDCode
        self.UAzimut    = UAzimut
        self.UPente     = UPente
        self.PrecLong   = PrecLong
        self.PrecAzimut = PrecAzimut
        self.PrecPente  = PrecPente
        self.Commentaire= QCommentaire
#-----------------------------------------------------------------
class TExpe:
    def __init__(self):
        #-2	1	28	5	88	CASSOU JP	PIPISTRELLE	0	0.00	0	52	JPC est un gros PD
        self.IDExpe = 0
        self.JourExpe = 1
        self.MoisExpe = 1
        self.AnneeExpe = 2016
        self.Speleometre  = ""
        self.Speleographe = ""
        self.IdxCouleur   = 0
        self.Declinaison = 0.00
        self.Inclinaison = 0.00
        self.Commentaire = ""
        
#-----------------------------------------------------------------
class TStation:
    def __init__(self):
        self.IDStation = 0
        self.Secteur   = 0
        self.TypeVisee = 0
        self.Code = 0
        self.Expe = 0
        self.Longueur = 0.00
        self.Azimut = 0.00
        self.Pente  = 0.00
        self.LG     = 0.00
        self.LD     = 0.00
        self.HZ     = 0.00
        self.HN     = 0.00
        self.Commentaire = ""
        self.IDTerrain   = ""  
        self.QDeltaX     = 0.00
        self.QDeltaY     = 0.00
        self.QDeltaZ     = 0.00
        self.QLongDev    = 0.00
        self.X           = 0.00
        self.Y           = 0.00
        self.Z           = 0.00
        
    def SetValeurs(self, qID, qSecteur, qTypeVisee, qCode, qExpe, qLong, qAz, qP, qLG, qLD, qHZ, qHN, qIDTerrain, qCommentaire):
        self.IDStation = qID
        self.Secteur = qSecteur
        self.TypeVisee = qTypeVisee
        self.Code = qCode
        self.Expe = qExpe
        self.Longueur = qLong
        self.Azimut = qAz
        self.Pente  = qP
        self.LG     = qLG
        self.LD     = qLD
        self.HZ     = qHZ
        self.HN     = qHN
        self.Commentaire = qIDTerrain
        self.IDTerrain   = qCommentaire   
        
# Classe TNoeud
# class TNoeud:
    # def __init__(self):
        # IDNoeud = 0
        # X       = 0.00
        # Y       = 0.00
        # Z       = 0.00
        
#-----------------------------------------------------------------
# Classe TSerie
class TSerie:
    def __init__(self):
        #1	-1	1	0	1	10	10	1	3	GALERIE PRINCIPALE		0	1.02
        self.ClearSerie()
        self.IdxSerie = 0
        self.NomSerie = ''
        self.IdxReseau = 0
        self.IdxEntrance = 0
        self.SerDep = 0
        self.PtDep  = 0
        self.SerArr = 0
        self.PtArr  = 0
        self.NbSts  = 0
        self.Chance = 0
        self.Obstacle     = 0
        self.Commentaires = "Serie0"
    #---------------------------------
    def ClearSerie(self):
        self.FListeStations = []
    #---------------------------------
    # ajout d une station
    def AddStation(self, S):
        self.FListeStations.append(S) 
    #---------------------------------
    # attraper une station
    def GetStation(self, Idx):
        return self.FListeStations[Idx]
    #---------------------------------
    def PutStation(self, Idx, C):
        self.FListeStations[Idx] = C
    #---------------------------------
    def GetNbStations(self):
        return len(self.FListeStations) 

# Classe TJonction
class TJonction:
    def __init__(self):
        NoNoeud     = 0
        IDJonction  = ""
        X           = 0.00
        Y           = 0.00
        Z           = 0.00    
#-----------------------------------------------------------------
# Classe TBranche
class TBranche:
    def __init__(self):
        #1	-1	1	0	1	10	10	1	3	GALERIE PRINCIPALE		0	1.02
        self.ClearBranche()
        NoSerie      = 0
        NoReseau     = 0
        NoeudDepart  = 0
        NoeudArrivee = 0
        Rigidite     = 1.00 # module de raideur, egal Ã  1.00 par defaut
        LongDev      = 0.00 # longueur dÃ©veloppÃ©e
        DeltaX       = 0.00
        DeltaY       = 0.00
        DeltaZ       = 0.00
        XDepart      = 0.00
        YDepart      = 0.00
        ZDepart      = 0.00
        XArrivee     = 0.00
        YArrivee     = 0.00
        ZArrivee     = 0.00
        
    
    #---------------------------------
    def AddStationByValeurs(self,  qSecteur, qTypeVisee, qID, qCode, qExpe, qLong, qAz, qP, qLG, qLD, qHZ, qHN, qIDTerrain, qCommentaire): 
        VV = TStation()
        VV.SetValeurs(qID, qSecteur, qTypeVisee, qCode, qExpe, qLong, qAz, qP, qLG, qLD, qHZ, qHN, qIDTerrain, qCommentaire)
        self.FListeStations.append(VV) 
    #---------------------------------
    def ClearBranche(self):
        self.FListeStations = []
        WU = self.AddStationByValeurs(0, 0, 0, 0, 0, 0.01, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, "","Added")
    #---------------------------------
    # ajout d une station
    def AddStation(self, S):
        self.FListeStations.append(S) 
    
    #---------------------------------
    # attraper une station
    def GetStation(self, Idx):
        return self.FListeStations[Idx]
    #---------------------------------
    def PutStation(self, Idx, C):
        self.FListeStations[Idx] = C
    #---------------------------------
    def GetNbStations(self):
        return len(self.FListeStations)  
    
# ------------------------------------------------------------
# structure pour les entitÃ©s (rÃ©sultats du calcul)
class TEntiteEtendue:
    def __init__(self):
        #  serie et point
        self.Entite_Serie      = 0   #  SÃ©rie
        self.Entite_Station    = 0   #  Station
        #  secteurs, type de visÃ©e, rÃ©seaux, codes, expÃ©s
        self.Type_Entite       = 0;
        self.eSecteur          = 0
        self.eReseau           = 0
        self.eCode             = 0
        self.eExpe             = 0
        self.DateLeve          = 0.00
        #  drapeaux
        self.Drawn             = False
        #  valeurs initiales: Long, Az, P
        self.oLongueur              = 0.00
        self.oAzimut                = 0.00
        self.oPente                 = 0.00
        self.oLG                    = 0.00
        self.oLD                    = 0.00
        self.oHZ                    = 0.00
        self.oHN                    = 0.00
        #  valeurs calculÃ©es: centerline
        self.Une_Station_1_X   = 0.00
        self.Une_Station_1_Y   = 0.00
        self.Une_Station_1_Z   = 0.00

        self.Une_Station_2_X   = 0.00
        self.Une_Station_2_Y   = 0.00
        self.Une_Station_2_Z   = 0.00
        #  valeurs calculÃ©es: silhouette
        self.X1PD        = 0.00 #X point droit contour
        self.Y1PD        = 0.00 #Y point gauche contour
        self.X1PG        = 0.00 #X point droit contour
        self.Y1PG        = 0.00 #Y point gauche contour

        self.X2PD        = 0.00 #X point droit contour
        self.Y2PD        = 0.00 #Y point gauche contour
        self.X2PG        = 0.00 #X point droit contour
        self.Y2PG        = 0.00 #Y point gauche contour

        self.Z1PH        = 0.00 #Z point haut contour
        self.Z1PB        = 0.00 #Z point bas contour
        self.Z2PH        = 0.00 #Z point haut contour
        self.Z2PB        = 0.00 #Z point bas contour
        #  valeur calculÃ©e: Couleur en fonction de la profondeur
        #  stockÃ©e ici en raison du grand nombre de calculs pour le dÃ©gradÃ©
        self.ColourByDepth    = rgb(255, 255, 255)
        #  champs texte => en fin de ligne
        self.oIDLitteral      = ""
        self.oCommentaires    = ""
#-----------------------------------------------------------
class TTemporaryStation:
    def __init__(self):
        self.NumSerie  = 0
        self.NumPoint  = 0
        self.stSecteur = 0
        self.stCode    = 0
        self.stExpe    = 0
        self.Couleur      = rgb(0,0,0)
        self.TypeVisee  = 0
        self.Date         = date.today
        self.Longueur     = 0.00
        self.Azimut       = 0.00
        self.Pente        = 0.00
        self.LD           = 0.00
        self.LG           = 0.00
        self.HZ           = 0.00
        self.HN           = 0.00
        self.Commentaire  = ""
        self.IDTerrainStation  = ""
        self.X = 0.00
        self.Y = 0.00
        self.Z = 0.00
