import discord
from discord.ext import commands, tasks

import random

class ReplyUser(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener(name="on_message")
    async def reply(self, ctx):

        # ignore message if author is a bot
        if ctx.author.bot: return
        # ignore message if in smiley channel
        if ctx.channel.id == 966231964375994378: return
        
        roll = random.randint(0, 100)

        if roll == 0:

            message_pool = [

                "hi",
                "hey",
                "what's up",
                f"hiiiiii buddy {ctx.author.mention}",
                "shut the fuck up",
                "dude guess what",
                "why would you say that",
                "can you elaborate on that",
                "fuck you",
                "dude i know this is unrelated but i need your help right now.",
                "no fucking way",
                "dry humps ur leg",
                "retard alert",
                "im gonna get you",
                "are u busy?",
                "lethal company?",
                "hop on",
                "vc?",
                "I Want You.",
                "mnngh",
                "...",
                "cease",
                "im gonna get you"

            ]

            msg = random.choice(message_pool)

            await ctx.reply(msg)


async def setup(bot):
    await bot.add_cog(ReplyUser(bot))