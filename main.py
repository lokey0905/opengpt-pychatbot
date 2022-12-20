import discord
import openai
import asyncio
from pyChatGPT import ChatGPT
import random

from config import config

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
channel = []

@client.event
async def on_ready():
    print('Login As：', client.user)
    game = discord.Game('Test with OpenAI by lokey')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    if message.content == "hi" or message.content == "HI":
        await message.channel.send('Hi')

    elif message.content == "/start":
      find=0
      for i in range(len(channel)):
        if message.channel.id == channel[i]:
          find=1
      if find!=1:
        channel.append(message.channel.id)
        await message.channel.send('開始對話')

    elif message.content == "/end":
      find=0
      for i in range(len(channel)):
        if message.channel.id == channel[i]:
          find=1
      if find==1:
        channel.remove(message.channel.id)
        await message.channel.send('結束對話')

    elif message.content.startswith('!'):
      tmp = message.content.split(" ",2)
      if len(tmp) == 1:
        await message.channel.send("!")
      else:
        await message.channel.send(tmp[1])

    elif message.content.startswith('?'):
      tmp = message.content.split(" ",2)
      if len(tmp) == 1:
        await message.channel.send("?")
      else:
        await message.channel.send("???")

    else:
      find=0
      for i in range(len(channel)):
        if message.channel.id == channel[i]:
          find=1
      if find==1:
        resp = api1.send_message(message.content)
        txt = resp['message']
        print(txt)
        txt = [txt[i: i + 2000] for i in range(0, len(txt), 2000)]
        for i in range(len(txt)):
          await message.channel.send(txt[i])
          

api1 = ChatGPT(config.session_token)
client.run(config.TOKEN,reconnect=True)
