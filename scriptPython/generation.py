from random import *
from mcpi.minecraft import *
import pouvoirs
import time

def gen():
    mc=Minecraft.create()
    x=randint(1,24)
    y=1
    z=randint(1,24)

    mc.postToChat("Welcome to the game. The rules are simple. Your goal is to find a diamond before your opponent.")
    mc.postToChat("To help you, you have access to bonuses and maluses to inflict to your opponent.")
    mc.postToChat("You can only activate powers every 10 seconds.")
    mc.postToChat("To win the game, you need to right-click on top of the diamond block with your sword.")
    mc.postToChat("Good luck and have fun !")

    mc.events.clearAll()

    mc.setBlocks(-200,-64,-200,200,64,200,0)
    mc.setBlocks(-25,-1,-25,25,0,25,45)
    mc.setBlocks(-25,6,-25,25,6,25,89)
    mc.setBlocks(-25,0,-25,-25,5,25,45)
    mc.setBlocks(-25,0,-25,25,5,-25,45)
    mc.setBlocks(25,0,-25,25,5,25,45)
    mc.setBlocks(-25,0,25,25,5,25,45)
    mc.setBlock(x,y,z,57)
    
    mc.player.setTilePos(0,1,0)
    
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
        
        if (time.time()-temps>=15):
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
