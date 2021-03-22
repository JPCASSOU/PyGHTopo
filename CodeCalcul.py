# -*-coding:utf-8 -*

import string
from math import *
from functions import *
from types_donnees import *
from ToporobotClasses import *
from UnitEntites import *

# 11/05/2014: Calcul matriciel OK
# 13/05/2014: RÃ©partition parallÃ¨le proportionnelle OK
# 14/05/2014: Centerlines: TestÃ© OK avec Charentais , Roy, Saint Marcel et Toporabot
# 16/05/2014: Parois OK


class TCodeCalcul:
    # /!\ En Python, ne jamais oublier le 'self' dans la liste
    #     des paramÃ¨tres d une methode (premier element)
    # c'est l equivalent de TClasse.Create()
    def __init__(self, arg1, arg2):
        self.FArg1 = arg1
        self.FArg2 = arg2
        AfficherMessage(self.FArg1)
        AfficherMessage(self.FArg2)
    #*********************************************************
    def ViderListes(self):
        self.FListeJonctions = []
        self.FListeBranches  = []
        self.FListeNoeuds    = []
    #*********************************************************
    def SetDocTopo(self, QDocTopo, QBDDEntites):
        self.FDocuTopo = QDocTopo
        self.MyTableEntites = QBDDEntites
        self.ViderListes()
        AfficherMessage(self.FDocuTopo.GetNbExpes())
    #*********************************************************
    def AddJonction(self, J):
        self.FListeJonctions.append(J)

    def GetJonction(self, Idx):
        return self.FListeJonctions[Idx]

    def PutJonction(self, Idx, MyJunction):
        self.FListeJonctions[Idx] = MyJunction

    def GetNbJonctions(self):
        return len(self.FListeJonctions)
    #*********************************************************
    def GetNbBranches(self):
        return len(self.FListeBranches)
    
    def GetBranche(self, Idx):
        return self.FListeBranches[Idx]

    def AddBranche(self, Branche):
        Branche = self.CalculerBranche(Branche)
        self.FListeBranches.append(Branche)

    def RemoveBranche(self, Idx):
        self.FListeBranches.pop(Idx)

    def PutBranche(self, Idx, Branche):
        self.FListeBranches[Idx] = Branche
    #**********************************************************
    def CalculerBranche(self, Branche):
        Nb = Branche.GetNbStations()
        Branche.DeltaX       = 0.00
        Branche.DeltaY       = 0.00
        Branche.DeltaZ       = 0.00  
        Branche.LongDev      = 0.00
        for i in range(0, Nb):
            QVisee = self.CalculerVisee(Branche.GetStation(i))
            Branche.DeltaX  += QVisee.QDeltaX
            Branche.DeltaY  += QVisee.QDeltaY
            Branche.DeltaZ  += QVisee.QDeltaZ
            Branche.LongDev += QVisee.QLongDev
            Branche.PutStation(i, QVisee)
        return Branche
    
    
    #*********************************************************
    # function TCodeDeCalcul.RecenserJonctions: integer;
    def RecenserJonctions(self):
        def AddSansDoublon(X):
            try:
                toto = FListeProvJunct.index(X)
            except:
                pass
               
        FListeProvJunct = []
        # Entree
        WU = self.FDocuTopo.GetNbEntrees()
        for i in range (0, WU):
            MyEntree = self.FDocuTopo.GetEntree(i)
            NbPtsTopo = "%d.%d" % (MyEntree.eRefSer, MyEntree.eRefSt)
            FListeProvJunct.append(NbPtsTopo)
        # Series
        WU = self.FDocuTopo.GetNbSeries()
        AfficherMessage("Recensement jonctions: %d series" % (WU))
        for i in range(0, WU):
            MySerie = self.FDocuTopo.GetSerie(i)
            NbPtsTopo = "%d.%d" % (MySerie.SerDep, MySerie.PtDep)
            QAT = "%d.%d" % (MySerie.SerArr, MySerie.PtArr)
            #if (FListeProvJunct.index(NbPtsTopo) >= 0):
            FListeProvJunct.append(NbPtsTopo)
            FListeProvJunct.append(QAT)
        FListeProvJunct.sort()
        self.FLB = list(strip_duplicates(FListeProvJunct))
        self.FLB.sort()
        # creation de la liste des jonctions
        WU = len(self.FLB)
        for i in range(0, WU):
            Jonction = TJonction()
            Jonction.NoNoeud     = i
            Jonction.IDJonction  = self.FLB[i] 
            self.AddJonction(Jonction)
