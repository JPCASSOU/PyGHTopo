# -*-coding:Latin-1 -*
import string

from math import *
from functions import *
from types_donnees import *

class TPalette256:
    def __init__(self):
        self.FColorArray = [] #[0 for i in range(0, 256)]
        self.GenererToporobotPalette()
    # Couleurs MAC vers couleurs PC
    def GetPCColor(self, MR, MG, MB):
        R = MR / 256
        G = MG / 256
        B = MG / 256
        return rgb(R, G, B)
    #------------------------------------
    def AddCouleurByMacRGB(self, R, G, B):
        EWE = self.GetPCColor(R, G, B)
        self.FColorArray.append(EWE) 
    #------------------------------------
    def GetCouleurByIndex(self, Idx):
        try:
            if (Idx > 255):
                Idx = 0
            return self.FColorArray[Idx]
        except:
            return self.FColorArray[0]
    #------------------------------------
    def GenererToporobotPalette(self):
        M13107 = 13107
        M4369  = 4369;
        # on génère en dur une palette de 256 couleurs
        self.AddCouleurByMacRGB(65535, 65535, 65535)
        self.AddCouleurByMacRGB(0, 0, 0)
        self.AddCouleurByMacRGB(30583, 30583, 30583)
        self.AddCouleurByMacRGB(21845, 21845, 21845)
        self.AddCouleurByMacRGB(65535, 65535, 0)
        self.AddCouleurByMacRGB(65535, 26214, 0)
        self.AddCouleurByMacRGB(56797, 0, 0)
        self.AddCouleurByMacRGB(65535, 0, 39321)
        self.AddCouleurByMacRGB(26214, 0, 39321)
        self.AddCouleurByMacRGB(0, 0, 56797)
        self.AddCouleurByMacRGB(0, 39321, 65535)
        self.AddCouleurByMacRGB(0, 61166, 0)
        self.AddCouleurByMacRGB(0, 26214, 0)
        for i in range(1, 3): 
            self.AddCouleurByMacRGB(M13107*(i+1), M13107 * i, M13107 * (i-1))
        self.AddCouleurByMacRGB(48059, 48059, 48059)
        for i in range(16, 20):
            self.AddCouleurByMacRGB(5*M13107, 5 * M13107, M13107 * (20-i))
        for i in range(4, 2, -1): # for i = 4 downto 2 do
            for j in range(5, 0, -1): # for j = 5 downto 0 do begin
                self.AddCouleurByMacRGB(5*M13107, i*M13107, j*M13107)
        for i in range(5, 0, -1): #for i = 5 downto 0 do begin
            self.AddCouleurByMacRGB(5*M13107, M13107, i*13107)
        for i in range(5, 4, -1): #for i = 5 downto 4 do begin
            self.AddCouleurByMacRGB(5*M13107,0, i*13107)
        for i in range(2, 0, -1): # for i = 2 downto 0 do begin
            self.AddCouleurByMacRGB(5*M13107,0, i*13107)
        for j in range(2, 0, -1): # for j = 5 downto 0 do
            for k in range(5, 0, -1): # for k = 5 downto 0 do begin
                self.AddCouleurByMacRGB(4*M13107,j*M13107, k*M13107)
        for j in range(5, 3, -1): # for j = 5 downto 3 do
            for k in range(5, 0, -1): # for k = 5 downto 0 do begin
                self.AddCouleurByMacRGB(3*M13107,j*M13107, k*M13107)
        for k in range(5, 2, -1): # for k = 5 downto 2 do begin
            self.AddCouleurByMacRGB(3*M13107,2*M13107, k*M13107)
        self.AddCouleurByMacRGB(3*M13107,2*M13107, 0)
        for j in range(1, 0, -1): # for j = 1 downto 0 do
            for i in range(5, 0, -1): # for k = 5 downto 0 do begin
                self.AddCouleurByMacRGB(3*M13107,j*M13107, k*M13107)
        for j in range(5, 1, -1): # for j = 5 downto 1 do
            for k in range(5, 0, -1): # for k = 5 downto 0 do begin
                self.AddCouleurByMacRGB(2*M13107,j*M13107, k*M13107)
        for i in range(5, 4, -1): # for k = 5 downto 4 do begin
            self.AddCouleurByMacRGB(2*M13107,0, k*M13107)
        for k in range(2, 0, -1): # for k = 2 downto 0 do begin
            self.AddCouleurByMacRGB(2*M13107,0, k*M13107)
        for j in range(5, 0, -1): # for j = 5 downto 0 do
            for k in range(5, 0, -1): # for k = 5 downto 0 do begin
                self.AddCouleurByMacRGB(M13107,j*M13107, k*M13107)
        for j in range(5, 4, -1): # for j = 5 downto 4 do
            for k in range(5,  0, -1): # for k = 5 downto 0 do begin
                self.AddCouleurByMacRGB(0,j*M13107, k*M13107)
        for k in range(4, 0, -1): # for k = 4 downto 0 do begin
            self.AddCouleurByMacRGB(0, 3*M13107, k*M13107)
        for k in range(5, 1, -1): # for k = 5 downto 1 do begin
            self.AddCouleurByMacRGB(0, 2*M13107, k*M13107)
        for i in range(5, 0, -1): # for k = 5 downto 0 do begin
            self.AddCouleurByMacRGB(0, M13107, k*M13107)
        for i in range(5, 1, -1): # for k = 5 downto 1 do begin
            self.AddCouleurByMacRGB(0, 0, k*M13107)
        self.AddCouleurByMacRGB(61166, 0, 0)
        self.AddCouleurByMacRGB(48059, 0, 0)
        r = 0;
        for i in range(1, 7, 1): # for i = 1 to 7 do begin
            r += IIF((i % 2 != 0), M4369, 2*M4369)
            self.AddCouleurByMacRGB(48059 - r, 0, 0)
        self.AddCouleurByMacRGB(0, 56797, 0)
        self.AddCouleurByMacRGB(0, 48059, 0)
        r = 0;
        for i in range(1, 7, 1): # for j = 1 to 7 do begin
            r += IIF(((j % 2) != 0), M4369, 2*M4369)
            self.AddCouleurByMacRGB(0, 48059 - r, 0)
        self.AddCouleurByMacRGB(0, 0, 61166)
        self.AddCouleurByMacRGB(0, 0, 48059)
        r = 0;
        for i in range(1, 7, 1): # for j = 1 to 7 do begin            
            r += IIF((j % 2 != 0), M4369, 2*M4369)
            self.AddCouleurByMacRGB(0, 0,48059 - r)
        r = 61166
        self.AddCouleurByMacRGB(r,r,r)
        r = 56797
        self.AddCouleurByMacRGB(r,r,r)
        r = 43690
        self.AddCouleurByMacRGB(r,r,r)
        r = 34952
        self.AddCouleurByMacRGB(r,r,r)
        for i in range(1, 3, 1): # for i = 1 to 3 do begin
            r = r // 2;
            self.AddCouleurByMacRGB(r,r,r)
    #------------------------------------
    #------------------------------------
    #------------------------------------
    #------------------------------------
    #------------------------------------
    #------------------------------------
    #------------------------------------
    