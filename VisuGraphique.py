# -*-coding:Latin-1 -*
import string
from tkinter import *
from math import *
from functions import *
from types_donnees import *
from UnitEntites import *
# Exercice: Deuxième fenêtre
from dlgFenetreFille import TFenetreFille



class TVisualisateur2D(Toplevel):
    def __init__(self, Parent, MyBDDEntites, QW, QH):
        Toplevel.__init__(self, Parent)
        self.protocol("WM_DELETE_WINDOW", self.OnClose)
        # le dialogue apparaît au dessus de son conteneur
        self.transient (Parent)
        self.title('Vue en plan') 
        # Ancestor = fenêtre qui ouvre le Dialogue
        self.Ancestor = Parent
        # rendre la fenêtre modale
        self.grab_set()
        
        #self.ByRoot = tix.Tk()   # ByRoot = fenêtre racine, prononcé comme biroute xD
        #self.ByRoot.title("Vue en plan")
    
    
    
        self.FBDDEntites = MyBDDEntites
        self.VueWidth  = QW
        self.VueHeight = QH
        print("Init Visu 2D: %d entites" % (self.FBDDEntites.GetNbEntites()))
        C1 = self.FBDDEntites.GetCoinBasGauche()
        C2 = self.FBDDEntites.GetCoinHautDroit()
        self.SetViewLimits(C1.X, C1.Y, C2.X, C2.Y, 50.00)
        
        
        # cadre contenant la vue
        self.pnlVue = tix.Frame(self, borderwidth=2, relief=GROOVE)
        self.MyVue = tix.Canvas(self.pnlVue, width=800, height=800, background=("#FFFFFF"))
        self.MyVue.pack()
        self.pnlVue.pack(side=LEFT)
        # bouttons
        self.pnlButtons = tix.Frame(self, borderwidth=2, relief=GROOVE)
        self.btnZoomPlus  = tix.Button(self.pnlButtons, text='Zoom +'    , command=self.acZoomPlus).grid(row=0, column=0) 
        self.btnResetVue  = tix.Button(self.pnlButtons, text='Reset vue' , command=self.acResetVue).grid(row=0, column=1)       
        self.btnZoomMoins = tix.Button(self.pnlButtons, text='Zoom -'    , command=self.acZoomMoins).grid(row=0, column=2) 
        
        self.btnPanNW     = tix.Button(self.pnlButtons, text='Pan NW'    , command=self.acPanNW).grid(row=1, column=0)
        self.btnPanNN     = tix.Button(self.pnlButtons, text='Pan NN'    , command=self.acPanNN).grid(row=1, column=1)
        self.btnPanNE     = tix.Button(self.pnlButtons, text='Pan NE'    , command=self.acPanNE).grid(row=1, column=2)
        
        self.btnPanWW     = tix.Button(self.pnlButtons, text='Pan WW'    , command=self.acPanWW).grid(row=2, column=0)
        #self.btnPanNN     = tix.Button(self.pnlButtons, text='Pan NN'    , command=self.acPanNN).grid(row=1, column=1)
        self.btnPanEE     = tix.Button(self.pnlButtons, text='Pan EE'    , command=self.acPanEE).grid(row=2, column=2)
        
        self.btnPanSW     = tix.Button(self.pnlButtons, text='Pan SW'    , command=self.acPanSW).grid(row=3, column=0)
        self.btnPanSN     = tix.Button(self.pnlButtons, text='Pan SS'    , command=self.acPanSS).grid(row=3, column=1)
        self.btnPanSE     = tix.Button(self.pnlButtons, text='Pan SE'    , command=self.acPanSE).grid(row=3, column=2)
        
        self.pnlButtons.pack()
        
        self.btnClose     = tix.Button(self, text='Fermer'    , command=self.acFormClose)
        self.btnClose.pack(side=BOTTOM)
        

        
        
        # premier dessin
        self.DessinerALArrache()
        
    def acResetVue(self):
        C1 = self.FBDDEntites.GetCoinBasGauche()
        C2 = self.FBDDEntites.GetCoinHautDroit()
        self.SetViewLimits(C1.X, C1.Y, C2.X, C2.Y, 50.00)
        self.DessinerALArrache()
    
    def acZoomPlus(self):
        self.SetViewLimits(self.FRegionXMini + 20.00, self.FRegionYMini + 20.00, self.FRegionXMaxi - 20.00, self.FRegionYMaxi - 20.00, 0)
        self.DessinerALArrache()
    def acZoomMoins(self):
        self.SetViewLimits(self.FRegionXMini - 20.00, self.FRegionYMini - 20.00, self.FRegionXMaxi + 20.00, self.FRegionYMaxi + 20.00, 0)
        self.DessinerALArrache()
    def acPanNW(self):
        self.DeplacerVue(  20, -20)
    def acPanNN(self):
        self.DeplacerVue(   0, -20)
    def acPanNE(self):
        self.DeplacerVue( -20, -20)
    def acPanWW(self):
        self.DeplacerVue(  20,   0)
    
    def acPanEE(self):
        self.DeplacerVue( -20,   0)   
        
    def acPanSW(self):
        self.DeplacerVue(  20,  20)
    def acPanSS(self):
        self.DeplacerVue(   0,  20)
    def acPanSE(self):
        self.DeplacerVue( -20,  20)        
        
    def DeplacerVue(self, OffsetX, OffsetY):
        self.SetViewLimits(self.FRegionXMini + OffsetX, self.FRegionYMini + OffsetY, self.FRegionXMaxi + OffsetX, self.FRegionYMaxi + OffsetY, 0)
        self.DessinerALArrache()
        
    
    # Fermeture de la fenêtre
    def acFormClose (self, AEvent = None) :
        self.initial_focus.focus_set()
        # effacement avant de supprimer (pour le rendu)
        self.withdraw()
        # nécessaire si dans apply() on utilise des éléments
        # qui doivent être visibles pour fournir des données
        self.update_idletasks()
        self.apply()
        self.OnClose()
        
    def OnClose (self, AEvent = None) :
        self.Ancestor.focus_set()
        self.destroy()
        

        
        
    #----------------------------------------
    # Création de widgets
    #----------------------------------------
    def CreateButton(self, Parent, x, y, l, h, Caption, OnClickProc):
        QButton = Button(Parent, width=l, height=h, text=Caption, command=OnClickProc)
        QButton.pack(padx=x, pady=y)    
    # ---------------------------------------
    # Evenements de widgets
    # ---------------------------------------
    def btnWinChildOnClick(self):
        MyFenetreFille = TFenetreFille(self)
    def btnTitiOnClick(self):
        print("Bouton Titi enfonce")
    def btnLuluOnClick(self):
        print("Bouton Lulu enfonce")
    
    # ---------------------------------------
    def GetRYMaxi(self):
        self.FRappHLVue    = self.VueHeight / self.VueWidth;                          # calcul du rapport Hauteur/largeur de vue
        self.FRappScrReal  = self.VueWidth / (self.FRegionXMaxi - self.FRegionXMini); # calcul du rapport Ecran/Réel
        self.FInvRappScrReal = 1 / self.FRappScrReal;
        # calcul de la hauteur de visualisation
        return self.FRegionYMini + (self.FRegionXMaxi - self.FRegionXMini) * self.FRappHLVue;
        
    # ---------------------------------------
    def GetCoordsPlan(self, QX, QY):
        Result = TPoint2Di(floor((QX - self.FRegionXMini) * self.FRappScrReal), \
                          floor((self.FRegionYMaxi - QY) * self.FRappScrReal));
        return Result
    # ---------------------------------------    
    def SetViewLimits(self, qX1, qY1, qX2, qY2, Marge):
        print("-- SetViewLimits %.2f, %.2f, %.2f, %.2f" % (qX1, qY1, qX2, qY2))
        self.FRegionXMini = qX1 - Marge
        self.FRegionXMaxi = qX2 + Marge
        self.FRegionYMini = qY1 - Marge
        self.FRegionYMaxi = qY2 + Marge
        # Redéfinition de la hauteur maxi
        self.FRegionYMaxi = self.GetRYMaxi();
    # ---------------------------------------
    def DessinerALArrache(self): # Tracé OK - DONE: Type de galeries, couleurs, ...
        print("--- Tracer centerlines a l arrache")
        self.MyVue.create_rectangle(0, 0, self.VueHeight, self.VueWidth, fill="#FFFFFF")
        for i in range(1,  self.FBDDEntites.GetNbEntites()): # centerlines
            EWE = self.FBDDEntites.GetEntite(i)
            if (1 == 1):
            #if (EWE.Type_Entite != 7):
                # centerlines
                PP1 = self.GetCoordsPlan(EWE.Une_Station_1_X, EWE.Une_Station_1_Y)
                PP2 = self.GetCoordsPlan(EWE.Une_Station_2_X, EWE.Une_Station_2_Y)
                self.MyVue.create_line(PP1.X, PP1.Y, PP2.X, PP2.Y, fill="#0000FF")
                # sections 
                PP1 = self.GetCoordsPlan(EWE.X2PD, EWE.Y2PD)
                PP2 = self.GetCoordsPlan(EWE.X2PG, EWE.Y2PG)
                self.MyVue.create_line(PP1.X, PP1.Y, PP2.X, PP2.Y, fill="#808080")
                # textes
                #WU = '%d.%d' % (EWE.Entite_Serie, EWE.Entite_Station)
                #self.MyVue.create_text(PP2.X, PP2.Y, text = WU)
        # visées radiantes
        Nb = self.FBDDEntites.GetNbAntennes()
        print('    %d antennes' %(Nb))
        if (Nb > 0):
            for i in range(1, Nb): # antennes
                WU = self.FBDDEntites.GetAntenne(i)
                #print('%.2f, %.2f > %.2f, %.2f' % (WU.X1, WU.Y1, WU.X2, WU.Y2))
                PP1 = self.GetCoordsPlan(WU.X1, WU.Y1)
                PP2 = self.GetCoordsPlan(WU.X2, WU.Y2)
                self.MyVue.create_line(PP1.X, PP1.Y, PP2.X, PP2.Y, fill="#808080")

        # entrées
        Nb = self.FBDDEntites.GetNbEntrances()
        for i in range(0, Nb):
            MyEntrance = self.FBDDEntites.GetEntrance(i)
            # AfficherMessage('%d - %s' % (i, MyEntrance.eNomEntree))
            WU = '%s' % (MyEntrance.eNomEntree)
            PP1 = self.GetCoordsPlan(MyEntrance.eXEntree - 2, MyEntrance.eYEntree - 2)
            PP2 = self.GetCoordsPlan(MyEntrance.eXEntree + 2, MyEntrance.eYEntree + 2)
            self.MyVue.create_oval(PP1.X, PP1.Y, PP2.X, PP2.Y, fill="#FF8080")
            self.MyVue.create_text(PP2.X + 3 , PP2.Y + 3, text = WU) 
            
        
    # ---------------------------------------
    def Flush(self):
        self.mainloop()
    # ---------------------------------------
# ============================================
