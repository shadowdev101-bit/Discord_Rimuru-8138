import os
import discord
from discord.ext import commands

from myserver import server_on

class Client(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('สวัสดี'):
            await message.channel.send(f'สวัสดีค่ะ @{message.author}')

        if message.content.startswith('!rimuru_dl ActionsStuff'):
            await message.channel.send(f'# ตอบกลับ {message.author} [ดาวโหลด](https://www.mediafire.com/file/1pe2xxasyrps3rh/Actions+Stuff+1.8+By+Asuki+(resources)+61c7a786-d7ad-49e0-a710-817121cd9795.mcpack/file)')



 #

intents = discord.Intents.default()
intents.message_content = True

server_on()

client = Client(intents=intents)
client.run(os.getenv('TOKEN'))