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
from alexa_reply import reply

intents = discord.Intents.default()
intents.members = True



client = commands.Bot(command_prefix = ">", intents=intents, help_command=None)


@client.event
async def on_ready():
    print('Bot is ready')
    change_status.start()


@tasks.loop(seconds=10)
async def change_status():
    status = ["under devolopment"]
    await client.change_presence(activity=discord.Game(choice(status)))








@client.command()
async def set(ctx, channel: discord.TextChannel = None, *, message: str = None):
    if not message or not channel:
        return await ctx.send('Give the params retard...')
    with open('welcomedata.json', 'r') as f:
        data = json.load(f)
    data[str(ctx.guild.id)] = {}
    data[str(ctx.guild.id)]['channel'] = channel.id
    data[str(ctx.guild.id)]['message'] = message
    with open('welcomedata.json', 'w') as f:
        json.dump(data, f, indent=4)
    await ctx.send('Set the bullshit up...')




@client.event
async def on_member_join(member, ):
    with open('welcomedata.json', 'r') as f:
        data = json.load(f)    
    if str(member.guild.id) not in data:
        return
    channel = client.get_channel(int(data[str(member.guild.id)]["channel"]))
    if not channel:
        return

    av = Image.open(io.BytesIO(await member.avatar_url_as(static_format='png', size=128).read())).convert('RGB')
    bg = Image.open('zZLkuPBh.jpg')
    av = av.resize((630, 630)) ## Resize the av to our wanted size
    large = (av.size[0] * 3, av.size[1] * 3) ## large is our image sized up by 3x
    mask = Image.new('L', large, 0)    ## Our mask were gonna use to get a transparent bg with our circle
    main = ImageDraw.Draw(mask)    ## Allows us to make the circle
    main.ellipse((0, 0) + large, fill=255)
    mask = mask.resize(av.size, Image.ANTIALIAS)    ## Changes our masks size to the same as the avatar
    av.putalpha(mask)    ## this makes the rest of the image transparent and thus we now have a circled av

    bg = bg.copy()    ## Just copies our background from the start
    bg.paste(av, (732, 57), av)    ## Pastes our avatar onto the background

    draw = ImageDraw.Draw(bg)
    font = ImageFont.truetype("Niceyear-7BjZV.otf", 150)
    big = ImageFont.truetype("Niceyear-7BjZV.otf", 200)     ## different sizes initiate 2 classes
    draw.text((710, 705), "Welcome", font=big, fill=(255,255,255,128))
    ## top messages
    try:
        draw.text((820, 855), member.name, font=font, fill=(255,255,255,255))
    except UnicodeEncodeError:
        draw.text((820, 855), "New User", font=font, fill=(255,255,255,255))
    ## unicode handling ^^^^
    
    bg.save('welcome.png')    ## And we save it
    await channel.send(file=discord.File("welcome.png"))



@client.command() ## change to bot pleaseeee
@commands.cooldown(1, 10, commands.BucketType.user)
async def ping(ctx):
    return await ctx.send(' {:.2f}ms'.format(client.latency * 1000))


@client.command()
async def test(ctx, member: discord.Member = None):
    member = member or ctx.author
    av = Image.open(io.BytesIO(await member.avatar_url_as(static_format='png', size=128).read())).convert('RGB')
    bg = Image.open('zZLkuPBh.jpg')
    av = av.resize((630, 630)) ## Resize the av to our wanted size
    large = (av.size[0] * 3, av.size[1] * 3) ## large is our image sized up by 3x
    mask = Image.new('L', large, 0)    ## Our mask were gonna use to get a transparent bg with our circle
    main = ImageDraw.Draw(mask)    ## Allows us to make the circle
    main.ellipse((0, 0) + large, fill=255)
    mask = mask.resize(av.size, Image.ANTIALIAS)    ## Changes our masks size to the same as the avatar
    av.putalpha(mask)    ## this makes the rest of the image transparent and thus we now have a circled av

    bg = bg.copy()    ## Just copies our background from the start
    bg.paste(av, (732, 57), av)    ## Pastes our avatar onto the background, i just did it dead in centre

    draw = ImageDraw.Draw(bg)
    font = ImageFont.truetype("Niceyear-7BjZV.otf", 150)
    big = ImageFont.truetype("Niceyear-7BjZV.otf", 200)     ## different sizes initiate 2 classes
    draw.text((710, 705), "Welcome", font=big, fill=(255,255,255,128))
    ## top messages
    try:
        draw.text((820, 855), member.name, font=font, fill=(255,255,255,255))
    except UnicodeEncodeError:
        draw.text((820, 855), "New User", font=font, fill=(255,255,255,255))
    ## unicode handling ^^^^
    
    bg.save('welcome.png')    ## And we save it
    await ctx.send(file=discord.File("welcome.png"), content=f"{member.mention}")






#chat bot useing bruh api 

@client.command(aliases = ['r'])
async def command(ctx, *, message):
    owner = "Crepco#3057"
    bot =  "Keira"
    message = message
    resp = reply(message, bot, owner)
    await ctx.send(await resp)
    
    



initial_extensions=[
            'cogs.fun',
]

if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)








client.run('no')





























