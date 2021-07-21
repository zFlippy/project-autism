import asyncio
import os
import json
import requests

import discord
from discord.ext import commands

class Gato(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def gato(self, ctx):
        url = "https://cataas.com/cat?json=true"
        content = requests.get(url).content
        id = json.loads(content)["id"]

        embed = discord.Embed(
            title = "Random Gato Generator",
            color = discord.Color.green()
        )
        embed.set_image(url=f"https://cataas.com/cat/{id}")
        embed.set_footer(text="© PROJECT AUTISM 2021")

        await ctx.message.delete()
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Gato(client))