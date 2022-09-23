import json
import sys
import os
from asyncio import events
import discord
from discord.ext import commands

import github_wrapper

USER_TOKEN = os.getenv('USER_TOKEN')

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
    notifications = json.loads(github_wrapper.getNotifications(USER_TOKEN))

    message = "\n".join(list(map(github_wrapper.generateNotificationMessage, notifications)))
    print(message[:2000])

    await ctx.send(f"{message[:2000]}")



client.run(
    'your token here')
