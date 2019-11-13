import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print("빅스비 활성화")
  game = discord.Game("빅스비 개발 중..")
  await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
  if message.content.startswith("hi"):
    await client.send_message(message.channel, "HI")
    
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
