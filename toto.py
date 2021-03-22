import string
from os import *
from sys import *
from platform import *

from tkinter import *
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
    QFileName = askopenfilename(title="Ouvrir un fichier",filetypes = QFilter)
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


# Classe principale de l'application
        
class TApplication(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.Initialise()
        
    def Initialise(self):
        self.title('PyGHTopo')
        # Barre de menus
        self.MenuBar = Menu(self)
        # menu Fichier
        self.mnuFichier = Menu(self.MenuBar, tearoff=0)
        self.mnuFichier.add_command(label = 'Ouvrir', command = self.acOuvrirXTB)
        self.mnuFichier.add_command(label = 'Quitter', command = self.acQuitter)
        
        # ...
        self.MenuBar.add_cascade(label='Fichier', menu=self.mnuFichier)
        # menu Calcul ...
        self.mnuCalcul = Menu(self.MenuBar, tearoff=0)
        self.mnuCalcul.add_command(label = 'Lancer', command = self.acCalculerLaTopo)
        # ...
        self.MenuBar.add_cascade(label='Calcul', menu=self.mnuCalcul)
        # menu DistoX ...
        self.mnuDistoX = Menu(self.MenuBar, tearoff=0)
        self.mnuDistoX.add_command(label = 'Connecter')
        # ...
        self.MenuBar.add_cascade(label='DistoX2', menu=self.mnuDistoX)
       
        # et on flushe le tout
        self.config(menu=self.MenuBar)

        # Boutons
        #btnQuit = AddButton(self, 10, 20, 100, 25, 'Quitter', self.acQuitter)

        
        # empêcher certains comportements (auto-adjust lors d'une saisie de texte
        self.update()
        self.geometry(self.geometry())       

    def Finalise(self):
        pass

    def OuvrirUneTopo(self, FichierXTB):
        self.MyDocTopo = TDocuTopo('miaou', 'toto')

        self.MyDocTopo.ChargerFichierTab(FichierXTB)
        
    
    
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
        self.MyBDDEntites.ListerLesEntites()
        MyVisualisateur2D = TVisualisateur2D(self.MyBDDEntites, 1000, 1000)
        MyVisualisateur2D.Flush()

    def acOuvrirXTB(self):
        QFileName = ''
        QFilters  = [('Fichiers GHTopo XTB','.xtb'),('Tous','.*')]
       
        R = DoDialogOpenFile('', QFilters, QFileName)
        DoOpen    = R[0] # résultat de la fonction précédente
        QFileName = R[1] # paramètres 'out' de la fonction précédente
        if (DoOpen):
            print("Fichier %s prêt à être ouvert" % (QFileName))
            self.OuvrirUneTopo(QFileName)
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
        
#************************************************

def Main():
    Application = TApplication(None)
    
    Application.mainloop()
    
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