##        #controle
##        WU = self.GetNbJonctions()
##        for i in range(0, WU):
##            Jonction = self.FListeJonctions[i]
##            AfficherMessage("Node:(%d/%d) = %d - %s" % (i, (WU-1), Jonction.NoNoeud, Jonction.IDJonction))
    #--- END PROC --------------------
    #*********************************************************
    def GetNoeud(self,  QIdxSerie, QIdxStation):
        # la methode de recherche par la fonction <Liste>.index(cle) est connue 
        # mais inutilisable pour les listes de composites
        Nb  = len(self.FListeJonctions)
        QAT = "%d.%d" % (QIdxSerie, QIdxStation)
        for i in range(0, Nb):
            JC = self.GetJonction(i)
            if (JC.IDJonction == QAT):
                return i
        return -1
    #*********************************************************
    def RecenserBranches(self):
        def InitBranche(QIdxSerie, QReseau, QNdDep, QNdArr, QRigidite, QDeltaX, QDeltaY, QDeltaZ):
            Result = TBranche()
            Result.NoSerie      = QIdxSerie
            Result.NoReseau     = QReseau
            Result.NoeudDepart  = QNdDep
            Result.NoeudArrivee = QNdArr
            Result.Rigidite     = QRigidite
            Result.DeltaX       = QDeltaX
            Result.DeltaY       = QDeltaY
            Result.DeltaZ       = QDeltaZ
            Result.LongDev      = 0.00
            # Result.AddStationByValeurs(0, 0, 0, 1, 1, 0.01, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, "","Added")
            return Result
        #--- END SUB PROC --------------------
            
        NbreSeries = self.FDocuTopo.GetNbSeries() 
        AfficherMessage("Recensement branches: %d series et %d jonctions" % (NbreSeries, self.GetNbJonctions()))
        # premiÃ¨re branche     S  R  D  A  K      X     Y     Z
        Branche0 = InitBranche(0, 0, 0, 0, 1.00,  0.01, 0.01, 0.01)
        self.AddBranche(Branche0)
        Branche0 = InitBranche(1, 0, 0, 1, 1.00,  0.01, 0.01, 0.01)
        self.AddBranche(Branche0)
        Br = 0
        # balayage des series
        for Ser in range(1, NbreSeries):
            if ((Ser % 50) == 0):
               AfficherMessage("Serie: %d / %d" % (Ser, NbreSeries - 1))
            Serie = self.FDocuTopo.GetSerie(Ser)
            Nd    = self.GetNoeud(Serie.SerDep, Serie.PtDep);
            # debut de serie = nouvelle branche
            # premiÃ¨re branche     S  R  B  D  A  K      X     Y     Z
            Branche0 = InitBranche(Serie.IdxSerie, Serie.IdxReseau, Nd, -1, 1.00, 0.01, 0.01, 0.01)
            NbreStations = Serie.GetNbStations()
            for Vis in range(1, NbreStations):
                Visee = Serie.GetStation(Vis)
                Nd    = self.GetNoeud(Serie.IdxSerie, Vis)
                Visee.NoVisee = Vis;
                Branche0.AddStation(Visee)
                if ((Nd > -1) and (Vis < (NbreStations - 1))):
                    # clÃ´turer la branche courante
                    Branche0.NoeudArrivee = Nd
                    self.AddBranche(Branche0)
                    #et creer la suivante
                    Br += 1
                    Branche0 = InitBranche(Serie.IdxSerie, Serie.IdxReseau, Nd, -1, 1.00, 0.01, 0.01, 0.01)  
                    Branche0.NoeudDepart = Nd;
                # fin de serie = fin de branche: cloturer la branche
                if (Vis == NbreStations - 1):
                    Nd = self.GetNoeud(Serie.SerArr, Serie.PtArr)
                    Branche0.NoeudArrivee = Nd;
                    self.AddBranche(Branche0)
                    Br += 1
        # entrees
        NbEntrees = self.FDocuTopo.GetNbEntrees()
        NoeudDeDepart = self.GetNoeud(1, 0)
        for i in range(1, NbEntrees):
            Entree = self.FDocuTopo.GetEntree(i)
            Nd = self.GetNoeud(Entree.eRefSer, Entree.eRefSt)
            Branche = InitBranche(Entree.eRefSer, 0, 0, Nd, 1.00, 0.01, 0.01, 0.01)
            QQX = self.FDocuTopo.GetPoint0X()
            QQY = self.FDocuTopo.GetPoint0Y()
            QQZ = self.FDocuTopo.GetPoint0Z()
            QQ = GetBearingInc(Entree.eXEntree - QQX, Entree.eYEntree - QQY, Entree.eZEntree - QQZ, 360.00, 360.00)
            Branche.AddStationByValeurs(0, tgENTRANCE, 0, 0, 0, QQ.oLongueur, QQ.oAzimut, QQ.oPente, 0.00, 0.00, 0.00, 0.00, "", "Entrance %d" % (i))
            self.AddBranche(Branche)
            Branche = self.GetBranche(i)
            #AfficherMessage("Entree %s: %.2f %.2f %.2f" % (Branche.NoSerie, Branche.DeltaX, Branche.DeltaY, Branche.DeltaZ))
        # nettoyer les branches
        i = 0
        #
        while (i < self.GetNbBranches()):
            Branche0 = self.GetBranche(i);
            # critère de suppression: Développement nul
            # ne pas supprimer la branche 0-1
            WU = (Branche0.NoeudArrivee > 1) and (abs(Branche0.LongDev) < 1e-3)
            if (WU):
                self.RemoveBranche(i)
                AfficherMessage("Branche %d supprimee" % (i))
            i = i+1

        # contrÃ´le
        NbBranches = self.GetNbBranches()
        
