from discord.ext.commands import Bot
from discord.ext import commands
from itertools import cycle
import discord
import random
import asyncio
import os
import time
import json




TOKEN = ""


BOT_PREFIX = (".")
client = Bot(command_prefix=BOT_PREFIX)
client.remove_command('help')

game = discord.Game("with Wierd.py")

#%%

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(status=discord.Status.do_not_disturb, activity=game)



@client.event
async def on_command_errorx(ctx, error):
    if isinstance(error, commands.CommandNotFound):                                                     #error checking
        await ctx.send("Invalid command used.")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):                                                     #error checking
        await ctx.send("Please pass in all required arguments.")

@client.command(aliases=("Help","helpu"))
async def help(ctx):
    await ctx.send("I serve only for my master:")
    await ctx.send("**spotify, twitter, reddit**")



######################################################################################################################################################################################################################################################
        
#%%


@client.command(name = "clear",
                description = "CLEARS THE CHAT DUMB ASS",
                brief ="clear's the chat",
                pass_context = True)
@commands.has_guild_permissions(administrator = True)
async def clear(ctx, amount : int):                                                                                 #permissions
    amount = amount + 1
    await ctx.channel.purge(limit=amount)



def is_it_me(ctx):
    return ctx.author.id == 459814977973256202

@client.command()                                                                                               #permissions (Only for chossen person)
@commands.check(is_it_me)
async def god(ctx):                                                                                             
    await ctx.send(f"That's me {ctx.message.author.mention}.")        
                                                                                                 




@client.command(aliases=("spotify","spotifyy"))
async def Spotify(ctx):
    await ctx.send("**My master's playlist:** https://open.spotify.com/playlist/6u37xhmXLiQFdXXzUF1Gu6?si=BMCo5BfHRz2D47rHvQ60jA")

@client.command(aliases=("Twitter","twittero"))
async def twitter(ctx):
    await ctx.send("**My master's Twitter account:** https://twitter.com/WierdPy")

@client.command(aliases=("Reddit","reddito"))
async def reddit(ctx):
    await ctx.send("**My master's Reddit account:** https://www.reddit.com/user/Nealmazerx")





@client.command(brief="spam")
@commands.has_guild_permissions(administrator = True)
async def spam(ctx, number,* ,word):
    if int(number) <= 25:
        for i in range(int(number)):
            await ctx.send(word)
            time.sleep(0.5)
    else:
        await ctx.send("You can spam max 25!")
    


@client.command()
@commands.has_guild_permissions(administrator = True)
async def ping(ctx):
    await ctx.send(f"Ping: {round(client.latency * 1000)}ms")
    

client.run(TOKEN)


