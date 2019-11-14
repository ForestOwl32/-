import discord
import asyncio
import os

client = discord.Client()

@client.event
async def on_ready():
  print("빅스비 활성화")
  game = discord.Game("\"빅스비 도움\" 입력 ㄱㄱ")
  await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
  if message.content.startswith("하이 빅스비"):
    await message.channel.send("안녕하세요!")
    
  if message.content.startswith("빅스비"):
    await message.channel.send("네, 플레이어님")
    
  if message.conetnt.startswith("빅스비 바보"):
    await message.channel.send("플레이어님이 더 바보")
    
  if message.content.startswith("빅스비 모두불러줘"):
    await message.channel.send("@everyone")
    
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
