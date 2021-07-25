import asyncio
import os
import json
import requests

import discord
from discord.ext import commands

class Nuker(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def nuke(self, ctx, *args):
        await ctx.message.delete()
        # https://discordpy.readthedocs.io/en/latest/api.html#discord.Member.guild_permissions guild perms
        # TODO: make the command lelelelelel


def setup(client):
    client.add_cog(Nuker(client))