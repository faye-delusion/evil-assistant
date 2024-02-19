import discord
from discord.ext import commands

class Highlights(commands.Cog):

    def __init__(self,bot: commands.Bot):
        self.bot = bot
        self.highlights_menu = discord.app_commands.ContextMenu(

            name = "Highlight This Message",
            callback = self.highlights_callback

        )
        self.bot.tree.add_command(self.highlights_menu)

    async def highlights_callback(self, interaction: discord.Interaction, message: discord.Message):

        output_embed = discord.Embed(

            title=f"{message.author.name}",
            description=f"{message.content}",
            color=discord.Color.random()

        )

        output_channel = self.bot.get_channel(1209230611362091038)

        pinned_message = await output_channel.send(content=f"{message.author.mention} ([Original Message]({message.jump_url})):\n{message.content}\n{' '.join([message.attachments[i].url for i in range(0,len(message.attachments))])}")

        await interaction.response.send_message(f"New pinned message added. [See Here]({pinned_message.jump_url})")
    

async def setup(bot):
    await bot.add_cog(Highlights(bot))
