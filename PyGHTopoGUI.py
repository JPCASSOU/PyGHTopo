# -*-coding:utf-8 -*

import string
from os import *
from sys import *
from platform import *

from tkinter import *
from tkinter.tix import *
from tkinter.messagebox import *
from tkinter.filedialog import *

from math import *
from functions import *
from types_donnees import *
from ToporobotClasses import *
from CodeCalcul import *
from VisuGraphique import *
# Toolbox, à mettre dans une unité séparée

def QuestionOuiNon(Titre, Msg):
    return askyesno(Titre, Msg)

# Fonctions de la forme
# function DoDialogOpenFile(const QInitialDir, QFilter: string; out QFileName: string): Boolean;
def DoDialogOpenFile(QInitialDir, QFilter, QFileName):
    QFileName = askopenfilename(title="Ouvrir un fichier", filetypes = QFilter)
    WU = len(Trim(QFileName))
    # Le résultat va dans un tableau
    # Valeur de retour 0: Le booléen (VR proprement dite)
    # Valeur de retour 1: Le contenu de la variable équivalente au paramètre en 'out' ou 'var'
    return (WU > 0), QFileName 

def DoDialogSaveFile(QInitialDir, QFilter, QFileName):
    return False

def AddButton(Parent, x, y, l, h, Caption, onClick):
    EWE = Button(Parent, width = l, height = h, text = Caption, command = onClick)
    EWE.pack(side = LEFT, padx = x, pady = y)
    return EWE

def BeginMenuBar(Parent):
    return Menu(Parent)

def EndMenuBar(Parent, QMenuBar):
    Parent.config(menu = QMenuBar)

def BeginPullDownMenu(QMenuBar):
    return  Menu(QMenuBar, tearoff=0)

def PullDownMenuAddItem(QPullDownMenu, QCaption, QCommand):
    QPullDownMenu.add_command(label = QCaption, command = QCommand)

def PullDownMenuAddSeparator(QPullDownMenu):
    QPullDownMenu.add_separator()
    
def EndPullDownMenu(QMenuBar, QPullDownMenu, QCaption):
    return QMenuBar.add_cascade(label = QCaption, menu = QPullDownMenu)

def AddListBox(Parent, X, Y, L, H, QItems, QItemIndex):
    Result = Listbox(Parent)
    n = len(QItems)
    for i in range(0, n):
        Result.insert(i+1, QItems[i])
    Result.pack(side = TOP, padx = X, pady = Y)
    return Result

def AddComboBox(Parent, X, Y, L, H, QItems, QCommand, QItemIndex):
    Parent.MyFrame = Frame(Parent, bd=1, relief=RAISED)
    Parent.MyFrame.pack(side = TOP, padx = X, pady = Y)
    Result = tkinter.tix.ComboBox(Parent.MyFrame, label="Encoding: ", dropdown=1,  command = QCommand, editable=0)
    n = len(QItems)
    for i in range(0, n):
        Result.insert(i+1, QItems[i])
    Result.pack()
    return Result



# Classe principale de l'application
        
