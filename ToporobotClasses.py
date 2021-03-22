# -*-coding:utf-8 -*
import string

#from xml.dom import minidom # parseur xml
from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement


from math import *
from functions import *
from types_donnees import *
#-----------------------------------------------
# Gestion du fichier XTB
# 14/05/2014: OK
class TDocuTopo:
    # /!\ En Python, ne jamais oublier le 'self' dans la liste
    #     des paramÃ¨tres d une methode (premier element)
    # c'est l equivalent de TClasse.Create()
    def __init__(self, arg1, arg2):
        self.FArg1 = arg1
        self.FArg2 = arg2
        AfficherMessage(self.FArg1)
        AfficherMessage(self.FArg2)
    #---------------------------------    
    # vider les listes
    def ViderListes(self):
        # En Python, les tableaux sont en fait des listes.
        self.FListeEntrees = []
        self.FListeReseaux  = []
        self.FListeSecteurs = []
        self.FListeCodes = [] # equivalent de FListeCodes.Clear
        self.FListeExpes = []        
        self.FListeSeries  = []
        self.FListeAntennes = []
        # éléments 0
        MyReseau = TReseau()
        # après une instanciation 'à vide', affecter une valeur à tous les membres
        MyReseau.IdxReseau    = 0
        MyReseau.ColorReseau  = 0
        MyReseau.TypeReseau   = 0
        MyReseau.NomReseau    = "Reseau0"
        MyReseau.ObsReseau    = ""
        self.AddReseau(MyReseau)
        MySecteur = TSecteur(0, 255, 0, 0, "Secteur0")
        self.AddSecteur(MySecteur)
        
        
    # Coordonnees de references = coordonnees de l entree 0
    def SetCoordsDeReference(self, x, y, z):
        self.FReferencePoint0X = x
        self.FReferencePoint0Y = y
        self.FReferencePoint0Z = z
    #--- END PROC --------------------    
    def GetPoint0X(self):
        return self.FReferencePoint0X
    #--- END PROC --------------------
    def GetPoint0Y(self):
        return self.FReferencePoint0Y
    #--- END PROC --------------------
    def GetPoint0Z(self):
        return self.FReferencePoint0Z
    #--- END PROC --------------------
        
    
    #---------------------------------
    # ENTREES
    def AddEntree(self, E):
        self.FListeEntrees.append(E)
    #--- END PROC --------------------
        
    def GetEntree(self, Idx):
        return self.FListeEntrees[Idx]
    #--- END PROC --------------------
    def GetNbEntrees(self):
        return len(self.FListeEntrees)
    #--- END PROC --------------------
    def PutEntree(self, Idx, E):
        self.FListeEntrees[Idx] = E
    #--- END PROC --------------------
    #---------------------------------
    # RESEAUX
    #def MakeEmptyReseau(self):
    #    Result = TReseau()
    #    return Result
    
    def AddReseau(self, R):
        self.FListeReseaux.append(R)
    #--- END PROC --------------------
        
    def GetReseau(self, Idx):
        return self.FListeReseaux[Idx]
    #--- END PROC --------------------    
    def GetNbReseaux(self):
        return len(self.FListeReseaux)
    #--- END PROC --------------------  
    def PutReseau(self, Idx, R):
        self.FListeReseaux[Idx] = R
    #---------------------------------
    # SECTEURS
    #def MakeEmptySecteur(self):
    #    Result = TSecteur(0, 255,0,0, 'Secteur0')
    #    return Result
    
    def AddSecteur(self, C):
        self.FListeSecteurs.append(C) 
    #---------------------------------
    def GetSecteur(self, Idx):
        return self.FListeSecteurs[Idx]
    #---------------------------------
    def PutSecteur(self, Idx, C):
        self.FListeSecteurs[Idx] = C
    #---------------------------------
    def GetNbSecteurs(self):
       return len(self.FListeSecteurs)    
    #---------------------------------
    # CODES
    def AddCode(self, C):
        self.FListeCodes.append(C) 
    #---------------------------------
    def GetCode(self, Idx):
        return self.FListeCodes[Idx]
    #---------------------------------
    def PutCode(self, Idx, C):
        self.FListeCodes[Idx] = C
    #---------------------------------
    def GetNbCodes(self):
       return len(self.FListeCodes)
    #---------------------------------
    def GetCodeByIndex(self, Idx):
        # try:
            # QN = self.FListeCodes.index(Idx)
        # except:
            # QN = 0
        # return self.FListeCodes[QN]
        Nb = self.GetNbCodes()
        for i in range(0, Nb):
            EWE = self.FListeCodes[i]
            if (EWE.IDCode == Idx):
                return EWE
        return self.FListeCodes[0]
    #--- END PROC --------------------
    # EXPES
    def AddExpe(self, C):
        self.FListeExpes.append(C)
    #---------------------------------
    def GetExpe(self, Idx):
        return self.FListeExpes[Idx]
    #---------------------------------
    def PutExpe(self, Idx, C):
        self.FListeExpes[Idx] = C
    #---------------------------------
    def GetNbExpes(self):
       return len(self.FListeExpes)
    #---------------------------------
    def GetExpeByIndex(self, Idx):
        # La mÃ©thode utilisant <tableau>.index(Idx) ne semble pas fonctionner
        # try:
            # QN = self.FListeExpes.index(Idx)
        # except:
            # QN = 0
        # return self.FListeExpes[QN]
        Nb = self.GetNbExpes()
        for i in range(0, Nb):
            EWE = self.FListeExpes[i]
            if (EWE.IDExpe == Idx):
                return EWE
        return self.FListeExpes[0]
    #--- END PROC --------------------
    #---------------------------------
    # SERIES
    def AddSerie(self, C):
        self.FListeSeries.append(C) 
    #---------------------------------
    def GetSerie(self, Idx):
        return self.FListeSeries[Idx]
    #---------------------------------
    def PutSerie(self, Idx, C):
        self.FListeSeries[Idx] = C
    #---------------------------------
    def GetNbSeries(self):
       return len(self.FListeSeries)
    #---------------------------------
    # ANTENNES
    def AddAntenne(self, C):
        self.FListeAntennes.append(C) 
    #---------------------------------
    def GetAntenne(self, Idx):
        return self.FListeAntennes[Idx]
    #---------------------------------
    def PutAntenne(self, Idx, C):
        self.FListeAntennes[Idx] = C
    #---------------------------------
    def GetNbAntennes(self):
       return len(self.FListeAntennes)
    #*********************************
    # OPERATIONS
    def TraiterLigne(self, MyLine):
        R = Trim(MyLine)
        return R     
    
    # chargement d un fichier
    def ChargerFichierTab(self, FileName, CharEncoding):
        
        # end LireLigne    
        self.FFileName = FileName
        DoPrepareSerie = 0
        # equivalent de la fonction Format de Delphi
        # WU = Format('ChargerFichierTab: %s - %d  , [self.FFileName, 123]);
        # devient
        # WU =        'ChargerFichierTab: %s - %d  % (self.FFileName, 123)       
        AfficherMessage("ChargerFichierTab: %s - %d"  % (self.FFileName, 123))
        self.ViderListes()
        # premiers elements des listes
        MyCode  = TCode(0, 360.00, 360.00, 0.1, 1.0, 1.0, '')
        self.AddCode(MyCode)
        
        MySerie = TSerie()
        MyStation = TStation()
        MySerie.AddStation(MyStation)
        self.AddSerie(MySerie)
        # analyse du fichier
        #file = open(FileName, 'rU')
        #file = open(FileName, encoding='utf-8')
        file = open(FileName, 'r', -1, CharEncoding) # ou "cp1252" pour ansiutf-8
        try:
            NoLine = 0
            NbEntrees = 0
            for line in file:
                #try:
                    line = self.TraiterLigne(line)
                    #line = line + '\t'
                    NoLine = NoLine + 1
                    if (len(line) == 0):
                        continue
                    if (line[0] == '#'): # vire les commentaires
                        continue
                    #line = unicode(line, 'mac_roman') # Toporobot comes from Mac
                    Values = line.split('\t')
                    Prefix = int(Trim(Values[0]))
                    if (Prefix == -10):
                        #-10	1	0	0	255	Puits d entree
                        MySecteur = TSecteur(int(Trim(Values[1])), \
                                             int(Trim(Values[2])), \
                                             int(Trim(Values[3])), \
                                             int(Trim(Values[4])), \
                                             Trim(Values[5]) \
                                             )
                        self.AddSecteur(MySecteur)
                    if (Prefix == -8):
                        # -8	1	128	128	128	3	Topos de surface
                        MyReseau = TReseau()
                        MyReseau.IdxReseau    = int(Trim(Values[1]))
                        MyReseau.ColorReseau  = rgb(int(Trim(Values[1])), \
                                                    int(Trim(Values[2])), \
                                                    int(Trim(Values[3])))
                        MyReseau.TypeReseau   = int(Trim(Values[4]))
                        MyReseau.NomReseau    = Trim(Values[5])
                        MyReseau.ObsReseau    = Trim(Values[6])

                        self.AddReseau(MyReseau)

                    if (Prefix == -9):
                        #-9	1	0	0	300	12	1	5	ANT01	6.66	190.00	12.00	12.00
                        MyAntenne = TAntenne()
                        MyAntenne.ID       = int(Trim(Values[1]))
                        MyAntenne.Reseau   = int(Trim(Values[2]))
                        MyAntenne.Secteur  = int(Trim(Values[3]))
                        MyAntenne.SerDep   = int(Trim(Values[4]))
                        MyAntenne.PtDep    = int(Trim(Values[5]))
                        MyAntenne.Code     = int(Trim(Values[6]))
                        MyAntenne.Expe     = int(Trim(Values[7]))
                        MyAntenne.IDerrain = Trim(Values[8])
                        MyAntenne.Longueur = float(Trim(Values[9]))
                        MyAntenne.Azimut   = float(Trim(Values[10]))
                        MyAntenne.Pente    = float(Trim(Values[11]))
                        MyAntenne.Commentaire = '' # Trim(Values[11])
                        self.AddAntenne(MyAntenne)
                        
                    if (Prefix == -6):
                        AfficherMessage('Entree: %d: %s' % (Prefix, Values[1]))
                        # -6	1	Gouffre des Charentais
                        # -5	1	442197.93	3070536.01	1193.00	1	0	jmhsgdsmdg
                        MyEntree = TEntree()
                        MyEntree.eNumEntree = int(Trim(Values[1]))
                        MyEntree.eNomEntree = Trim(Values[2])
                        self.AddEntree(MyEntree)
                    elif (Prefix == -5):
                        AfficherMessage("Entree: %d"  % (Prefix))
                        MyEntree = self.GetEntree(NbEntrees)
                        MyEntree.eXEntree = float(Trim(Values[2]))
                        MyEntree.eYEntree = float(Trim(Values[3]))
                        MyEntree.eZEntree = float(Trim(Values[4]))
                        MyEntree.eRefSer  = int(Trim(Values[5]))
                        MyEntree.eRefSt   = int(Trim(Values[6]))
                        MyEntree.eObserv  = ''
                        AfficherMessage("%d: %d.%d - %s - %.2f %.2f %.2f" % (Prefix, MyEntree.eRefSer, MyEntree.eRefSt, MyEntree.eNomEntree, MyEntree.eXEntree, MyEntree.eYEntree, MyEntree.eZEntree))
                        self.PutEntree(NbEntrees, MyEntree)
                        NbEntrees = NbEntrees + 1
                    elif (Prefix == -4): # inutilise
                        pass             # instruction pass = instruction vide
                    elif (Prefix == -3):
                        pass
                    elif (Prefix == -2):
                        #AfficherMessage("Expe: %d"  % (Prefix))
                        MyExpe = TExpe()
                        MyExpe.IDExpe    = int(Trim(Values[1]))
                        MyExpe.JourExpe  = int(Trim(Values[2]))
                        MyExpe.MoisExpe  = int(Trim(Values[3]))
                        MyExpe.AnneeExpe = int(Trim(Values[4]))
                        MyExpe.Speleometre = Trim(Values[5])
                        MyExpe.Speleographe= Trim(Values[6])
                        MyExpe.IdxCouleur  = int(Trim(Values[7]))
                        self.AddExpe(MyExpe)
                                       
                    elif (Prefix == -1):
                        #AfficherMessage("Code: %d"  % (Prefix))
                        MyCode = TCode(int(Trim(Values[1])), \
                                       float(Trim(Values[2])), \
                                       float(Trim(Values[3])), \
                                       float(Trim(Values[4])), \
                                       float(Trim(Values[5])), \
                                       float(Trim(Values[6])),  \
                                       ''
                                       )
                        self.AddCode(MyCode)
                    elif (Prefix > 0):
                        NumeroSerie = abs(Prefix)
                        Prefix1 = int(Trim(Values[1]))
                        if (Prefix1 == -1):
                            if (Prefix > 1): # un premier tour 
                                self.AddSerie(MySerie)
                            
                            # 1	-1	1	0	1	10	10	1	3	GALERIE PRINCIPALE		0	1.02
                            MySerie = TSerie()
                            MySerie.IdxSerie  = NumeroSerie
                            MySerie.SerDep   = int(Trim(Values[2]))
                            MySerie.PtDep    = int(Trim(Values[3]))
                            MySerie.SerArr   = int(Trim(Values[4]))
                            MySerie.PtArr    = int(Trim(Values[5]))
                            MySerie.NbSts    = int(Trim(Values[6]))
                            MySerie.Chance   = int(Trim(Values[7]))
                            MySerie.Obstacle = int(Trim(Values[8]))
                            MySerie.NomSerie = Trim(Values[9])
                           
                        if (Prefix1 >= 0):
                            # 1	1	1	1	10.00	89.00	-5.00	2.00	1.00	2.00	1.00			0
                            MyStation = TStation()
                            MyStation.IDStation = int(Trim(Values[1]))
                            MyStation.Code      = int(Trim(Values[2]))
                            MyStation.Expe      = int(Trim(Values[3]))
                            MyStation.Longueur  = float(Trim(Values[4]))
                            MyStation.Azimut    = float(Trim(Values[5]))
                            MyStation.Pente     = float(Trim(Values[6]))
                            MyStation.LG        = float(Trim(Values[7]))
                            MyStation.LD        = float(Trim(Values[8]))
                            MyStation.HZ        = float(Trim(Values[9]))
                            MyStation.HN        = float(Trim(Values[10]))
                            MyStation.Commentaire = Trim(Values[11])
                            MyStation.IDTerrain   = Trim(Values[12])
                            MyStation.TypeVisee   = int(Trim(Values[13]))
                            MyStation.Secteur     = int(Trim(Values[14]))
                            
                            MySerie.AddStation(MyStation)
                    else:
                        pass
                        
                #except UnicodeDecodeError:
                #    pass
                
                #except:
                #    AfficherMessage('Error in line %d'  % (NoLine))
            # definir le point 0
            QEntree = self.GetEntree(0) 
            self.SetCoordsDeReference(QEntree.eXEntree, QEntree.eYEntree, QEntree.eZEntree)
            # Indispensable: Ajouter la derniÃ¨re serie
            self.AddSerie(MySerie)
        finally:
            file.close()
    #--- END PROC --------------------
    #---------------------------------
    # Lister les entrees
    def ListerLesEntrees(self):
        EWE = self.GetNbEntrees()
        if (EWE > 0):
            AfficherMessage('ListerLesEntrees: %d entrees' % (EWE))
            for i in range(EWE): # range(EWE) renvoie n - 1 
                MyEntree = self.GetEntree(i)
                # MyCode.UAzimut = 666 + i # les membres d une "structure" sont modifiables
                # AfficherMessage('Entree: %d - %s - (%d.%d) - %.2f, %.2f, %.2f - %s' % (\
                #      i, MyEntree.eNumEntree, MyEntree.eNomEntree, \
                #      MyEntree.eRefSer, MyEntree.eRefSt, \
                #      MyEntree.eXEntree, MyEntree.eYEntree, MyEntree.eZEntree, \
                #      MyEntree.eObserv 
                #      ))
                AfficherMessage('Entree: %d:  %d - %s - (%d.%d)- %.2f, %.2f, %.2f - %s' % (\
                      i, MyEntree.eNumEntree, MyEntree.eNomEntree, \
                      MyEntree.eRefSer, MyEntree.eRefSt, \
                      MyEntree.eXEntree, MyEntree.eYEntree, MyEntree.eZEntree, \
                      MyEntree.eObserv ))
    #--- END PROC --------------------            
    # Lister les reseaux
    def ListerLesReseaux(self):
        EWE = self.GetNbReseaux()
        if (EWE > 0):
            AfficherMessage('ListerLesReseaux: %d reseaux' % (EWE))
            for i in range(EWE): # range(EWE) renvoie n - 1 
                MyReseau = self.GetReseau(i)
                # MyCode.UAzimut = 666 + i # les membres d une "structure" sont modifiables
                AfficherMessage('Reseau: %d - %d - Couleur: %d - %d - %s - %s' % (\
                      i, MyReseau.IdxReseau, \
                      MyReseau.ColorReseau , \
                      MyReseau.TypeReseau, \
                      MyReseau.NomReseau, \
                      MyReseau.ObsReseau 
                      ))
    #--- END PROC --------------------
    # Lister les secteurs
    def ListerLesSecteurs(self):
        EWE = self.GetNbSecteurs()
        if (EWE > 0):
            AfficherMessage('ListerLesSecteurs: %d secteurs' % (EWE))
            for i in range(EWE): # range(EWE) renvoie n - 1 
                MySecteur = self.GetSecteur(i)
                # MyCode.UAzimut = 666 + i # les membres d une "structure" sont modifiables
                AfficherMessage('Secteur: %d - RGB(%d, %d, %d) - %s' % (\
                      MySecteur.IDSecteur, \
                      MySecteur.ColR, \
                      MySecteur.ColG, \
                      MySecteur.ColB, \
                      MySecteur.NomSecteur \
                      ))
    #--- END PROC --------------------
    #---------------------------------
    # Lister les codes
    def ListerLesCodes(self):
        EWE = self.GetNbCodes()
        AfficherMessage('ListerLesCodes: %d codes' % (EWE))
        for i in range(EWE): # range(EWE) renvoie n - 1 
            MyCode = self.GetCode(i)
            # MyCode.UAzimut = 666 + i # les membres d une "structure" sont modifiables
            AfficherMessage('Code: %d - %.2f %.2f - %.2f %.2f %.2f - %s' % (\
                  MyCode.IDCode, \
                  MyCode.UAzimut, \
                  MyCode.UPente, \
                  MyCode.PrecLong, \
                  MyCode.PrecAzimut,
                  MyCode.PrecPente, \
                  MyCode.Commentaire
                  ))
    #--- END PROC --------------------
    #---------------------------------
    # Lister les expes
    def ListerLesExpes(self):
        EWE = self.GetNbExpes()
        AfficherMessage("ListerLesExpes: %d expes" % (EWE))
        for i in range(EWE): # range(EWE) renvoie n - 1 
            MyExpe = self.GetExpe(i)
            # MyCode.UAzimut = 666 + i # les membres d une "structure" sont modifiables
            AfficherMessage("Expe: %d - %.2d/%.2d/%.4d - %s; %s - %d"  % (\
                  MyExpe.IDExpe, \
                  MyExpe.JourExpe, \
                  MyExpe.MoisExpe, \
                  MyExpe.AnneeExpe, \
                  MyExpe.Speleometre, \
                  MyExpe.Speleographe, \
                  MyExpe.IdxCouleur \
                 ))
    #--- END PROC --------------------
    #---------------------------------
    # Lister les series
    def ListerLesSeries(self):
        EWE = self.GetNbSeries()
        AfficherMessage('ListerLesSeries: %d series' % (EWE))
        for i in range(EWE): # range(EWE) renvoie n - 1 
            MySerie = self.GetSerie(i)
            # MyCode.UAzimut = 666 + i # les membres d une "structure" sont modifiables
            AfficherMessage("Serie: %d - De %d.%d a %d.%d - %d sts - C = %d, O = %d - %s" % (\
                  MySerie.IdxSerie, \
                  MySerie.SerDep,  MySerie.PtDep, \
                  MySerie.SerArr, MySerie.PtArr, \
                  MySerie.NbSts, \
                  MySerie.Chance, MySerie.Obstacle, \
                  MySerie.Commentaires
                 ))
            # lister les stations
            WU = MySerie.GetNbStations()
            for St in range(WU):
                MyStation = MySerie.GetStation(St)
                AfficherMessage(" -- %d: %d - %d: %.2f %.2f %.2f" % ( \
                      MyStation.IDStation, \
                      MyStation.Code, MyStation.Expe, \
                      MyStation.Longueur, MyStation.Azimut, MyStation.Pente \
                      ))
    #--- END PROC --------------------
    # Lister les antennes
    def ListerLesAntennes(self):
        EWE = self.GetNbAntennes()
        if (EWE > 0):
            AfficherMessage("ListerLesAntennes: %d antennes" % (EWE))
            for i in range(EWE): # range(EWE) renvoie n - 1 
                MyAntenne = self.GetAntenne(i)
                # MyCode.UAzimut = 666 + i # les membres d une "structure" sont modifiables
                AfficherMessage('Antenne: %d - (%d-%d) - Station: %d.%d - %d, %d - %s - %.2f, %.2f, %.2f - %s' % (\
                        MyAntenne.ID, \
                        MyAntenne.Reseau, MyAntenne.Secteur, \
                        MyAntenne.SerDep , \
                        MyAntenne.PtDep  , \
                        MyAntenne.Code   , \
                        MyAntenne.Expe   , \
                        MyAntenne.IDerrain , \
                        MyAntenne.Longueur , \
                        MyAntenne.Azimut   , \
                        MyAntenne.Pente    , \
                        MyAntenne.Commentaire 
                     ))
        else:
            AfficherMessage("Pas de visees en antenne")
    #--- END PROC --------------------
