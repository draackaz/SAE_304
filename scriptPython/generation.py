from random import *
from mcpi.minecraft import *
import pouvoirs
import time

def gen():
    mc=Minecraft.create()
    x=randint(-20,20)
    y=randint(0,11)
    z=randint(-20,20)

    mc.postToChat("Welcome to the game. The rules are simple. Your goal is to find a diamond before your opponent.")
    mc.postToChat("To help you, you have access to bonuses and maluses to inflict to your opponent.")
    mc.postToChat("You can only activate powers every 5 seconds.")
    mc.postToChat("To win the game, you need to stand on top of the diamond block.")
    mc.postToChat("Good luck and have fun !")

    mc.events.clearAll()

    mc.setBlocks(-1000,-64,-1000,1000,64,1000,0) #nettoie la carte
    
    mc.setBlocks(-25,0,-25,25,0,25,45) #sol du rez de chaussee
    
    mc.setBlocks(-25,14,-25,25,14,25,89) #toit en glowstone
    
    mc.setBlocks(-25,0,-25,-25,14,25,45) #murs
    mc.setBlocks(-25,0,-25,25,14,-25,45)
    mc.setBlocks(25,0,-25,25,14,25,45)
    mc.setBlocks(-25,0,25,25,14,25,45)
    
    mc.setBlocks(-22,4,-22,22,4,22,89) #deuxieme etage
    mc.setBlocks(-22,5,-22,22,5,22,45)
    
    mc.setBlocks(-20,9,-20,20,9,20,89) #troisieme etage
    mc.setBlocks(-20,10,-20,20,10,20,45)
    
    mc.setBlock(x,y,z,57) #bloc de diamant
    
    #mc.player.setTilePos(0,1,0)
    
    diamant_pos=(x,y,z)
    victoire_pos=(x,y+1,z)
    
    temps=time.time()
    
    while True:
        if mc.getBlock(*diamant_pos) != 57:
            mc.setBlock(*diamant_pos, 57)
        """hits=mc.events.pollBlockHits()
        for hit in hits :
            if (hit.pos.x==x and hit.pos.y==y and hit.pos.z==z):
                mc.postToChat("Victoire")
                exit()
        time.sleep(0.1)"""
        
        if (time.time()-temps>=10):
            for player in mc.getPlayerEntityIds():
                mc.postToChat("Player "+str(mc.getPlayerEntityIds().index(player)+1)+" is "+str(round(pouvoirs.Joueur(player).distance(*diamant_pos),2))+" blocks away from the diamond")
            temps=time.time()
            
        for player in mc.getPlayerEntityIds():
            position=mc.entity.getTilePos(player)
            if (position.x==x and position.y==y+1 and position.z==z):
                print(player)
                if (player==mc.getPlayerEntityIds()[0]):
                    mc.postToChat("Player 1 wins !")
                else :
                    mc.postToChat("Player 2 wins !")
                exit()
