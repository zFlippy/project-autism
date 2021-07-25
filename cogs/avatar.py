import asyncio
import json
import os
import requests

import discord
from discord.ext import commands

class Avatar(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["av", "pfp"])
    async def avatar(self, ctx, member:discord.Member=None):
        await ctx.message.delete()

        if member == None:
            url = ctx.author.avatar_url
            namefull = ctx.author
        else:
            try:
                url = member.avatar_url
                namefull = member
            except Exception as ex:
                embed = discord.Embed(
                    title = "Error",
                    description = ex,
                    color = discord.Color.red()
                )

                await ctx.send(embed=embed)
        
        embed = discord.Embed(
            title = f"Avatar of {namefull}",
            color = discord.Color.green()
        )

        embed.set_image(url=url)

        await ctx.send(embed=embed)
def setup(client):
    client.add_cog(Avatar(client))
