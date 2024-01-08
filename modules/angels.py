import discord
from discord.ext import tasks, commands

import json
import datetime
import re

class AngelCounter(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.guild_id = 817475690499670066
        self.global_kills_channel = 862279824461529098
        self.global_leader_channel = 862647658271473664
        self.daily_kills_channel = 880598351224143892
        self.daily_leader_channel = 1192440063133487154

    def cog_load(self):
        self.update_global_counter.start()
        self.update_daily_counter.start()
        self.refresh_file.start()

    def cog_unload(self):
        self.update_global_counter.stop()
        self.update_daily_counter.stop()
        self.refresh_file.stop()

    @tasks.loop(minutes=1)
    async def reset_daily_counter(self):

        # reset daily lb
        if datetime.datetime.now().strftime("%H:%M") == "00:00":

            with open("angels.json", "r") as f:
                file = json.load(f)

            file["daily_kills"] = 0

            with open("angels.json", "w") as f:

                json.dump(file, f, indent=4)
        

    @tasks.loop(minutes=10)
    async def update_daily_counter(self):

        guild = self.bot.get_guild(self.guild_id)

        with open("angels.json", "r") as f:
            file = json.load(f)

        daily_kills = file["daily_kills"]

        await self.bot.get_channel(self.daily_kills_channel).edit(name="⏰Killed: {:,}".format(daily_kills))

    @tasks.loop(minutes=10)
    async def update_global_counter(self):
        
        guild = self.bot.get_guild(self.guild_id)

        with open("angels.json", "r") as f:
            file = json.load(f)

        global_kills = 0

        for member, kills in file["users"].items():
            global_kills += kills

        await self.bot.get_channel(self.global_kills_channel).edit(name="🌍Killed: {:,}".format(global_kills))

    @tasks.loop(minutes=10)
    async def refresh_file(self):

        guild = self.bot.get_guild(self.guild_id)

        with open("angels.json", "r") as f:
            file = json.load(f)

        most_kills = max(file["users"], key=lambda key: file["users"][key])
        
        user_with_most_kills = await guild.fetch_member(most_kills)

        await self.bot.get_channel(self.global_leader_channel).edit(name=f"🌍⬆ {user_with_most_kills.name}")

        with open("angels.json", "w") as f:
            json.dump(file, f, indent=4)

    @commands.Cog.listener(name="on_message")
    async def increment_angels(self, ctx):

        if ctx.author.bot: return

        badwords = []

        with open("badwords.txt", "r") as f:

            badwords = f.readlines()

        kills = 0

        for word in badwords:

            words = re.findall(word[:-2], ctx.content.lower())

            kills += len(words)

        if kills > 0:

            with open("angels.json", "r") as f:
                file = json.load(f)

            if not str(ctx.author.id) in file["users"]:

                file["users"][str(ctx.author.id)] = kills

            else:

                file["users"][str(ctx.author.id)] += kills

            file["daily_kills"] += kills

            with open("angels.json", "w") as f:
                json.dump(file, f, indent=4)

        








async def setup(bot):
    await bot.add_cog(AngelCounter(bot))
        

        