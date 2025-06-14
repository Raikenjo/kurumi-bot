from discord.ext import commands
from bot.utils.logger import send_log

class OnReady(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"✅ Bot connected as {self.bot.user}")
        await send_log(self.bot, "🟢 Bot Aktif", f"{self.bot.user.name} telah online.")

async def setup(bot):
    await bot.add_cog(OnReady(bot))
