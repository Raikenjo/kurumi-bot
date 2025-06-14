import discord
from discord.ext import commands
from bot.utils.logger import send_log

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="kick", description="Kick member dari server")
    async def kick(self, interaction: discord.Interaction, member: discord.Member, reason: str = "No reason provided"):
        await member.kick(reason=reason)
        await interaction.response.send_message(f"{member.mention} telah di-kick. ✅", ephemeral=True)

        await send_log(
            self.bot,
            "👢 Member Di-Kick",
            f"{member.mention} di-kick oleh {interaction.user.mention}\n**Alasan:** {reason}",
            color=discord.Color.red()
        )

async def setup(bot):
    await bot.add_cog(Moderation(bot))
