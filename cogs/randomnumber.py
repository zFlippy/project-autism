import discord
from discord.ext import commands
import random

class randomnumber(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["rng", "randnumber", "randnum"])
    async def randomnumber(self, ctx, number1="1", number2="100"):
        try:
            i = int(number1)
            i2 = int(number2)
            ir = random.randint(i, i2)

        except Exception as ex:
            embed = discord.Embed(
                title = "Error",
                description = ex,
                color = discord.Color.red()
            )

            await ctx.message.delete()
            await ctx.send(embed=embed)
            return

        embed = discord.Embed(
            title = "Random Number Generator",
            description = f"Generated **{ir}** ({i}-{i2})",
            color=discord.Color.green()
        )

        embed.set_footer(text="© PROJECT AUTISM 2021")

        await ctx.send(embed=embed)
        await ctx.message.delete()

def setup(client):
    client.add_cog(randomnumber(client))
