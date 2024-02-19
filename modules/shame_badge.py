import discord
from discord.ext import commands

class BadgeOfShameHandler(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener(name="on_presence_update")
    async def add_shame_badge(self, before: discord.Member, after: discord.Member):

        guild = self.bot.get_guild(817475690499670066)

        badge_of_shame = discord.utils.get(guild.roles, id=1193726381654298636)

        if after.bot: return

        current_activities = after.activities

        for activity in current_activities:

            shame_list = [

                "genshin impact",
                "honkai: star rail",
                "valorant",
                "league of legends",
                "overwatch 2",
                "osu!",
                "world of warcraft",
                "team fortress 2",
                "world of tanks"

            ]

            if activity.name.lower() in shame_list:

                try:

                    await after.add_roles(badge_of_shame, reason=f"caught playing {activity.name}")

                except:

                    return
                
                else:

                    channel = guild.get_channel(817475690558521353)

                    await channel.send(embed=discord.Embed(title=f"{after.name} was given the BADGE OF SHAME!!!!!", description=f"caught this mf playing {activity.name}"))


async def setup(bot):
    await bot.add_cog(BadgeOfShameHandler(bot))