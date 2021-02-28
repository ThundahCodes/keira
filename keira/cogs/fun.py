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


class fun(commands.Cog):
    def __init__(self, bot):
        self.client = bot




    @commands.command()
    async def slap(self, ctx, user: discord.Member):
        gifs = ["https://media1.tenor.com/images/b6d8a83eb652a30b95e87cf96a21e007/tenor.gif?itemid=10426943",
           "https://media1.tenor.com/images/e8f880b13c17d61810ac381b2f6a93c3/tenor.gif?itemid=17897236"]
        embed = discord.Embed(title="Slap",
                              description=f"Woa {ctx.author.mention} chill bro... You slapped {user.mention} so hard he/she is now in hospital...",
                              color=random.randint(0x000000, 0xFFFFFF))
        embed.set_image(url=f"{random.choice(gifs)}")
        if user == ctx.author:
            embed = discord.Embed(title="IMAGINE",
                                  description=f"{ctx.author.mention} You wont slap yourself hard enough come HERE!",
                                  color=random.randint(0x000000, 0xFFFFFF))
            embed.set_image(url=f"{random.choice(gifs)}")
        await ctx.send(embed=embed)
        

    @commands.command()
    async def hug(self, ctx, user: discord.Member):
        gifs = ["https://cdn.weeb.sh/images/H1ui__XDW.gif", "https://cdn.weeb.sh/images/B11CDkhqM.gif", "https://cdn.weeb.sh/images/rJv2H5adf.gif", "https://cdn.weeb.sh/images/SywetdQvZ.gif", "https://cdn.weeb.sh/images/BJCCd_7Pb.gif", "https://cdn.weeb.sh/images/Bk5haAocG.gif"]
        embed = discord.Embed(title="Hug", description=f"{ctx.author.mention} hugs {user.mention} ",
                              color=random.randint(0x000000, 0xFFFFFF))
        embed.set_image(url=f"{random.choice(gifs)}")
        if user == ctx.author:
            embed = discord.Embed(title="LONELY?",
                                  description=f"{ctx.author.mention} Why you hugging yourself come here lemme hug you!",
                                  color=random.randint(0x000000, 0xFFFFFF))
            embed.set_image(url=f"{random.choice(gifs)}")
        await ctx.send(embed=embed)





     
    @commands.command()
    async def kiss(self, ctx, user: discord.Member):
        gifs = ["https://giphy.com/embed/FqBTvSNjNzeZG"
"https://media.giphy.com/media/vaSA1fpCkY06I/giphy.gif "
"https://i.pinimg.com/originals/9c/be/bf/9cbebfb852e76c2b8d9c3b72ae08e68f.gif"
"https://www.icegif.com/wp-content/uploads/anime-kiss-icegif-2.gif"
"https://gfycat.com/boringsadibis"
"https://gfycat.com/hopefulfabulouskouprey"
"https://gfycat.com/uglydefenselessdiamondbackrattlesnake"
"https://i.imgur.com/WVSwvm6.gif"
"https://i.imgur.com/sZhtvBR.gif"
"https://i.imgur.com/q340AoA.gif"
"https://i.imgur.com/SeCRpPp.gif"
"https://i.imgur.com/LRPJt19.gif"
"https://i.imgur.com/6nCt4eb.gif"
"https://i.imgur.com/9758cJX.gif"
"https://i.imgur.com/Iu2j5Fh.gif"
"https://i.imgur.com/b3KBV8i.gif"
"https://i.imgur.com/AOpGwmX.gif"
"https://i.imgur.com/KAmjoLO.gif"
"https://i.imgur.com/2pZMgU7.gif"
"https://i.imgur.com/THyefKo.gif"
"https://i.imgur.com/QETjUCT.gif"
"https://i.imgur.com/fXh0i2H.gif"
"https://tenor.com/bbzm9.gif"
"https://cdn.myanimelist.net/s/common/uploaded_files/1483589430-f951b924a6fd5f59434ad3c63fc6960c.gif"
"https://cdn.myanimelist.net/s/common/uploaded_files/1450921081-24d8c4265c9f860d73293bce20ebd08f.jpeg"
"https://cdn.myanimelist.net/s/common/uploaded_files/1483588772-bde49b07ca18ca564d91efa7ac9703d7.gif"
"https://cdn.myanimelist.net/s/common/uploaded_files/1483589533-910174dfbbd5636c8fb4be5b117ecfd0.gif"
"https://cdn.myanimelist.net/s/common/uploaded_files/1483589602-6b6484adddd5d3e70b9eaaaccdf6867e.gif"
"https://cdn.myanimelist.net/s/common/uploaded_files/1483589646-9c8cd327454990f5da24af7d3f057627.gif"
"https://cdn.myanimelist.net/s/common/uploaded_files/1483589715-78566ff0e75a4c8f004df98d994561e4.gif"
"https://cdn.myanimelist.net/s/common/uploaded_files/1483589844-8d0395a7386d12026399620c087f4b97.gif"
"https://cdn.myanimelist.net/s/common/uploaded_files/1483589911-a8ffb9869c28bec5498777144571ade2.gif"
"https://cdn.myanimelist.net/s/common/uploaded_files/1483590013-b9d0df015159909c2fc2afe38651250f.gif"
"https://cdn.myanimelist.net/s/common/uploaded_files/1483590076-279c6e2645e2df2bbba1f76b80a70f06.gif"
"https://cdn.myanimelist.net/s/common/uploaded_files/1483590131-f84dd6ab7ec5369c6ec6a2c0eb70cb64.gif"
"https://cdn.myanimelist.net/s/common/uploaded_files/1483590257-0861880ab63699fae58af9c57e58d3b4.gif"
"https://tenor.com/view/anime-kiss-crying-cute-couple-gif-13970544"
"https://tenor.com/OJXy.gif"
"https://tenor.com/view/cute-kawai-kiss-anime-gif-16371489"
"https://tenor.com/2cNG.gif"
"https://tenor.com/Y683.gif"
"https://media.giphy.com/media/wOtkVwroA6yzK/giphy.gif"]
        embed = discord.Embed(title="Kiss", description=f"Woah {ctx.author.mention} stop kissing {user.mention} so passionately ...",
                              color=random.randint(0x000000, 0xFFFFFF))
        embed.set_image(url=f"{random.choice(gifs)}")
        if user == ctx.author:
            embed = discord.Embed(title="LONELY?",
                                  description=f"{ctx.author.mention} Why you kissing yourself come here lemme kiss you!",
                                  color=random.randint(0x000000, 0xFFFFFF))
            embed.set_image(url=f"{random.choice(gifs)}")
        await ctx.send(embed=embed)



    
    @commands.command()
    async def pat(self, ctx, user: discord.Member):
        gifs = ["https://i1.wp.com/gifimage.net/wp-content/uploads/2017/07/head-pat-gif-9.gif?fit=800,450", 
                 "https://media1.tenor.com/images/6ee188a109975a825f53e0dfa56d497d/tenor.gif?itemid=17747839"
                 "https://64.media.tumblr.com/cadf248febe96afdd6869b7a95600abb/tumblr_onjo4cGrZE1vhnny1o1_500.gifv"]
        embed = discord.Embed(title="pat", description=f"{ctx.author.mention} pats {user.mention}", color=random.randint(0x000000, 0xFFFFFF))
        embed.set_image(url=f"{random.choice(gifs)}")
        if user == ctx.author:
            embed = discord.Embed(title="LONELY?",
                                  description=f"{ctx.author.mention} Why you patting yourself come here lemme pat you!",
                                  color=random.randint(0x000000, 0xFFFFFF))
            embed.set_image(url=f"{random.choice(gifs)}")
        await ctx.send(embed=embed)    







    @commands.command()
    async def lick(self, ctx, user: discord.Member):
        gifs = ["https://images-ext-2.discordapp.net/external/AqmvPrnwsYvvxn5kgJH9Bd-J7mKkl3ka-jpVCwOiMyQ/https/cdn.weeb.sh/images/Sk15iVlOf.gif",
                "https://media1.tenor.com/images/6b701503b0e5ea725b0b3fdf6824d390/tenor.gif?itemid=12141727", "https://cdn.weeb.sh/images/ryGpGsnAZ.gif"]
        embed = discord.Embed(title="Lick", description=f"Woah {ctx.author.mention} stop licking {user.mention} like he/she is icecream ...",
                              color=discord.Color.blue())
        embed.set_image(url=f"{random.choice(gifs)}")
        if user == ctx.author:
            embed = discord.Embed(description=f"{ctx.author.mention} Licks himself. ||How do you even lick yourself?||",color=random.randint(0x000000, 0xFFFFFF))
            embed.set_image(url=f"{random.choice(gifs)}")
        await ctx.send(embed=embed)           





    @commands.command()
    async def kill(self, ctx, user: discord.Member):
        gifs = ["https://cdn.weeb.sh/images/r11as1tvZ.gif", "https://cdn.weeb.sh/images/BJO2j1Fv-.gif", ]
        embed = discord.Embed(title="kill", description=f" {ctx.author.mention} brutally kills {user.mention} oooof...", color=random.randint(0x000000, 0xFFFFFF))
        embed.set_image(url=f"{random.choice(gifs)}")
        if user == ctx.author:
            embed = discord.Embed(description=f"{ctx.author.mention} You dumb why you wanna kill yourslf. ||If your feeling sad you can always DM Crepco#3057 :pleading_face:||",
            color=random.randint(0x000000, 0xFFFFFF))
            embed.set_image(url=f"{random.choice(gifs)}")
        await ctx.send(embed=embed)         




    @commands.command(name='cry')
    async def cry(self, ctx, member:discord.Member=None): 
        gifs = ["https://media1.tenor.com/images/98466bf4ae57b70548f19863ca7ea2b4/tenor.gif?itemid=14682297", "https://media1.tenor.com/images/e69ebde3631408c200777ebe10f84367/tenor.gif?itemid=5081296", "https://media1.tenor.com/images/b88fa314f0f172832a5f41fce111f359/tenor.gif?itemid=13356071", "https://media1.tenor.com/images/26e7564bfb4408f9f7ff9518d4f87308/tenor.gif?itemid=8199739", "https://media1.tenor.com/images/ce52606293142a2bd11cda1d3f0dc12c/tenor.gif?itemid=5184314"]
        if member == None:
            embed = discord.Embed(title="cry", description=f"{ctx.author.mention} is crying. But why you crying ||If your feeling sad you can always DM Crepco#3057 :pleading_face:||", color=random.randint(0x000000, 0xFFFFFF))
            a = random.choice(gifs)
            embed.set_image(url=a)
        else:  
            embed = discord.Embed(title="cry", description=f"{ctx.author.mention} cries cause of  {member.mention}", color=random.randint(0x000000, 0xFFFFFF))
            embed.set_image(url=f"{random.choice(gifs)}")
        await ctx.send(embed=embed)
    
  







        
    
 




def setup(bot):
    bot.add_cog(fun(bot))
    print("fun cog is loaded")




