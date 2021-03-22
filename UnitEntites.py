# -*-coding:utf-8 -*
import string

from math import *
from functions import *
from types_donnees import *
from UnitClassPalette import *
#--------------------------------
# Table des entités
class TTableDesEntites:
    def __init__(self):
        self.MyPalette = TPalette256()
        self.FListeEntites = []
        self.FListeEntrees = []
        self.FListeAntennes = []
        
    #------------------------------------
    def AddEntite(self, MyEntite):
        self.FListeEntites.append(MyEntite)
    #------------------------------------
    def GetNbEntites(self):
        return len(self.FListeEntites)
    #------------------------------------
    def GetEntite(self, Idx):
        return self.FListeEntites[Idx]
    #------------------------------------
    def GetEntiteFromSerSt(self, QSerieDepart, QPtDepart):
        for i in range(0, self.GetNbEntites()):
            E = self.GetEntite(i)
            if ((E.Entite_Serie == QSerieDepart) and (E.Entite_Station == QPtDepart)):
                return E
        return E
                
    #------------------------------------
    def AddEntrance(self, MyEntrance):
        self.FListeEntrees.append(MyEntrance)
    #------------------------------------
    def GetNbEntrances(self):
        return len(self.FListeEntrees)
    #------------------------------------
    def GetEntrance(self, Idx):
        return self.FListeEntrees[Idx]
    #------------------------------------ 
    def AddAntenne(self, MyAntenne):
        self.FListeAntennes.append(MyAntenne)
    #------------------------------------
    def GetNbAntennes(self):
        return len(self.FListeAntennes)
    #------------------------------------
    def GetAntenne(self, Idx):
        return self.FListeAntennes[Idx]   
    #------------------------------------        
    def SetColorVisee(self, Idx):
        return self.MyPalette.GetCouleurByIndex(Idx)
    #------------------------------------
    def SetMinMax(self, Marge):
        self.FCoinMini = TPoint3Df( 1E18,  1E18,  1E18)
        self.FCoinMaxi = TPoint3Df(-1E18, -1E18, -1E18)
        self.FMarge = Marge
        # entités
        for i in range(1, self.GetNbEntites()):
            E = self.GetEntite(i)
            # AfficherMessage("-- %.2f, %.2f, %.2f" % (E.Une_Station_2_X, E.Une_Station_2_Y, E.Une_Station_2_Z))
            if (E.Une_Station_2_X < self.FCoinMini.X): self.FCoinMini.X = E.Une_Station_2_X
            if (E.Une_Station_2_Y < self.FCoinMini.Y): self.FCoinMini.Y = E.Une_Station_2_Y
            if (E.Une_Station_2_Z < self.FCoinMini.Z): self.FCoinMini.Z = E.Une_Station_2_Z
            if (E.Une_Station_2_X > self.FCoinMaxi.X): self.FCoinMaxi.X = E.Une_Station_2_X
            if (E.Une_Station_2_Y > self.FCoinMaxi.Y): self.FCoinMaxi.Y = E.Une_Station_2_Y
            if (E.Une_Station_2_Z > self.FCoinMaxi.Z): self.FCoinMaxi.Z = E.Une_Station_2_Z
        AfficherMessage("SetMinMax: %.2f, %.2f, %.2f -> %.2f, %.2f, %.2f" % (self.FCoinMini.X, self.FCoinMini.Y, self.FCoinMini.Z, self.FCoinMaxi.X, self.FCoinMaxi.Y, self.FCoinMaxi.Z))
        # entrées
        for i in range(0, self.GetNbEntrances()):
            Entr = self.GetEntrance(i)
            if (Entr.eXEntree < self.FCoinMini.X): self.FCoinMini.X = Entr.eXEntree
            if (Entr.eYEntree < self.FCoinMini.Y): self.FCoinMini.Y = Entr.eYEntree
            if (Entr.eZEntree < self.FCoinMini.Z): self.FCoinMini.Z = Entr.eZEntree 

            if (Entr.eXEntree > self.FCoinMaxi.X): self.FCoinMaxi.X = Entr.eXEntree
            if (Entr.eYEntree > self.FCoinMaxi.Y): self.FCoinMaxi.Y = Entr.eYEntree
            if (Entr.eZEntree > self.FCoinMaxi.Z): self.FCoinMaxi.Z = Entr.eZEntree 
            
    #------------------------------------
    def GetCoinBasGauche(self):
        return self.FCoinMini
    #------------------------------------
    def GetCoinHautDroit(self):
        return self.FCoinMaxi
    #------------------------------------
    def ListerLesEntites(self):
        AfficherMessage("Liste des %d entites" % (self.GetNbEntites()))
        for i in range(1, self.GetNbEntites()):
            E = self.GetEntite(i)
            AfficherMessage("%d.%d -  %.2f, %.2f, %.2f" % (E.Entite_Serie, E.Entite_Station, E.Une_Station_2_X, E.Une_Station_2_Y, E.Une_Station_2_Z))

    #------------------------------------
    #------------------------------------
    #------------------------------------
    #------------------------------------
    #------------------------------------
    #------------------------------------
    #------------------------------------
    #------------------------------------
    #------------------------------------