##        AfficherMessage("Liste des %d branches" % (NbBranches))
##        AfficherMessage("-----------------------")
##        for i in range(0, NbBranches):
##            Branche0 = self.GetBranche(i)
##            NbSts = Branche0.GetNbStations()
##            AfficherMessage("%d - Serie %d - %d->%d (%d stations) - Delta: %.2f, %.2f, %.2f - Ld = %.2f" % (i, Branche0.NoSerie, \
##                  Branche0.NoeudDepart, Branche0.NoeudArrivee, NbSts, \
##                  Branche0.DeltaX, Branche0.DeltaY, Branche0.DeltaZ, \
##                  Branche0.LongDev))
##            # for j in range (0, NbSts):
                # MyStation = Branche0.GetStation(j)
                # AfficherMessage("-- %d: %d - %d, %d - %.2f, %.2f, %.2f - %.1f, %.1f, %.1f, %.1f [%.2f, %.2f %.2f] %s - %s" % ( \
                      # j, MyStation.IDStation, \
                      # MyStation.Code, MyStation.Expe, \
                      # MyStation.Longueur, MyStation.Azimut, MyStation.Pente, \
                      # MyStation.LG, MyStation.LD, MyStation.HZ, MyStation.HN, \
                      # MyStation.QDeltaX, MyStation.QDeltaY, MyStation.QDeltaZ,
                      # MyStation.IDTerrain, MyStation.Commentaire))
    #--- END PROC --------------------
    #*********************************************************
    def CalculerVisee(self, MaVisee):
        LeCode = self.FDocuTopo.GetCodeByIndex(MaVisee.Code)
        LaExpe = self.FDocuTopo.GetExpeByIndex(MaVisee.Expe) 
        # AfficherMessage("(%d, %d) - Code: %d - %f - %f - Expe: %d" % (MaVisee.Code, MaVisee.Expe, LeCode.IDCode, LeCode.UAzimut, LeCode.UPente, LaExpe.IDExpe)) 
        return CalculerUneVisee(MaVisee, LeCode.UAzimut, LeCode.UPente, LaExpe.Declinaison, LaExpe.Inclinaison)
    #--- END PROC --------------------    
    #*********************************************************
    def GetMaxNode(self):
        M = -1
        for i in range(0, self.GetNbBranches()):
            QBra = self.GetBranche(i)
            if (QBra.NoeudDepart > M):
                M = QBra.NoeudDepart;
            if (QBra.NoeudArrivee > M):
                M = QBra.NoeudArrivee;
        return M
    #--- END PROC --------------------
    #*********************************************************       
    # matrice d assemblage 
    def MakeRMatrix(self):
        def beuh(QB, QJ):
            if (QB.NoeudDepart == (QJ)):
                return -1
            elif (QB.NoeudArrivee == (QJ)):
                return +1
            else:
                return  0
        AfficherMessage("MakeRMatrix")
       
        M = self.GetNbBranches() + 1
        N = self.GetNbJonctions() + 1
        # AfficherMessage(M, N)
        self.RMatrix = [[0 for j in range(1, self.GetNbJonctions() + 1)] for i in range(1, self.GetNbBranches() + 1)] # initialisation d une matrice (M,N) 
        for i in range(1, self.GetNbBranches()):
            if ((i % 10) == 10):
                AfficherMessage("-- Ligne %d" % (i))
            Br = self.GetBranche(i)  
            # AfficherMessage("Branche: %d: %d -> %d: %.2f, %.2f, %.2f" % (i, Br.NoeudDepart, Br.NoeudArrivee, Br.DeltaX, Br.DeltaY, Br.DeltaZ))            
            for j in range(1, self.GetNbJonctions()):
                self.RMatrix[i][j] = beuh(Br, j)
    #--- END PROC --------------------
    #*********************************************************
    # matrice de compensation: B = Rt * W * R
    def MakeBMatrix(self):
        AfficherMessage("MakeBMatrix")
        M = self.GetNbBranches() + 1
        N = self.GetNbJonctions() + 1
        # vecteurs index de valeurs non nulles de R
        self.LowIndex  = [0 for i in range(1, N)]
        self.HighIndex = [0 for i in range(1, N)]
        for i in range(1, self.GetNbJonctions()):
            for j in range(1, self.GetNbBranches()): 
                if (abs(self.RMatrix[j][i]) > 0):
                    self.LowIndex[i] = j
                    break
        for i in range(1, self.GetNbJonctions()): 
            for j in range(self.GetNbBranches() - 1, 0, -1): #downto
                if (abs(self.RMatrix[j][i]) > 0):
                    self.HighIndex[i] = j
                    break            
        # AfficherMessage(self.LowIndex)
        # AfficherMessage(self.HighIndex)
        # matrice de compensation 
        self.BMatrix = [[0 for j in range(1, N+1)] for i in range(1,N+1)] # initialisation d une matrice (M,N) 
        for i in range(1, self.GetNbJonctions()):
            if ((i % 10) == 0):
                AfficherMessage("-- Ligne %d" % (i))
            for j in range(1, self.GetNbJonctions()):
                ww = 0
                # for k in range(1, self.GetNbBranches()): #OK 
                for k in range(self.LowIndex[i]-1, self.HighIndex[i]+1):
                    ww = ww + self.RMatrix[k][i] * self.RMatrix[k][j]
                self.BMatrix[i][j] = ww
        for i in range(1, N-1):
            for j in range(i+1, N):
                self.BMatrix[i][j] = self.BMatrix[j][i]
    #--- END PROC --------------------
    #*********************************************************         
    def MakeSecondMembre(self, Axe):
        AfficherMessage("-- Second membre: %d " % (Axe))
        M = self.GetNbBranches() + 1
        N = self.GetNbJonctions() + 1
        self.SecMembre = [0 for i in range(1, N)]
        for i in range(1, self.GetNbJonctions()):
            ww = 0
            for k in range(1, self.GetNbBranches()):
                Br = self.GetBranche(k)
                if   (Axe == 1): WU = Br.DeltaX
                elif (Axe == 2): WU = Br.DeltaY
                elif (Axe == 3): WU = Br.DeltaZ
                ww = ww + self.RMatrix[k][i] * WU
            self.SecMembre[i] = ww
    #--- END PROC --------------------        
    #*********************************************************
    # factorisation des matrices: OK au 10/05/2014
    def SolveMatrix(self, Axe):
        AfficherMessage("FACTORISATION DE LA MATRICE DE COMPENSATION: Axe: %s" % (chr(87 + Axe)))
        
        if   (Axe == 1): WU = self.FDocuTopo.GetPoint0X()
        elif (Axe == 2): WU = self.FDocuTopo.GetPoint0Y()
        elif (Axe == 3): WU = self.FDocuTopo.GetPoint0Z()
        
        M = self.GetNbBranches() + 1
        N = self.GetNbJonctions() + 1
        XX = [0 for i in range(1, N+1)]
        V_Matrix = [[0 for j in range(1, N+1)] for i in range(1, N+1)]
        S_Vector = [0 for i in range(1, N+1)]
        AfficherMessage("-- Descente: V.V* = A")
        for i in range(1, self.GetNbJonctions()):
            if ((i % 40) == 0):
                AfficherMessage("-- Ligne %d" % (i))
            vv = 0
            for k in range(1, i):
                vv = vv + V_Matrix[i][k] ** 2
            V_Matrix[i][i] = sqrt(abs(self.BMatrix[i][i] - vv))
            for j in range(1+i, self.GetNbJonctions()):
                ww = 0
                for k in range(1, i): # for k := 1 to i-1
                    ww = ww + V_Matrix[i][k] * V_Matrix[j][k];
                V_Matrix[j][i] = (self.BMatrix[i][j] - ww) / (V_Matrix[i][i] + 1e-24)
        AfficherMessage("-- Triangularisation")
        for i in range(1, self.GetNbJonctions()):
            ww = 0
            for k in range(1, i): #i-1
                ww = ww + V_Matrix[i][k] * S_Vector[k];
            S_Vector[i] = (self.SecMembre[i] - ww) / (V_Matrix[i][i] + 1e-24)
        AfficherMessage("-- Remontee du systÃ¨me; inconnues recherchees")
        for i in range(self.GetNbJonctions(), 0, -1):
            ww = 0
            for k in range(1 + i, self.GetNbJonctions()):
                ww = ww + V_Matrix[k][i] * XX[k]
            XX[i] = (S_Vector[i] - ww) / (V_Matrix[i][i] + 1e-24) 
        #XX[0] := XX[1];
        # AfficherMessage(XX)
       
        for i in range(0, self.GetNbJonctions()): 
            JC = self.GetJonction(i)
            if   (Axe == 1):
                JC.X = XX[i] + self.FDocuTopo.GetPoint0X()
            elif (Axe == 2):
                JC.Y = XX[i] + self.FDocuTopo.GetPoint0Y()
            elif (Axe == 3):
                JC.Z = XX[i] + self.FDocuTopo.GetPoint0Z() 
            self.PutJonction(i, JC)
    #--- END PROC --------------------
    #*********************************************************
    # lister les noeuds
    def ListerNoeuds(self):  
        AfficherMessage("-- Coordonnees des %d noeuds" % (self.GetNbJonctions()))
        AfficherMessage("--- Xo = %.2f" % (self.FDocuTopo.GetPoint0X()))
        AfficherMessage("--- Yo = %.2f" % (self.FDocuTopo.GetPoint0Y()))
        AfficherMessage("--- Zo = %.2f" % (self.FDocuTopo.GetPoint0Z()))
        AfficherMessage("")
        for i in range(0, self.GetNbJonctions()): 
            JC = self.GetJonction(i)        
            AfficherMessage("%d, %d, %s, %.2f, %.2f, %.2f" % (i, JC.NoNoeud, JC.IDJonction, JC.X, JC.Y, JC.Z))
    #--- END PROC --------------------
    #*********************************************************
    # rÃ©partition des Ã©carts
    # calcul des coordonnÃ©es
    def RepartirEcarts(self):
        AfficherMessage("-- Repartition des ecarts")
        N1 = TJonction()
        N2 = TJonction()
        for i in range(1, self.GetNbBranches()):
            Br = self.GetBranche(i)
            N1 = self.GetJonction(Br.NoeudDepart)
            N2 = self.GetJonction(Br.NoeudArrivee)
            OffsetX = (N2.X - N1.X) - Br.DeltaX
            OffsetY = (N2.Y - N1.Y) - Br.DeltaY
            OffsetZ = (N2.Z - N1.Z) - Br.DeltaZ
            LC  = 0.00
            QPX = 0.00
            QPY = 0.00
            QPZ = 0.00
            # AfficherMessage("%d: N%d (%.2f, %.2f, %.2f) N%d (%.2f, %.2f, %.2f)- Delta = %.2f, %.2f, %.2f - Offset = %.2f, %.2f, %.2f" % \
                  # (i, Br.NoeudDepart , N1.X, N1.Y, N1.Z, \
                      # Br.NoeudArrivee, N2.X, N2.Y, N2.Z, Br.DeltaX, Br.DeltaY, Br.DeltaZ, \
                      # OffsetX, OffsetY, OffsetZ
                  # ))
            for j in range(0, Br.GetNbStations()):
                St  = Br.GetStation(j)
                LC += St.QLongDev
                R   = LC / Br.LongDev
                QPX += St.QDeltaX
                QPY += St.QDeltaY
                QPZ += St.QDeltaZ
                St.X = N1.X + QPX + OffsetX * R
                St.Y = N1.Y + QPY + OffsetY * R
                St.Z = N1.Z + QPZ + OffsetZ * R
                Br.PutStation(j, St)
                # AfficherMessage("%d, %d, %.2f, %.2f, %.2f" % (i, j, St.X, St.Y, St.Z))
            self.PutBranche(i, Br)
        AfficherMessage("-- RÃ©partition OK -- (ValidÃ©)--")
    #--- END PROC --------------------
    #*********************************************************
    def CalcViseeAntenne(self, VA, QNo):
        Result = TAntenne()
        try:
            Result = VA
            Result.ID = 0            
            EE = self.MyTableEntites.GetEntiteFromSerSt(VA.SerDep, VA.PtDep)
            VS = TStation()
            VS.SetValeurs(0, 0, 7, VA.Code, VA.Expe, VA.Longueur, VA.Azimut, VA.Pente, 0.00, 0.00, 0.00, 0.00, '', '')
            VU = self.CalculerVisee(VS)
            #AfficherMessage('-- : %d.%d - %.d, %.d - L %.2f, A %.2f P %.2f - X %.2f, Y %.2f' % (EE.Entite_Serie, EE.Entite_Station, \
            #                                                                      VA.Code, VA.Expe,  \
            #                                                                      VA.Longueur, VA.Azimut, VA.Pente, \
            #                                                                      VU.QDeltaX, VU.QDeltaY))
            DX = EE.Une_Station_2_X + VU.QDeltaX
            DY = EE.Une_Station_2_Y + VU.QDeltaY
            DZ = EE.Une_Station_2_Z + VU.QDeltaZ
            #  centerline
            Result.X1 = EE.Une_Station_2_X
            Result.Y1 = EE.Une_Station_2_Y
            Result.Z1 = EE.Une_Station_2_Z
            Result.X2 = DX
            Result.Y2 = DY
            Result.Z2 = DZ
        except:
            Result.ID = -1
        return Result
        #--- END PROC --------------------        
        
    #*********************************************************
    # calcul contours galeries
    def CalculContoursGaleries(self):
        #--------------------------------
        def TraiterBranche(QBranche):
            def SetProvViseeNulle():
                Result = TTemporaryStation()
                Result.NumSerie  = 0
                Result.NumPoint  = 0
                Result.stSecteur = 0
                Result.stCode    = 0
                Result.stExpe    = 0
                Result.Couleur      = 0
                Result.TypeGalerie  = 0
                Result.Date  = 0
                Result.Longueur  = 0.01
                Result.Azimut    = 0.00
                Result.Pente     = 0.00

                Result.LD       = 0.00
                Result.LG       = 0.00
                Result.HZ       = 0.00
                Result.HN       = 0.00
                Result.Commentaire  = 0.00
                Result.IDTerrainStation  = 0.00
                Result.X = 0.00
                Result.Y = 0.00
                Result.Z = 0.00
                return Result
            #--- END SUB SUB PROC --------------------
                
            def SetProvVisee(V1):
                Result = TTemporaryStation()
                Result.NumSerie  = QBranche.NoSerie
                Result.NumPoint  = V1.IDStation #  NumPoint =V1.NoViseeSer
                Result.stSecteur = V1.Secteur
                QExpe      = self.FDocuTopo.GetExpeByIndex(V1.Expe)
                QCode      = self.FDocuTopo.GetCodeByIndex(V1.Code)
                Result.stCode    = QCode.IDCode
                Result.stExpe    = QExpe.IDExpe
                Result.Couleur      = self.MyTableEntites.SetColorVisee(QExpe.IdxCouleur)
                Result.TypeVisee  = V1.TypeVisee
                Result.Date  = GetSecuredDate(QExpe.AnneeExpe, QExpe.MoisExpe, QExpe.JourExpe) # TODO Corriger dates
                Result.Longueur  = V1.Longueur
                Result.Azimut    = V1.Azimut
                Result.Pente     = V1.Pente

                Result.LD       = V1.LD
                Result.LG       = V1.LG
                Result.HZ       = V1.HZ
                Result.HN       = V1.HN
                Result.Commentaire  = V1.Commentaire
                Result.IDTerrainStation  = V1.IDTerrain
                Result.X = V1.X
                Result.Y = V1.Y
                Result.Z = V1.Z
                return Result
            #--- END SUB SUB PROC --------------------
            #--------------------
            Result  = False;
            TabVisee = []  # SetLength(TabVisee, 2 + NbPts);        # SetLength(TabVisee, 2 + EWE);
            NbPts = QBranche.GetNbStations()
            AReseau = self.FDocuTopo.GetReseau(QBranche.NoReseau)                                           # AReseau := FDocumentToporobot.GetReseau(QBranche.NoReseau);
            #TabVisee.append(QBranche.GetStation(0))
            # AfficherMessage("-------- Generation tableau provisoire: %d stations - NdDep = %d, NdArr = %d" % (NbPts, QBranche.NoeudDepart, QBranche.NoeudArrivee))
            # for i in range(0, NbPts):
                # EWE = SetProvVisee(QBranche.GetStation(i))
                # AfficherMessage("Station: %d  - %.2f, %.2f, %.2f - %.2f, %.2f, %.2f" % (i, EWE.Longueur, EWE.Azimut,  EWE.Pente, EWE.X, EWE.Y, EWE.Z))
            # GHTopo initialise systÃ©matiquement une visÃ©e 0 trÃ¨s courte -> au moins deux stations dans une branche.
            # Une protection a Ã©tÃ© placÃ©e pour les branches Ã  une seule station (entrÃ©es notamment)
            if (NbPts <= 2): # Une seule visÃ©e ? Utilisation des noeuds.
                V1 = SetProvVisee(QBranche.GetStation(NbPts - 1))
                QEntite = TEntiteEtendue() 
                QEntite.eCode       = V1.stCode
                QEntite.eExpe       = V1.stExpe
                QEntite.eSecteur    = V1.stSecteur
                QEntite.eReseau     = AReseau.IdxReseau
                QEntite.Type_Entite = V1.TypeVisee #2
                QEntite.DateLeve    = V1.Date
                QEntite.Entite_Serie    = QBranche.NoSerie
                QEntite.Entite_Station  = 1
                # donnÃ©es originales
                QEntite.oLongueur       = V1.Longueur
                QEntite.oAzimut         = V1.Azimut
                QEntite.oPente          = V1.Pente
                QEntite.oLG             = V1.LG
                QEntite.oLD             = V1.LD
                QEntite.oHZ             = V1.HZ
                QEntite.oHN             = V1.HN
                # centerline
                N1      = self.GetJonction(QBranche.NoeudDepart)
                N2      = self.GetJonction(QBranche.NoeudArrivee)
                QEntite.Une_Station_1_X = N1.X 
                QEntite.Une_Station_1_Y = N1.Y 
                QEntite.Une_Station_1_Z = N1.Z 
                QEntite.Une_Station_2_X = N2.X 
                QEntite.Une_Station_2_Y = N2.Y 
                QEntite.Une_Station_2_Z = N2.Z 
                # angle: pour une seule visÃ©e
                AlphaV       = atan2(QEntite.Une_Station_2_Y - QEntite.Une_Station_1_Y, \
                                     QEntite.Une_Station_2_X - QEntite.Une_Station_1_X
                                    )
                AlphaG = AlphaV + pi / 2
                # AlphaD = AlphaV - pi / 2
                # habillage
                qCosAlphaG = cos(AlphaG)
                qSinAlphaG = sin(AlphaG)
                QEntite.X1PD = QEntite.Une_Station_1_X + QEntite.oLD * qCosAlphaG # cos(AlphaD)
                QEntite.Y1PD = QEntite.Une_Station_1_Y + QEntite.oLD * qSinAlphaG # sin(AlphaD)
                QEntite.X1PG = QEntite.Une_Station_1_X - QEntite.oLG * qCosAlphaG # cos(AlphaG)
                QEntite.Y1PG = QEntite.Une_Station_1_Y - QEntite.oLG * qSinAlphaG # sin(AlphaG)
                QEntite.Z1PH = QEntite.Une_Station_1_Z + QEntite.oHZ
                QEntite.Z1PB = QEntite.Une_Station_1_Z - QEntite.oHN
                
                QEntite.X2PD = QEntite.Une_Station_2_X + QEntite.oLD * qCosAlphaG # cos(AlphaD)
                QEntite.Y2PD = QEntite.Une_Station_2_Y + QEntite.oLD * qSinAlphaG # sin(AlphaD)
                QEntite.X2PG = QEntite.Une_Station_2_X - QEntite.oLG * qSinAlphaG # cos(AlphaG)
                QEntite.Y2PG = QEntite.Une_Station_2_Y - QEntite.oLG * qSinAlphaG # sin(AlphaG)
                QEntite.Z2PH = QEntite.Une_Station_2_Z + QEntite.oHZ
                QEntite.Z2PB = QEntite.Une_Station_2_Z - QEntite.oHN
                # couleur pour dÃ©gradÃ©
                QEntite.ColourByDepth = rgb(0,0,255)
                # commentaires
                QEntite.oIDLitteral   = GetIDStation(QBranche.NoSerie, V1)
                QEntite.oCommentaires = V1.Commentaire
                if (QEntite.Type_Entite != tgENTRANCE):
                    self.MyTableEntites.AddEntite(QEntite)
            else:
                for St in range(1, NbPts):
                    V1 = SetProvVisee(QBranche.GetStation(St-1))
                    V2 = SetProvVisee(QBranche.GetStation(St))
                    if   (St == 1):           # station de dÃ©but = perpendiculaire Ã  la visÃ©e 
                        AlphaV = atan2(V2.Y - V1.Y, V2.X - V1.X)
                        AlphaG = AlphaV + pi / 2
                        # AlphaD = AlphaV - pi / 2
                    elif (St == (NbPts - 1)): # station de fin = perpendiculaire Ã  la visÃ©e
                        AlphaV = atan2(V2.Y - V1.Y, V2.X - V1.X)
                        AlphaG = AlphaV + pi / 2
                        # AlphaD = AlphaV - pi / 2
                    else:
                        V3 = SetProvVisee(QBranche.GetStation(St+1))
                        AlphaG = CalculerAngleBissecteur(V2.X - V1.X, \
                                                         V2.Y - V1.Y, \
                                                         V3.X - V2.X, \
                                                         V3.Y - V2.Y)
                        # AlphaG = AlphaD + pi
                    qCosAlphaG = cos(AlphaG)
                    qSinAlphaG = sin(AlphaG)
                    
                    QEntite = TEntiteEtendue()
                    QEntite.eCode       = V2.stCode
                    QEntite.eExpe       = V2.stExpe
                    QEntite.eSecteur    = V2.stSecteur
                    QEntite.eReseau     = AReseau.IdxReseau
                    QEntite.Type_Entite = V2.TypeVisee 
                    QEntite.DateLeve    = V2.Date

                    QEntite.Entite_Serie    = QBranche.NoSerie
                    QEntite.Entite_Station  = V2.NumPoint
                    # donnÃ©es originales
                    QEntite.oLongueur       = V2.Longueur
                    QEntite.oAzimut         = V2.Azimut
                    QEntite.oPente          = V2.Pente
                    QEntite.oLG             = V2.LG
                    QEntite.oLD             = V2.LD
                    QEntite.oHZ             = V2.HZ
                    QEntite.oHN             = V2.HN
                    # centerline
                    QEntite.Une_Station_1_X = V1.X 
                    QEntite.Une_Station_1_Y = V1.Y 
                    QEntite.Une_Station_1_Z = V1.Z 
                    QEntite.Une_Station_2_X = V2.X 
                    QEntite.Une_Station_2_Y = V2.Y 
                    QEntite.Une_Station_2_Z = V2.Z 
                    # habillage
                    qCosAlphaG = cos(AlphaG)
                    qSinAlphaG = sin(AlphaG)
                    QEntite.X1PD = QEntite.Une_Station_1_X + V1.LD * qCosAlphaG # cos(AlphaD)
                    QEntite.Y1PD = QEntite.Une_Station_1_Y + V1.LD * qSinAlphaG # sin(AlphaD)
                    QEntite.X1PG = QEntite.Une_Station_1_X - V1.LG * qCosAlphaG # cos(AlphaG)
                    QEntite.Y1PG = QEntite.Une_Station_1_Y - V1.LG * qSinAlphaG # sin(AlphaG)
                    QEntite.Z1PH = QEntite.Une_Station_1_Z + V1.HZ
                    QEntite.Z1PB = QEntite.Une_Station_1_Z - V1.HN
                   
                    QEntite.X2PD = QEntite.Une_Station_2_X + V2.LD * qCosAlphaG # cos(AlphaD)
                    QEntite.Y2PD = QEntite.Une_Station_2_Y + V2.LD * qSinAlphaG # sin(AlphaD)
                    QEntite.X2PG = QEntite.Une_Station_2_X - V2.LG * qCosAlphaG # cos(AlphaG)
                    QEntite.Y2PG = QEntite.Une_Station_2_Y - V2.LG * qSinAlphaG # sin(AlphaG)
                    QEntite.Z2PH = QEntite.Une_Station_2_Z + V2.HZ
                    QEntite.Z2PB = QEntite.Une_Station_2_Z - V2.HN
                    # couleur pour dÃ©gradÃ©
                    QEntite.ColourByDepth = rgb(0,0,255)
                    # commentaires
                    QEntite.oIDLitteral   = GetIDStation(QBranche.NoSerie, V1)
                    QEntite.oCommentaires = V2.Commentaire
                    # </with QEntite>
                    # AfficherMessage("%d, %d_%d,%s,  %.2f, %.2f, %.2f, , %.2f, %.2f, %.2f" % (i,  QEntite.Entite_Serie, QEntite.Entite_Station , QEntite.oIDLitteral, \
                                                                               # QEntite.Une_Station_1_X, QEntite.Une_Station_1_Y, QEntite.Une_Station_1_Z, \
                                                                               # QEntite.Une_Station_2_X, QEntite.Une_Station_2_Y, QEntite.Une_Station_2_Z))
                    if (QEntite.Type_Entite != tgENTRANCE):
                        self.MyTableEntites.AddEntite(QEntite)  
            Result = True
            return Result
        #--- END SUB PROC --------------------
        # </def TraiterBranche(QBranche, Br):>
        #----------------------------------------------------                       
       
        #----------------------------------------------------
        def CloturerListeVisees(self):
            pass
        #--- END SUB PROC --------------------
           
        #+++++++++++++++++++++++++++++++++++
        AfficherMessage("-- Calcul contours galeries")
        
        NbBrchs = self.GetNbBranches()
        AfficherMessage("-> Traitement des %d branches" % (NbBrchs)) 
        for i in range(1, NbBrchs):
            TraiterBranche(self.GetBranche(i))
        AfficherMessage("-- Contours galeries OK")

        
    #*********************************************************
    # calculer les visÃ©es en antenne
    def TraiterViseesEnAntenne(self):
        NbA = self.FDocuTopo.GetNbAntennes()
        AfficherMessage("--- TraiterViseesEnAntenne: %d" % (NbA))
        if (NbA > 1):
            for n in range(1, NbA):
                VA = self.FDocuTopo.GetAntenne(n)
                QAntenne = self.CalcViseeAntenne(VA, n)
                if (QAntenne.ID == 0):
                    self.MyTableEntites.AddAntenne(QAntenne)
                #else:
                #    AfficherMessage('CalcViseeAntenne: (%d) %d, %d - %.3f, %.3f, %.3f - %.2f, %.2f, %.2f' % (QAntenne.ID, QAntenne.SerDep, QAntenne.PtDep
                    
            AfficherMessage('%d antennes ajoutees' % (self.MyTableEntites.GetNbAntennes()))
        #--- END SUB PROC --------------------
    #*********************************************************
    # ajouter les entrees
    def AjouterLesEntrees(self):
       Nb = self.FDocuTopo.GetNbEntrees()
       
       for i in range(0, Nb):
           Entrance = self.FDocuTopo.GetEntree(i)
           self.MyTableEntites.AddEntrance(Entrance)
           
#*****************************************************************
        

    
