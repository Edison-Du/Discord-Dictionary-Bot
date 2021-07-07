import discord
from discord.ext import commands

class Ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_connect(self):
        print("Bot is online.")

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        print("Bot is shutting down.")
        await self.bot.close()

    @shutdown.error
    async def shutdown_error(self, ctx, error):
        if isinstance(error, (commands.CommandError)):
            embed = discord.Embed(
                title ="Error",
                description = "You do not have permission to use this command.",
                colour = discord.Colour.gold()
            )
            await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Ready(bot))