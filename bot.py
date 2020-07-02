import discord
import requests
import subprocess
import sys
import config as cfg


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


install('discord.py')
url = 'https://raw.githubusercontent.com/7Cav/FCbot/master/info.txt'


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.content.startswith('!'):
            raw = requests.get(url)
            data = raw.text
            await message.channel.send(data)


try:
    client = MyClient()
    client.run(cfg.token)
except Exception as e:
    print(e)
    input()
