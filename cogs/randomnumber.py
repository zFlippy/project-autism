import discord
from discord.ext import commands
import random




class randomnumbergen(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["rn", "randnumber", "randnum"])
    async def randomnumber(self, ctx, number1="1", number2="100"):
        i = int(number1)
        i2 = int(number2)
        ir = random.randint(i, i2)

        embed = discord.Embed(
            title="Random Number Generator",
            description=("You generated a random number between "+str(i)+" and "+str(i2)+", the random number is: **"+str(ir)+"**"),
            color=discord.Color.blue()
        )

        embed.set_footer(text="© PROJECT AUTISM 2021")

        await ctx.send(embed=embed)
        await ctx.message.delete()


def setup(client):
    client.add_cog(randomnumbergen(client))