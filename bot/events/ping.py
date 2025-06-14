import discord
from discord.ext import commands
from bot.utils.logger import send_log

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="ping", description="Cek latensi bot")
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)
        await interaction.response.send_message(f"Pong! `{latency}ms`")

        await send_log(
            self.bot,
            "📶 Ping Digunakan",
            f"{interaction.user.mention} menggunakan `/ping`.\n**Latency:** `{latency}ms`",
            color=discord.Color.green()
        )

async def setup(bot):
    await bot.add_cog(Ping(bot))
