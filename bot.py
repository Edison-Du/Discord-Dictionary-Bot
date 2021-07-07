from discord.ext import commands

bot = commands.Bot(command_prefix = "?")

bot.remove_command("help")
bot.load_extension(f"ready_cog")
bot.load_extension(f"dictionary_cog")

bot.run("BOT TOKEN HERE") 