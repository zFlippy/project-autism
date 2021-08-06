import asyncio
import json
import os
import requests

import discord
from discord.ext import commands

class Ratio(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ratio(self, ctx, *, msg):
        await ctx.message.delete()

        ratio_msg = await ctx.send(msg)

        await ratio_msg.add_reaction("👍")
        await ratio_msg.add_reaction("🔁")
        await ratio_msg.add_reaction("💬")
def setup(client):
    client.add_cog(Ratio(client))