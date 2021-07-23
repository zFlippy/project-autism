import asyncio
import os
import json

from datetime import datetime

import discord
from discord.ext import commands

class Userinfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["uinfo", "user"])
    async def userinfo(self, ctx, member:discord.Member=None):
        if member == None:
            embed = discord.Embed(
                title = "Error",
                description = "You must mention a user",
                color = discord.Color.red()
            )

            await ctx.message.delete()
            await ctx.send(embed=embed)

        else:
            info = [
                member.name,
                member.id,
                member.bot,
                member.created_at.strftime('%d-%m-%Y, %H:%M:%S'),
                member.joined_at.strftime('%d-%m-%Y, %H:%M:%S')
            ]
            desc = f"""
Name: {info[0]}
ID: {info[1]}
Bot: {info[2]}
Created at: {info[3]}
Joined at: {info[4]}
            """
            embed = discord.Embed(
                title = f"User Info: {member}",
                description = desc,
                color = discord.Color.green()
            )         

            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(text="© PROJECT AUTISM 2021")

            await ctx.message.delete()
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Userinfo(client))