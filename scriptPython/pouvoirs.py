from mcpi.minecraft import *
import time
import math
import paho.mqtt.client as mqtt

mc = Minecraft.create()

class Joueur:
    def __init__(self,identifiant):
        self.id=identifiant
    def cassage(self):
        coordonnees=mc.entity.getTilePos(self.id)
        x,y,z=coordonnees.x,coordonnees.y,coordonnees.z
        mc.setBlocks(x-2,y,z-2,x+2,y+2,z+2,0)
        mc.setBlocks(-25,0,-25,-25,5,25,45)
        mc.setBlocks(-25,0,-25,25,5,-25,45)
        mc.setBlocks(25,0,-25,25,5,25,45)
        mc.setBlocks(-25,6,25,25,6,25,89)
    def slow(self):
        coordonnees=mc.entity.getTilePos(self.id)
        x,y,z=coordonnees.x,coordonnees.y,coordonnees.z
        mc.setBlocks(x-1,y,z-1,x+1,y,z+1,30)
    def mur(self,taille):
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