class TApplication(tix.Tk):
    def __init__(self, parent, **kwargs):
        tix.Tk.__init__(self, parent)
        self.parent = parent
        self.Initialise()
        
    def Initialise(self):
        self.title('PyGHTopo')
        # Barre de menus
        #self.MenuBar = Menu(self)
        self.MenuBar = BeginMenuBar(self)
        # menu Fichier
        self.mnuFichier = BeginPullDownMenu(self.MenuBar)
        PullDownMenuAddItem(self.mnuFichier, 'Ouvrir XTB', self.acOuvrirXTB)
        PullDownMenuAddItem(self.mnuFichier, 'Ouvrir GTX', self.acOuvrirGTX)
        PullDownMenuAddSeparator(self.mnuFichier)
        PullDownMenuAddItem(self.mnuFichier, 'Quitter', self.acQuitter)
        # ...
        #--self.MenuBar.add_cascade(label='Fichier', menu=self.mnuFichier)
        EndPullDownMenu(self.MenuBar, self.mnuFichier, 'Fichier')
        # menu Calcul ...
        self.mnuCalcul = BeginPullDownMenu(self.MenuBar)
        PullDownMenuAddItem(self.mnuCalcul, 'Lancer', self.acCalculerLaTopo)
        
        # ...
        EndPullDownMenu(self.MenuBar, self.mnuCalcul, 'Calcul')
        # menu DistoX ...
        self.mnuDistoX = BeginPullDownMenu(self.MenuBar)
        PullDownMenuAddItem(self.mnuDistoX, 'Connecter', self.acConnecterDistoX2)
        # ...
        EndPullDownMenu(self.MenuBar, self.mnuDistoX, 'DistoX2')
       
        # et on flushe le tout
        # self.config(menu=self.MenuBar)
        EndMenuBar(self, self.MenuBar)

        # Boutons
        #btnQuit = AddButton(self, 10, 20, 100, 25, 'Quitter', self.acQuitter)

        #liste d'encodages
        ListeEncodages = []
        ListeEncodages.append('utf-8')
        ListeEncodages.append('cp1252')
        ListeEncodages.append('cp850')
        ListeEncodages.append('latin-1')
        self.lsbEncodage = AddListBox(self, 10, 10, 100, 5, ListeEncodages, 0)
        #self.cmbEncodage = AddComboBox(self, 10, 10, 100, 5, ListeEncodages, self.acDummy, 0)
        
        
        # empêcher certains comportements (auto-adjust lors d'une saisie de texte
        self.update()
        self.geometry(self.geometry())       
    def acDummy(self, evt):
        pass
    
    def Finalise(self):
        pass

    def OuvrirUneTopo(self, FichierXTB):
        # NOTA: Le Python ne sait pas reconnaître de lui-même l'encodage des fichiers texte
        #       L'encodage doit être explicitement spécifié
        # extraire l'encodage de la listbox
        #Idx = self.lsbEncodage.curselection()
        #WU  = self.lsbEncodage.get(Idx)

        Idx = self.lsbEncodage.curselection()
        WU  = self.lsbEncodage.get(Idx)
        
        self.MyDocTopo = TDocuTopo('miaou', 'toto')
        self.MyDocTopo.ChargerFichierTab(FichierXTB, WU) # Windaube: cp1252, sinon utf-8
        
        self.MyDocTopo.ListerLesEntrees()
        self.MyDocTopo.ListerLesReseaux()
        self.MyDocTopo.ListerLesSecteurs()
        self.MyDocTopo.ListerLesCodes()
        self.MyDocTopo.ListerLesExpes()
        AfficherMessage("----------------------------")
        
    def OuvrirUneTopoGTX(self, FichierGTX):
        self.MyDocTopo = TDocuTopo('miaou', 'toto')
        self.MyDocTopo.ChargerFichierGTX(FichierGTX) # Windaube: cp1252, sinon utf-8
        
        
        self.MyDocTopo.ListerLesEntrees()
        self.MyDocTopo.ListerLesReseaux()
        self.MyDocTopo.ListerLesSecteurs()
        self.MyDocTopo.ListerLesCodes()
        self.MyDocTopo.ListerLesExpes()
        AfficherMessage("----------------------------")


    def CalculerLaTopo(self):    
        MyCodeCalcul = TCodeCalcul('EWE', 'WU')
        self.MyBDDEntites = TTableDesEntites()
        MyCodeCalcul.SetDocTopo(self.MyDocTopo, self.MyBDDEntites)
        MyCodeCalcul.AjouterLesEntrees()
        MyCodeCalcul.RecenserJonctions()
        MyCodeCalcul.RecenserBranches()
        AfficherMessage("Noeud max: %d" % (MyCodeCalcul.GetMaxNode()))
        MyCodeCalcul.MakeRMatrix()
        MyCodeCalcul.MakeBMatrix()

        for i in range(1, 4):
            MyCodeCalcul.MakeSecondMembre(i)
            MyCodeCalcul.SolveMatrix(i)
        #MyCodeCalcul.ListerNoeuds()
        MyCodeCalcul.RepartirEcarts()
        MyCodeCalcul.CalculContoursGaleries()
        MyCodeCalcul.TraiterViseesEnAntenne()
   
    def AfficherLaTopo(self):
        # démarrer visu graphique
        self.MyBDDEntites.SetMinMax(20.00)
        #self.MyBDDEntites.ListerLesEntites()
        MyVisualisateur2D = TVisualisateur2D(self, self.MyBDDEntites, 1000, 1000)
        MyVisualisateur2D.Flush()

    def acOuvrirXTB(self):
        QFileName = ''
        QFilters  = [('Fichiers GHTopo XTB','.xtb'),('Tous','.*')]
        
        # Ecriture 1: Récupération dans des variables
        DoOpen, QFileName = DoDialogOpenFile('', QFilters, QFileName)
        # Ecriture 2: Récupération dans un tuple (tableau)
        # R = DoDialogOpenFile('', QFilters, QFileName)
        # DoOpen    = R[0] # résultat de la fonction précédente
        # QFileName = R[1] # paramètres 'out' de la fonction précédente
        if (DoOpen):
            print("Fichier %s prêt à être ouvert" % (QFileName))
            self.OuvrirUneTopo(QFileName)
            self.CalculerLaTopo()
            self.AfficherLaTopo()
        else:
            print('Action abandonnée')
            
    def acOuvrirGTX(self):
        QFileName = ''
        QFilters  = [('Fichiers GHTopo XML','.gtx'),('Tous','.*')]
        
        # Ecriture 1: Récupération dans des variables
        DoOpen, QFileName = DoDialogOpenFile('', QFilters, QFileName)
        # Ecriture 2: Récupération dans un tuple (tableau)
        # R = DoDialogOpenFile('', QFilters, QFileName)
        # DoOpen    = R[0] # résultat de la fonction précédente
        # QFileName = R[1] # paramètres 'out' de la fonction précédente
        if (DoOpen):
            print("Fichier %s prêt à être ouvert" % (QFileName))
            self.OuvrirUneTopoGTX(QFileName)
            self.CalculerLaTopo()
            self.AfficherLaTopo()
        else:
            print('Action abandonnée')
        
    def acCalculerLaTopo(self):
        self.CalculerLaTopo()
        self.AfficherLaTopo()

        
    def acQuitter(self):
        if (QuestionOuiNon('PyGHTopo', 'Quitter')):
            self.Finalise()
            self.destroy()  # TApplication.Terminate()

    def acConnecterDistoX2(self):
        pass

    def Run(self): # pour analogie avec le TApplication de Delphi
        self.mainloop()
        
#************************************************

def Main():
    Application = TApplication(None)
    Application.Run()
    
#************************************************

Main()        
        
# Menu
##
##
##lbLabel1 = Label(MainFrm, text="hello world!", bg="red")
##lbLabel1.pack()
##
##canvas = Canvas(MainFrm, width=300, height=300, background='yellow')
##ligne1 = canvas.create_line(75, 0, 75, 120)
##ligne2 = canvas.create_line(0, 60, 150, 60)
##txt = canvas.create_text(75, 60, text="Cible", font="Arial 16 italic", fill="blue")
##canvas.pack(side=LEFT, padx=30, pady=30)





