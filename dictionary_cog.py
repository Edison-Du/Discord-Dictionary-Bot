import discord
from discord.ext import commands
import requests

class Dictionary(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            title = "Dictionary Bot Usage",
            description = "?define [word] - Provides the definitions of a word\n" + 
                          "?synonyms [word] - Provides the synonyms of a word\n",
            colour = discord.Colour.green()
        )
        await ctx.send(embed = embed)

    @commands.command()
    async def define(self, ctx, word):
        await ctx.send(embed = self.getEmbedDefinition(word))

    @commands.command()
    async def synonyms(self, ctx, word):
        await ctx.send(embed = self.getEmbedSynonym(word))

    def getEmbedDefinition(self, word):
        request = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en_US/" + word)
        embed = discord.Embed()
        
        if (request.status_code == 200):
            request = request.json()[0]

            phonetics = "/" 
            for i in request["phonetics"]:
                phonetics += i["text"][1:-1] + ", "
            phonetics = phonetics[:-2] + "/"

            embed = discord.Embed(
                title = word[0].upper() + word[1:].lower() + " | Definitions",
                description = phonetics + "\n",
                colour= discord.Colour.blue()                
            )

            for i in request["meanings"]:
                definition = "⠀⠀" + i["definitions"][0]["definition"] + "\n"
                if ("example" in i["definitions"][0]):
                    definition += "⠀⠀_\"" + i["definitions"][0]["example"] + "_\""
                embed.add_field(
                    name = "_" + i["partOfSpeech"] + "_",
                    value = definition,
                    inline = False
                )
            
        elif (request.status_code == 404):
            embed = discord.Embed(
                title ="Error",
                description = "No definitions found for \"" + word + "\".",
                colour = discord.Colour.gold()
            )
            
        return embed  

    def getEmbedSynonym(self, word):
        request = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en_US/" + word)
        embed = discord.Embed()

        if (request.status_code == 200):
            request = request.json()[0]

            allSynonyms = ""
            for i in request["meanings"]:
                if ("synonyms" in i["definitions"][0]):
                    for synonym in i["definitions"][0]["synonyms"]:
                        allSynonyms += synonym[0].upper() + synonym[1:].lower() + "\n"
            
            embed = discord.Embed(
                title = word[0].upper() + word[1:].lower() + " | Synonyms",
                description = allSynonyms,
                colour= discord.Colour.orange()                
            )
            
        elif (request.status_code == 404):
            embed = discord.Embed(
                title ="Error",
                description = "No synonyms found for \"" + word + "\".",
                colour = discord.Colour.gold()
            )
            
        return embed

def setup(bot):
    bot.add_cog(Dictionary(bot))