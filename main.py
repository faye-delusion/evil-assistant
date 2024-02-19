import discord
from discord.ext import commands

import json
import os

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix=">", intents=intents)

@bot.event
async def on_ready():
    for file in os.listdir("./modules"):
        if file.endswith(".py"):
            try:
                await bot.load_extension(f"modules.{file[:-3]}")
            except commands.ExtensionAlreadyLoaded:
                print(f"{file} already loaded")
            except commands.ExtensionFailed as E:
                print(f"{file} threw exception:\n{E}")
            else:
                print(f"loaded {file}")

    try:
        
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands\n{[synced[i] for i in range(0,len(synced))]}")

    except Exception as e:

        print(e)


@bot.command()
async def ping(ctx):
    await ctx.reply("pong")

@bot.command()
@commands.is_owner()
async def load(ctx, module):

    try:

        await bot.load_extension(f"modules.{module}")

    except Exception as E:

        await ctx.reply("uh oh!\n{}".format(E))

    else:

        await ctx.reply(":)")

@bot.command()
@commands.is_owner()
async def reload(ctx, module):

    try:

        await bot.reload_extension(f"modules.{module}")

    except Exception as E:

        await ctx.reply("uh oh!\n{}".format(E))

    else:

        await ctx.reply(":)")

token = ""
with open("config.json", "r") as f:
    token = json.load(f)["API_KEY"]

bot.run(token)