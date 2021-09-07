import discord
import os 

cliente = discord.Client()

@cliente.event
async def on_ready():
  print ('El bot esta funcioanndo {0.user}'.format(cliente))

@cliente.event
async def on_message(message):
  if message.authro == cliente.user:
    return 
  
  if message.Content.startwith('$hello'):
    await message.chand("Holanda")

cliente.run(os.getenv('TOKEN'))