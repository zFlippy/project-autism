import asyncio
import json
import os
import requests

import discord
from discord.ext import commands

class Doggo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def doggo(self, ctx):
        url = "https://dog.ceo/api/breeds/image/random"
        content = requests.get(url).content

        _json = json.loads(content)

        embed = discord.Embed(
            title = "Random Doggo Generator",
            color = discord.Color.green()
        )
        embed.set_image(url=_json["message"])
        embed.set_footer(text="© PROJECT AUTISM 2021")

        await ctx.message.delete()
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Doggo(client))