import discord
from PIL import Image
from io import BytesIO
from discord.ext import commands
import youtube_dl
import datetime
import json
import random
import aiohttp
import asyncio
from random import choice
from discord.ext import tasks
import os
import psutil
import cogs
import traceback
import sys
from PIL import ImageDraw
from PIL import ImageFont
import io


intents = discord.Intents.default()
intents.members = True



client = commands.Bot(command_prefix = ">", intents=intents, help_command=None)


@client.event
async def on_ready():
    print('Bot is ready')
    change_status.start()


@tasks.loop(seconds=10)
async def change_status():
    status = ["test"]
    await client.change_presence(activity=discord.Game(choice(status)))


@client.command(aliases = ['chatbot'])
async def cb(ctx, *, phrase):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://bruhapi.xyz/cb/{phrase}") as response2:
            resp = await response2.json()
            await ctx.send(resp["res"])





client.run('ODA0MjYxNzMwNTc3Njc4MzY2.YBJxGw.WZVkTw6mR7Xa86BaZRabtmQzWYk')