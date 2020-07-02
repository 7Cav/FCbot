import subprocess
import sys
import config as cfg



def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])



install('discord.py')



import discord


def read_file(file_name):
	try:
		file = open(file_name, 'r')
		data = file.read()
		return data
	except:
		return file_name + " not found."


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.content.startswith('!'):
        	file_name = message.content.replace('!', '').lower() + '.txt'
        	data = read_file(file_name)
        	await message.channel.send(data)

try:
	client = MyClient()
	client.run(cfg.token)
except Exception as e:
	print(e)
	input()