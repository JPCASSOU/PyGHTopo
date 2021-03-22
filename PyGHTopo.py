# -*-coding:utf-8 -*
# Sous Linux, remplacer Latin-1 par Utf-8
import string

from math import *
from functions import *
from types_donnees import *
from ToporobotClasses import *
from CodeCalcul import *
from VisuGraphique import *
from os import *
from sys import *
from platform import *

#version = platform.python_version_tuple()

AfficherMessage("OS de type: %s" % (os.name))
#AfficherMessage("Python Version %s.%s.%s" % (version[0], version[1], version[2]))
#AfficherMessage("chemin python: %s" % (sys.executable))
AfficherMessage("-------------------------------------------------")
           
def Main():

    # MyDirectory = '/storage/sdcard0/Python/PyGHTopo_20160619/' 
    MyDirectory = './' 

    MyDocTopo = TDocuTopo('miaou', 'toto')
    
      
    choi = 0
    # PageEncoding = 'utf-8'
    PageEncoding = 'cp1252'
    if   (choi == 0): MyDocTopo.ChargerFichierTab( MyDirectory + 'Toporabot.xtb', PageEncoding)
    elif (choi == 1): MyDocTopo.ChargerFichierTab( MyDirectory + '0_Reseau_Ardengost_20160611_11.xtb', PageEncoding)
    elif (choi == 2): MyDocTopo.ChargerFichierTab( MyDirectory + '00_Grottes_du_Roy.xtb', PageEncoding)
    elif (choi == 3): MyDocTopo.ChargerFichierTab( MyDirectory + '00_Grottes_Saint_Marcel.xtb', PageEncoding)
    elif (choi == 4): MyDocTopo.ChargerFichierTab( MyDirectory + '0_Bellegarde_20141222_georef.xtb', PageEncoding)
    elif (choi == 5): MyDocTopo.ChargerFichierTab( MyDirectory + '00_Roy_Reine_Fou_20150715_12bis.xtb', PageEncoding)


    
    MyDocTopo.ListerLesEntrees()
    MyDocTopo.ListerLesReseaux()
    MyDocTopo.ListerLesSecteurs()
    MyDocTopo.ListerLesCodes()
    MyDocTopo.ListerLesExpes()
    #MyDocTopo.ListerLesSeries()                                                   
    #MyDocTopo.ListerLesAntennes()
    AfficherMessage("----------------------------")
    MyCodeCalcul = TCodeCalcul('EWE', 'WU')
    MyBDDEntites = TTableDesEntites()
    MyCodeCalcul.SetDocTopo(MyDocTopo, MyBDDEntites)
    MyCodeCalcul.AjouterLesEntrees()
    MyCodeCalcul.RecenserJonctions()
    MyCodeCalcul.RecenserBranches()
    AfficherMessage("Noeud max: %d" % (MyCodeCalcul.GetMaxNode()))
    MyCodeCalcul.MakeRMatrix()
    MyCodeCalcul.MakeBMatrix()

    for i in range(1, 4):
        MyCodeCalcul.MakeSecondMembre(i)
        MyCodeCalcul.SolveMatrix(i)
    MyCodeCalcul.ListerNoeuds()
    MyCodeCalcul.RepartirEcarts()
    MyCodeCalcul.CalculContoursGaleries()
    MyCodeCalcul.TraiterViseesEnAntenne()
   
    # démarrer visu graphique
    MyBDDEntites.SetMinMax(20.00)
    #MyBDDEntites.ListerLesEntites()
    MyVisualisateur2D = TVisualisateur2D(super(), MyBDDEntites, 1000, 1000)
    MyVisualisateur2D.Flush()
#------------ Main()
Main()    
