import discord
from discord.ext import commands

import datetime
import random

class ButtonHandler(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def e(self, ctx):

        view = discord.ui.View()

        view.add_item(discord.ui.Button(label="EEEEEEEEEEEEEEEE!", style=discord.ButtonStyle.green, custom_id="the_button"))

        await ctx.send("e!", view=view)

    @commands.Cog.listener(name="on_interaction")
    async def button_pressed(self, interaction: discord.Interaction):

        if interaction.data['custom_id'] == "the_button":

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

        

async def setup(bot):
    await bot.add_cog(ButtonHandler(bot))
