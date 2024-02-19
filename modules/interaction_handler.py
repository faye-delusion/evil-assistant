import discord
from discord.ext import commands

import datetime
import random

class InteractionHandler(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def button(self, ctx):

        view = discord.ui.View()

        view.add_item(discord.ui.Button(label="EEEEEEEEEEEEEEEE!", style=discord.ButtonStyle.green, custom_id="the_button"))

        await ctx.send("e!", view=view)

    @commands.command()
    @commands.is_owner()
    async def lethalcompanyrole(self,ctx):

        view = discord.ui.View()

        view.add_item(discord.ui.Button(emoji="➕", style=discord.ButtonStyle.green, custom_id="LCADD"))
        view.add_item(discord.ui.Button(emoji="➖", style=discord.ButtonStyle.red, custom_id="LCRM"))

        embed = discord.Embed(

            title="Use buttons to add/remove role",
            description=f"Role: {discord.utils.get(self.bot.get_guild(817475690499670066).roles, id=1189028560346824784).mention}\nDescription: LFG ping role for Lethal Company players."

        )

        await ctx.send(embed=embed, view=view)

    @commands.Cog.listener(name="on_interaction")
    async def button_pressed(self, interaction: discord.Interaction):

        if not interaction.type == discord.InteractionType.component: return
        
        if interaction.data['custom_id'] == "the_button":

            # THE BUTTON

            view = discord.ui.View()

            emoji_list = ["🤭", "🥶", "😀","🤯", "🥴", "🤠", "🐟", "👻", "🏴‍☠️", "❤️", "📍", "🚪", "🛌", "🧱", "🔨", "🗿", "🛩️", "🎰"]

            scenarios = [

                [

                    discord.ui.Button(emoji="⭐", style=discord.ButtonStyle.green, custom_id="the_button"),
                    discord.ui.Button(emoji="☠️", style=discord.ButtonStyle.red, custom_id="punishment_button"),
                    discord.ui.Button(emoji=random.choice(emoji_list), style=discord.ButtonStyle.green, disabled=True),
                    discord.ui.Button(emoji=random.choice(emoji_list), style=discord.ButtonStyle.green, disabled=True),
                    discord.ui.Button(emoji=random.choice(emoji_list), style=discord.ButtonStyle.green, disabled=True)

                ],

                [

                    discord.ui.Button(emoji="🙂", style=discord.ButtonStyle.grey, custom_id="the_button"),
                    discord.ui.Button(emoji="❌", style=discord.ButtonStyle.grey),
                    discord.ui.Button(emoji="❌", style=discord.ButtonStyle.grey),
                    discord.ui.Button(emoji="❌", style=discord.ButtonStyle.grey),
                    discord.ui.Button(emoji="❌", style=discord.ButtonStyle.grey)

                ],

                [

                    discord.ui.Button(label="Click me!", style=discord.ButtonStyle.red, custom_id="the_button"),
                    discord.ui.Button(label="Not me!", style=discord.ButtonStyle.red, disabled=True),
                    discord.ui.Button(label="Not me!", style=discord.ButtonStyle.red, disabled=True),
                    discord.ui.Button(label="Not me!", style=discord.ButtonStyle.red, disabled=True),
                    discord.ui.Button(label="Not me!", style=discord.ButtonStyle.red, disabled=True),
                    
                ],

                [

                    discord.ui.Button(emoji="⭐", style=discord.ButtonStyle.red, custom_id="the_button"),
                    discord.ui.Button(emoji="☠️", style=discord.ButtonStyle.green, custom_id="punishment_button"),
                    discord.ui.Button(emoji="☠️", style=discord.ButtonStyle.green, custom_id="punishment_button"),
                    discord.ui.Button(emoji="☠️", style=discord.ButtonStyle.green, custom_id="punishment_button"),
                    discord.ui.Button(emoji="☠️", style=discord.ButtonStyle.green, custom_id="punishment_button")

                ]

            ]

            buttons = random.choice(scenarios)

            random.shuffle(buttons)

            for btn in buttons:
                view.add_item(btn)

            embed = discord.Embed(

                description=f"{interaction.user.mention} was here!"

            )

            embed.set_image(url=interaction.user.avatar.url)
            embed.timestamp = datetime.datetime.now()

            await interaction.response.edit_message(content=" ", embed=embed, view=view)

        elif interaction.data["custom_id"] == "punishment_button":

            await interaction.response.send_message(content="Wrong button buddy :)", ephemeral=True)

        elif interaction.data["custom_id"] == "LCADD":

            role = discord.utils.get(interaction.guild.roles, id=1189028560346824784)

            try:

                await interaction.user.add_roles(role, reason="they WANTED that shit fr")

            except:

                await interaction.response.send_message(content="Something went wrong, role was not added.", ephemeral=True)

            else:

                await interaction.response.send_message(content="Added role.", ephemeral=True)


        elif interaction.data["custom_id"] == "LCRM":

            role = discord.utils.get(interaction.guild.roles, id=1189028560346824784)

            try:

                await interaction.user.remove_roles(role, reason="they WANTED that shit fr")

            except:

                await interaction.response.send_message(content="Something went wrong, role was not removed.", ephemeral=True)

            else:

                await interaction.response.send_message(content="Removed role.", ephemeral=True)


        

async def setup(bot):
    await bot.add_cog(InteractionHandler(bot))
