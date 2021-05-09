import discord
import os
import sys
from discord.ext import commands

class slime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello!")

    @commands.command()
    async def shutdown(self, ctx):
        await self.bot.close()

    @commands.Cog.listener()
    async def on_connect(self):
        print("Bot is online")

def setup(bot):
    bot.add_cog(slime(bot))
