import paho.mqtt.client as mqtt
import pouvoirs
import generation
from mcpi.minecraft import *
import time

mc = Minecraft.create()

broker="localhost"
port=1883
username="gantServer"
password="gantServer"

def on_connect(client,userdata,flags,rc):
    print("Connected whith the broker")
    client.subscribe("gantServer/#")
    client.subscribe("gantClient/#")
    
def on_message(client,userdata,msg):
    payload=msg.payload.decode()
    print(f"Received from {msg.topic}:{payload}")
    
    match msg.topic:
        case "gantServer/index":
            joueur1.cassage()
        case "gantServer/majeur":
            joueur2.slow()
        case "gantServer/annulaire":
            joueur2.mur(2)
        case "gantServer/auriculaire":
            joueur2.eau()
        case "gantClient/index":
            joueur2.cassage()
        case "gantClient/majeur":
            joueur1.slow()
        case "gantClient/annulaire":
            joueur1.mur(2)
        case "gantClient/auriculaire":
            joueur1.eau()
        
        
client=mqtt.Client()
client.username_pw_set(username,password)
client.on_connect=on_connect
client.on_message=on_message

joueurs=mc.getPlayerEntityIds()
joueur1=pouvoirs.Joueur(joueurs[0])
joueur2=pouvoirs.Joueur(joueurs[1])

client.connect(broker,1883,60)
client.loop_start()
generation.gen()
        
