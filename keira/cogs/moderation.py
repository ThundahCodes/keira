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


class moderation(commands.Cog):
    def __init__(self, bot):
        self.client = bot



    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member, time, *, reason=None):
        guild = ctx.guild
        muted_role=discord.utils.get(ctx.guild.roles, name="Muted")
        if not muted_role:
               muted_role = await guild.create_role(name="Muted")
               for channel in guild.channels:
                   await channel.set_permissions(muted_role, speak=False, send_messages=False)     
        time_convert = {"s":1, "m":60, "h":3600,"d":86400}
        tempmute= int(time[0]) * time_convert[time[-1]]
        await member.add_roles(muted_role, reason=reason)
        embed = discord.Embed(description= f"✅ **{member.display_name} was muted for {reason}**", color=discord.Color.green())
        await ctx.send(embed=embed)
        await asyncio.sleep(tempmute)
        await member.remove_roles(muted_role) 


    @commands.command()
    async def unmute(self, ctx, member: discord.Member):
        await member.remove_roles(name="Muted")
        embed = discord.Embed(description="✅ **{member.display_name} was unmuted**", color=discord.Color.green())  
        await ctx.send(embed=embed)    
    


    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge (self, ctx, amount=None): 
    
      if amount == None:
        embed=discord.Embed(colour=discord.Colour.red())
        embed.add_field(name=":negative_squared_cross_mark: ERROR", value="Please provide the amount of messages you want to delete.")
        await ctx.send(embed=embed)
        return
      elif int(amount) <= 0:
        embed = discord.Embed(
        colour=discord.Colour.red())
        embed.add_field(name=":negative_squared_cross_mark: ERROR", value="Please provide a number more than 0.")
        await ctx.send(embed=embed)
        return
      else:
       await ctx.channel.purge(limit=int(amount) + 1)
       await ctx.send(f":correct~3: I have purged {amount} message(s).")
       await asyncio.sleep(2)
       await ctx.channel.purge(limit=1)



    @commands.command()
    @commands.has_permissions(administrator=True) 
    async def kick(self, ctx, member: discord.Member):
        await member.kick()
        await ctx.message.add_reaction("✅")  
        await ctx.send(f"{member.name} has been kicked by {ctx.author.name}!")



    

                

    
    













def setup(bot):    
      bot.add_cog(moderation(bot))
      print("moderation cog is loaded")