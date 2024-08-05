import discord
from discord.ext import commands
import os 
from dotenv import load_dotenv
import asyncio
import traceback
import sys
#load the env file
load_dotenv()
#Loading our token
token = os.getenv('discord_Token')
bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@bot.event 

#error handling
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found. Try again!")
    else:
        await ctx.send(f"An error occurred: {str(error)}")
        traceback.print_exc()

async def on_ready():
    print("Bot ready!")
#making the bot say hello in different variations
@bot.command(aliases=["hi","wassup","yo","hey"])
async def hello(ctx):
    await ctx.send(f"hello there!, {ctx.author.mention}!")
#Making the bot say goodmorning in different variations
@bot.command(aliases=["morning","gm",])
async def goodmorning(ctx):
    await ctx.send(f"Good morning, {ctx.author.mention}!")

bot.run(token)
