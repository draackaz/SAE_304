from mcpi.minecraft import *
import time
import math
import paho.mqtt.client as mqtt

mc = Minecraft.create()

class Joueur:
    def __init__(self,identifiant):
        self.id=identifiant #utilisé pour différencier les joueurs
    def cassage(self): #on casse les blocs autours du joueurs
        coordonnees=mc.entity.getTilePos(self.id)
        x,y,z=coordonnees.x,coordonnees.y,coordonnees.z
        
        mc.setBlocks(x-2,y,z-2,x+2,y+2,z+2,0)
        
        mc.setBlocks(-25,0,-25,25,0,25,45) #on replace le sol
        
        mc.setBlocks(-25,14,-25,25,14,25,89) #on replace le toit
        
        mc.setBlocks(-25,0,-25,-25,14,25,45) #on replace les murs
        mc.setBlocks(-25,0,-25,25,14,-25,45)
        mc.setBlocks(25,0,-25,25,14,25,45)
        mc.setBlocks(-25,0,25,25,14,25,45)
        
    def slow(self): #on place des toiles d'araignée sous le joueur
        coordonnees=mc.entity.getTilePos(self.id)
        x,y,z=coordonnees.x,coordonnees.y,coordonnees.z
        mc.setBlocks(x-1,y,z-1,x+1,y,z+1,30)
    def mur(self,taille): # on enferme le joueur
        coordonnees=mc.entity.getTilePos(self.id)
        x,y,z=coordonnees.x,coordonnees.y,coordonnees.z
        mc.setBlocks(x-taille,y,z-taille,x+taille,y+2,z-taille,45)
        mc.setBlocks(x-taille,y,z+taille,x+taille,y+2,z+taille,45)
        mc.setBlocks(x-taille,y,z-taille,x-taille,y+2,z+taille,45)
        mc.setBlocks(x+taille,y,z-taille,x+taille,y+2,z+taille,45)
        mc.setBlocks(x-taille,y-1,z-taille,x+taille,y-1,z+taille,45)
        mc.setBlocks(x-taille,y+2,z-taille,x+taille,y+2,z+taille,45)
    def eau(self):
        """if (self.cooldown==False):"""
        coordonnees=mc.entity.getTilePos(self.id)
        x,y,z=coordonnees.x,coordonnees.y,coordonnees.z
        mc.setBlock(x,y+2,z,8)
        """self.cooldown=True
        time.sleep(cooldown)
        self.cooldown=False"""
    """def paralysie(self):
        coordonnees=mc.entity.getTilePos(self.id)
        x,y,z=coordonnees.x,coordonnees.y,coordonnees.z
        
        debut = time.time()

        while time.time() - debut < 3:
            mc.entity.setTilePos(self.id, x, y, z)
            time.sleep(0.1)"""
    def distance(self,diamant_posx,diamant_posy,diamant_posz):
        coordonnees=mc.entity.getTilePos(self.id)
        x,y,z=coordonnees.x,coordonnees.y,coordonnees.z
        return math.sqrt((x-diamant_posx)**2+(y-diamant_posy)**2+(z-diamant_posz)**2)
"""mc.player.setTilePos(25,31,25)
joueur1.paralysie()"""  
