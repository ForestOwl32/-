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
  if message.content.startswith("하이 빅스비"):
    await message.channel.send("안녕하세요!")
  if message.content.startswith("빅스비"):
    await message.channel.send("네, 플레이어님")
    
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
