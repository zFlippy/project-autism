import asyncio
import os
import json

import discord
from discord.ext import commands

os.system('cls && mode 40,10 && title PROJECT AUTISM')

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="--", intents=intents, self_bot=True)
client.remove_command("help")

@client.event
async def on_ready():
    os.system("cls")
    print(f"PROJECT AUTISM\nLogged in as: {client.user.name}#{client.user.discriminator}")

@client.command()
async def ping(ctx):
    embed = discord.Embed(
        title = "Ping",
        description = f"{round(client.latency*1000)}ms",
        color = discord.Color.green()
    )
    embed.set_footer(text="© PROJECT AUTISM 2021")
    
    await ctx.message.delete()
    await ctx.send(embed=embed)


with open("config.json") as f:
    config = json.load(f)

for file in os.listdir("./cogs"):
    split = os.path.splitext(file)
    if split[1] == ".py":
        cog = f"cogs.{split[0]}"
        client.load_extension(cog)
        print(f"Loaded: {cog}")

client.run(config["token"], bot=False)
