import discord
from discord.ext import commands

class nword(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["nwordcount", "nwordcounter"])
    async def nword(self, ctx):
        acounter, rcounter, wcounter = 0
        
        async for message in ctx.channel.history(limit=1000):
            if message.author == message.author:
                if "nigger" in str(message.content):
                    rcounter += 1
                    wcounter +=1
                    
                if "nigga" in str(message.content):
                    acounter += 1
                    wcounter += 1
                    
        embed = discord.Embed(
            title="NWord Counter",
            description=("I said the NWord "+(str(wcounter))+" times in the last 1000 messages, of which "+(str(acounter))+" ended with an 'a' and "+(str(rcounter))+" ended with the hard r"),
            color=discord.Color.green()
        )

        embed.set_footer(text="© PROJECT AUTISM 2021")

        await ctx.message.delete()
        await ctx.send(embed=embed)

        
def setup(client):
    client.add_cog(nword(client))
