# -*-coding:Latin-1 -*
import string
from tkinter import *
class TFenetreFille(Toplevel):
    def __init__(self, Parent, Titre = None):
        # associer la fenête de dialogue et son conteneur
        Toplevel.__init__(self, Parent)
        self.protocol("WM_DELETE_WINDOW", self.OnClose)
        # le dialogue apparaît au dessus de son conteneur
        self.transient (Parent)
        #
        if (Titre):
            self.title(Titre) # title() est hérité de Toplevel
        # conteneur = fenêtre qui ouvre le Dialogue
        self.conteneur = Parent
        self.resultat = None
        # rendre la fenêtre modale
        self.grab_set()
        
    def ok (self, AEvent = None) :
        self.initial_focus.focus_set()
        # effacement avant de supprimer (pour le rendu)
        self.withdraw()
        # nécessaire si dans apply() on utilise des éléments
        # qui doivent être visibles pour fournir des données
        self.update_idletasks()
        self.apply()
        self.OnClose()
        
    def OnClose (self, AEvent = None) :
        self.conteneur.focus_set()
        self.destroy()
    def apply (self) :
        pass # méthode qui doit être surchargée