#--------------------------------------------
# charger un fichier GTX
    def ChargerFichierGTX(self, FichierGTX):
        AfficherMessage("ChargerFichierGTX: %s " % (FichierGTX))
        self.ViderListes()
        # premiers elements des listes
        MyCode  = TCode(0, 360.00, 360.00, 0.1, 1.0, 1.0, '')
        self.AddCode(MyCode)
        MyExpe  = TExpe()
        self.AddExpe(MyExpe)
        MySerie = TSerie()
        MyStation = TStation()
        MySerie.AddStation(MyStation)
        self.AddSerie(MySerie)
        #MyDoc = minidom.parse(FichierGTX)
        #ByRoot = MyDoc.documentElement
        
        MyDoc = ElementTree.parse(FichierGTX)
        ByRoot = MyDoc.getroot()
        print(MyDoc)
        
        ListeEntrances = MyDoc.find('Entrances')
        if (ListeEntrances): 
            n = len(ListeEntrances)
            print("--> J'entre dans %s - %d éléments" %(ListeEntrances.tag, n))
            # <Entrance X="403460.00" Y="3089600.00" Z="540.00" Name="GROTTE DUTROUX" Numero="0" Comments="entr�e principale" RefPoint="0" RefSerie="1" IdTerrain=""/>
            for NodeEntrance in MyDoc.findall( 'Entrances/Entrance'):
                MyEntrance = TEntree()
                MyEntrance.eNomEntree = NodeEntrance.get('Name')
                MyEntrance.eRefSer    = int(NodeEntrance.get('RefSerie'))
                MyEntrance.eRefSt     = int(NodeEntrance.get('RefPoint'))
                MyEntrance.eXEntree   = float(NodeEntrance.get('X'))
                MyEntrance.eYEntree   = float(NodeEntrance.get('Y'))
                MyEntrance.eZEntree   = float(NodeEntrance.get('Z'))
                MyEntrance.eObserv    = NodeEntrance.get('Comments')
                print('[%d.%d] %s - %.2f, %.2f, %.2f - %s' %(MyEntrance.eRefSer, MyEntrance.eRefSt, MyEntrance.eNomEntree, MyEntrance.eXEntree, MyEntrance.eYEntree, MyEntrance.eZEntree, MyEntrance.eObserv))
                self.AddEntree(MyEntrance)
            
        # <Network Name="Carrière souterraine" Type="1" ColorB="255" ColorG="0" ColorR="255" Numero="1" Comments=""/>
        ListeReseaux = MyDoc.find('Networks')
        if (ListeReseaux): 
            n = len(ListeReseaux)
            print("--> J'entre dans %s - %d éléments" % (ListeReseaux.tag, n))
            for NodeReseau in MyDoc.findall( 'Networks/Network'):
                MyReseau = TReseau()
                MyReseau.IdxReseau   = int(NodeReseau.get('Numero'))
                MyReseau.NomReseau   = NodeReseau.get('Name')
                MyReseau.TypeReseau  = int(NodeReseau.get('Type'))
                MyReseau.ColorReseau = rgb(int(NodeReseau.get('ColorR')), int(NodeReseau.get('ColorG')), int(NodeReseau.get('ColorB')))
                MyReseau.ObsReseau   = NodeReseau.get('Comments')
                print('%d: %s - Type: %d - Color: %d - %s' %(MyReseau.IdxReseau, MyReseau.NomReseau, MyReseau.TypeReseau, MyReseau.ColorReseau, MyReseau.ObsReseau))
                self.AddReseau(MyReseau)
                
        # <Secteur Name="Secteur Carrière" ColorB="64" ColorG="128" ColorR="255" Numero="1"/>
        ListeSecteurs = MyDoc.find('Secteurs')
        if (ListeSecteurs): 
            n = len(ListeSecteurs)
            print("--> J'entre dans %s - %d éléments" % (ListeSecteurs.tag, n))
            for NodeSecteur in MyDoc.findall( 'Secteurs/Secteur'):
                MySecteur = TSecteur(int(NodeSecteur.get('Numero')), \
                                     int(NodeSecteur.get('ColorR')), \
                                     int(NodeSecteur.get('ColorG')), \
                                     int(NodeSecteur.get('ColorB')), \
                                     NodeSecteur.get('Name')
                                    ) 
                print('%d: %s - Color: rgb(%d, %d, %d)' %(MySecteur.IDSecteur, MySecteur.NomSecteur, MySecteur.ColR, MySecteur.ColG, MySecteur.ColB))
                self.AddSecteur(MySecteur)
         
        # <Code PsiL="0.100" PsiP="1.000" Type="0" PsiAz="1.000" Numero="1" Comments="" FactLong="0.000" ClinoUnit="360.00" AngleLimite="0.00" CompassUnit="360.00" FuncCorrAzCo="0.000000" FuncCorrIncCo="0.000000" FuncCorrAzErrMax="0.000000" FuncCorrIncErrMax="0.000000" FuncCorrAzPosErrMax="0.000000" FuncCorrIncPosErrMax="0.000000"/>
        ListeCodes = MyDoc.find('Codes')
        if (ListeCodes): 
            n = len(ListeCodes)
            print("--> J'entre dans %s - %d éléments" % (ListeCodes.tag, n))
            for NodeCode in MyDoc.findall( 'Codes/Code'):
                MyCode = TCode(int(NodeCode.get('Numero')), \
                               float(NodeCode.get('CompassUnit')), \
                               float(NodeCode.get('ClinoUnit')), \
                               float(NodeCode.get('PsiL')), \
                               float(NodeCode.get('PsiAz')), \
                               float(NodeCode.get('PsiP')), \
                               NodeCode.get('Comments')) 
                print('--- %d; %.3f, %.3f; %.3f, %.3f, %.3f; "%s"' % ( \
                               MyCode.IDCode, \
                               MyCode.UAzimut, MyCode.UPente, \
                               MyCode.PrecLong, MyCode.PrecAzimut, MyCode.PrecPente, \
                               MyCode.Commentaire))
                self.AddCode(MyCode)
                
        # <Trip Date="0088-05-28" Color="52" Numero="1" ="JPC est un gros PD" Surveyor1="CASSOU JP" Surveyor2="PIPISTRELLE" Declination="0.0000" Inclination="0.0000" ModeDeclination="0"/>
        ListeExpes = MyDoc.find('Seances')
        if (ListeExpes): 
            n = len(ListeExpes)
            print("--> J'entre dans %s - %d éléments" % (ListeExpes.tag, n))
            for NodeExpe in MyDoc.findall( 'Seances/Trip'): 
                MyExpe = TExpe()              
                MyExpe.IDExpe          = int(NodeExpe.get('Numero'))
                MyExpe.JourExpe        = 1    #int(NodeExpe.get(''))
                MyExpe.MoisExpe        = 1    #int(NodeExpe.get(''))
                MyExpe.AnneeExpe       = 2016 #int(NodeExpe.get(''))
                MyExpe.IdxCouleur      = int(NodeExpe.get('Color'))
                MyExpe.Speleometre     = NodeExpe.get('Surveyor1')
                MyExpe.Speleographe    = NodeExpe.get('Surveyor2')
                MyExpe.Declinaison     = float(NodeExpe.get('Declination'))
                MyExpe.Inclinaison     = float(NodeExpe.get('Inclination')) 
                MyExpe.Commentaire     = NodeExpe.get('Comments')
                print('--- %d; %.2d/%.2d/%.4d; %d; %s, %s; %.3f, %.3f; "%s"' % ( \
                               MyExpe.IDExpe, \
                               MyExpe.JourExpe, MyExpe.MoisExpe, MyExpe.AnneeExpe, \
                               MyExpe.IdxCouleur, \
                               MyExpe.Speleometre, MyExpe.Speleographe, \
                               MyExpe.Declinaison, MyExpe.Inclinaison, \
                               MyExpe.Commentaire))
                self.AddExpe(MyExpe)
        # séries
        ListeSeries = MyDoc.find('Series')
        if (ListeSeries): 
            n = len(ListeSeries)
            print("--> J'entre dans %s - %d éléments" % (ListeSeries.tag, n))
            for NodeSerie in MyDoc.findall( 'Series/Serie'):
                # <Serie Name="GALERIE PRINCIPALE" Color="#000000" PtArr="11" PtDep="0" Chance="1" Numero="1" SerArr="1" SerDep="1" Network="1" Raideur="1.0200" Entrance="0" Obstacle="3" Commments="">
  
                MySerie = TSerie()
                
                MySerie.IdxSerie    = int(NodeSerie.get('Numero'))
                MySerie.NomSerie = NodeSerie.get('Name')
                MySerie.IdxReseau   = int(NodeSerie.get('Network'))
                MySerie.SerDep      = int(NodeSerie.get('SerDep'))
                MySerie.PtDep       = int(NodeSerie.get('PtDep'))
                MySerie.SerArr      = int(NodeSerie.get('SerArr'))
                MySerie.PtArr       = int(NodeSerie.get('PtArr'))
                
                MySerie.Chance      = int(NodeSerie.get('Chance'))
                MySerie.Obstacle    = int(NodeSerie.get('Obstacle'))
                MySerie.Commentaires = NodeSerie.get('Commments')
                MySerie.IdxEntrance  = int(NodeSerie.get('Entrance'))
                LesStations = NodeSerie.find('Stations')
                MySerie.NbSts        = len(LesStations)
                self.AddSerie(MySerie)
                for MyShot in NodeSerie.findall('Stations/Shot'):
                    MyStation = TStation()
                    MyStation.Secteur     = int(MyShot.get('Secteur'))
                    MyStation.TypeVisee   = int(MyShot.get('TypeShot'))
                    MyStation.Code        = int(MyShot.get('Code'))
                    MyStation.Expe        = int(MyShot.get('Trip'))
                    
                    MyStation.Longueur    = float(MyShot.get('Length')) 
                    MyStation.Azimut      = float(MyShot.get('Az'))
                    MyStation.Pente       = float(MyShot.get('Incl')) 
                    MyStation.LG          = float(MyShot.get('Left')) 
                    MyStation.LD          = float(MyShot.get('Right'))  
                    MyStation.HZ          = float(MyShot.get('Up')) 
                    MyStation.HN          = float(MyShot.get('Down'))
                    MyStation.IDTerrain   = MyShot.get('Label')
                    MyStation.Commentaire = MyShot.get('Comments')
                    
                    print('--- %d; %d; %d, %d; %.3f, %.3f, %.3f, %.3f, %.3f, %.3f, %.3f,  "%s",  "%s"' % ( \
                          MyStation.Secteur, MyStation.TypeVisee, MyStation.Code, MyStation.Expe, \
                          MyStation.Longueur, MyStation.Azimut, MyStation.Pente, \
                          MyStation.LG, MyStation.LD, MyStation.HZ, MyStation.HN, \
                          MyStation.IDTerrain, MyStation.Commentaire))
                    MySerie.AddStation(MyStation)
                
                print('%d: [%d.%d - %d.%d] (%d)  %s' %(MySerie.IdxSerie, MySerie.SerDep, MySerie.PtDep, MySerie.SerArr, MySerie.PtArr, MySerie.NbSts, MySerie.NomSerie )) 
        
        # antennes
        ListeAntennes = MyDoc.find('AntennaShots')
        if (ListeAntennes): 
            n = len(ListeAntennes)
            # <AntennaShot Az="190.00" Code="1" Incl="12.00" Trip="5" Label="ANT01" PtDep="12" Length="6.660" Numero="1" SerDep="300" Network="0" Secteur="0" Comments="12.00"/>
            print("--> J'entre dans %s - %d éléments" % (ListeAntennes.tag, n))
            for NodeAntenne in MyDoc.findall( 'AntennaShots/AntennaShot'): 
                MyAntenne = TAntenne() 
                MyAntenne.ID          = int(NodeAntenne.get('Numero'))
                MyAntenne.Reseau      = int(NodeAntenne.get('Network'))
                MyAntenne.Secteur     = int(NodeAntenne.get('Secteur'))
                MyAntenne.SerDep      = int(NodeAntenne.get('SerDep'))
                MyAntenne.PtDep       = int(NodeAntenne.get('PtDep'))
                MyAntenne.Code        = int(NodeAntenne.get('Code'))
                MyAntenne.Expe        = int(NodeAntenne.get('Trip'))
               
                MyAntenne.Longueur    = float(NodeAntenne.get('Length'))
                MyAntenne.Azimut      = float(NodeAntenne.get('Az'))
                MyAntenne.Pente       = float(NodeAntenne.get('Incl'))
                MyAntenne.IDTerrain   = NodeAntenne.get('Label')
                MyAntenne.Commentaire = NodeAntenne.get('Comments')
     
                print('--- %d; %d, %d; %d.%d; %d, %d; %.3f, %.3f, %.3f; "%s"; "%s"' % ( \
                           MyAntenne.ID, MyAntenne.Reseau, MyAntenne.Secteur, \
                           MyAntenne.SerDep, MyAntenne.PtDep, \
                           MyAntenne.Code, MyAntenne.Expe, \
                           MyAntenne.Longueur, MyAntenne.Azimut, MyAntenne.Pente, \
                           MyAntenne.IDTerrain, MyAntenne.Commentaire))
                self.AddAntenne(MyAntenne)
        
        # definir le point 0
            MyEntrance = self.GetEntree(0) 
            self.SetCoordsDeReference(MyEntrance.eXEntree, MyEntrance.eYEntree, MyEntrance.eZEntree)
#============================================