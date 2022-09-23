
import sys
import os
from asyncio import events
import discord
from discord.ext import commands

# since discord version 2.0 this code below is necesary to run the bot DO NOT ERASE
intents = discord.Intents.default()
intents.message_content = True

# commands for the bot in the discord server
client = commands.Bot(command_prefix=".", intents=intents)


@client.event
async def on_ready():
    print('bot online')


@client.command()
async def actualizar(ctx):
    await ctx.send("Datos actualizados :blush:")
    # this code below allows the bot to restart itself after the command, might be useful in the future but in the meantime is not

    # os.execv(sys.executable, ['python'] + sys.argv)

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

client.run(DISCORD_TOKEN)
