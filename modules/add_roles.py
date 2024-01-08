import discord
from discord.ext import commands

class LCButtons(discord.ui.View):

    def __init__(self, *, timeout=None):
        super().__init__(timeout=timeout)

    @discord.ui.button(emoji="➕", style=discord.ButtonStyle.green)
    async def add_role_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        role = discord.utils.get(interaction.guild.roles, id=1189028560346824784)

        try:

            await interaction.user.add_roles(role, reason="they WANTED that shit fr")

        except:

            await interaction.response.send_message(content="Something went wrong, role was not added.", ephemeral=True)

        else:

            await interaction.response.send_message(content="Added role.", ephemeral=True)

    @discord.ui.button(emoji="➖", style=discord.ButtonStyle.red)
    async def remove_role_button(self, interaction: discord.Interaction, button: discord.ui.Button):

        role = discord.utils.get(interaction.guild.roles, id=1189028560346824784)

        try:

            await interaction.user.remove_roles(role, reason="they WANTED that shit fr")

        except:

            await interaction.response.send_message(content="Something went wrong, role was not removed.", ephemeral=True)

        else:

            await interaction.response.send_message(content="Removed role.", ephemeral=True)

class RoleAddHandler(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def lethalcompanyrolething(self,ctx):

        embed = discord.Embed(

            title="Use buttons to add/remove role",
            description=f"Role: {discord.utils.get(self.bot.get_guild(817475690499670066).roles, id=1189028560346824784).mention}\nDescription: LFG ping role for Lethal Company players."

        )

        await ctx.send(embed=embed, view=LCButtons())


async def setup(bot):
    await bot.add_cog(RoleAddHandler(bot))