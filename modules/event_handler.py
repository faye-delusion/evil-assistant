import discord
from discord.ext import commands

import datetime

class EventHandler(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener(name="on_member_join")
    async def member_joined(self, member: discord.Member):

        if member.bot: return

        member_log_channel = member.guild.get_channel(879784150314389514)

        member_role = discord.utils.get(member.guild.roles, id=817475690499670070)

        await member.add_roles(member_role)
        await member_log_channel.send(embed=discord.Embed(title="Member Joined", description=f"{member.mention}", color=discord.Color.green()).set_image(url=member.avatar.url))

    @commands.Cog.listener(name="on_member_remove")
    async def member_leave(self, member):

        if member.bot: return

        member_log_channel = member.guild.get_channel(879784150314389514)  

        await member_log_channel.send(embed=discord.Embed(title="Member Left", description=f"{member.mention}", color=discord.Color.red()).set_image(url=member.avatar.url))
        


async def setup(bot):
    await bot.add_cog(EventHandler(bot))