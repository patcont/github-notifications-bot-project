
import sys
import os
from asyncio import events
from discord.ext import commands


# commands for the bot in the discord server
client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print('bot online')


@client.command()
async def actualizar(ctx):
    await ctx.send("Datos actualizados :blush:")
    # this code below allows the bot to restart itself after the command, might be useful in the future but in the meantime is not

    # os.execv(sys.executable, ['python'] + sys.argv)


client.run('YOUR TOKEN HERE')