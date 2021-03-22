# -*-coding:Latin-1 -*
import string
from tkinter import *
class TFenetreFille(Toplevel):
    def __init__(self, Parent, Titre = None):
        # associer la fen�te de dialogue et son conteneur
        Toplevel.__init__(self, Parent)
        self.protocol("WM_DELETE_WINDOW", self.OnClose)
        # le dialogue appara�t au dessus de son conteneur
        self.transient (Parent)
        #
        if (Titre):
            self.title(Titre) # title() est h�rit� de Toplevel
        # conteneur = fen�tre qui ouvre le Dialogue
        self.conteneur = Parent
        self.resultat = None
        # rendre la fen�tre modale
        self.grab_set()
        
    def ok (self, AEvent = None) :
        self.initial_focus.focus_set()
        # effacement avant de supprimer (pour le rendu)
        self.withdraw()
        # n�cessaire si dans apply() on utilise des �l�ments
        # qui doivent �tre visibles pour fournir des donn�es
        self.update_idletasks()
        self.apply()
        self.OnClose()
        
    def OnClose (self, AEvent = None) :
        self.conteneur.focus_set()
        self.destroy()
    def apply (self) :
        pass # m�thode qui doit �tre surcharg�e