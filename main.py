import discord
import os 
import requests
import json
import random
from replit import db
from keepAlive import keep_alive

client = discord.Client()


'''******  *****'''
if "responding" not in db.keys():
  db["responding"] = True

'''******** Update/Delete Builds *********'''
def update_builds (builds_message):
  if "builds" in db.keys():
    builds = db["builds"]
    builds.append(builds_message)
    db["builds"] = builds
  else:
    db["builds"] = [builds_message]

def delete_builds(index):
  builds = db["builds"]
  if len(builds) > index:
    del builds[index]
  db["builds"] = builds


'''******* El bot funciona *****'''
@client.event
async def on_ready():
  print ('El bot esta funcioanndo {0.user}'.format(client))

'''***** Respondiendo mensaje  ****'''
@client.event
async def on_message(message):
  if message.author == client.user:
    return 
  msg = message.content

  if db["responding"]: 
#Update/delete Builds wh db
    options = starter_builds
    if "builds" in db.keys():
      options.extend(db["builds"])
#Random Respuest
    if any(word in msg for word in buildsZvZ):
      await message.channel.send(random.choice(options))

#New respuesta. 
  if msg.startswith("$new"):
    builds_message = msg.split("$new ", 1)[1] 
    update_builds(builds_message)
    await message.channel.send("La Build fue agregada.")

#Borrar 
  if msg.startswith("$del"):
    builds = []
    if "builds" in db.keys():
      index = int(msg.split("$del", 1)[1])
      delete_builds(index)
      builds = db["builds"]
    await message.channel.send(builds)
  
  if msg.startswith("$list"):
    builds = []
    if "builds" in db.keys():
      builds = db["builds"]
    await message.channel.send(builds)

  '''if msg.startswith("$responding"):
    value = msg.split("$responding",1)[1]

    if value.lower() == "True":
      db["responding"] == True
      await message.channel.send("responding is on")
    else:
      db["responding"] == False
      await message.channel.send("responding is off")'''
  
  if msg.startswith("$keys"):
    keys = db.keys()
    print ("*************Estas son las llaves\n" , keys)
  
  if msg.startswith("$delete"):
     del db["key"]


#!!! MAntener vivo el bot
keep_alive()
#!!! Token
client.run(os.getenv('TOKEN'))
