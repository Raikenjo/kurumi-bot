import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_IDS = [discord.Object(id=int(gid.strip())) for gid in os.getenv("GUILD_ID").split(",")]

class KurumiBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!", 
            intents=discord.Intents.all(), 
            application_id=os.getenv("CLIENT_ID")
        )
        # Hapus self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.load_extension("bot.commands.on_ready")
        await self.load_extension("bot.events.ping")
        await self.load_extension("bot.events.moderation")

        # Sync slash commands ke semua GUILD
        for guild in GUILD_IDS:
            synced = await self.tree.sync(guild=guild)
            print(f"🔁 Synced {len(synced)} command(s) to guild {guild.id}")
            
            # Send log to embed log channel
            from bot.utils.logger import send_log
            cmd_list = "\n".join(f"`/{cmd.name}` - {cmd.description}" for cmd in synced)
            await send_log(
                self,
                title=f"🛠️ Slash Commands Synced",
                description=f"**Guild ID:** `{guild.id}`\n**Total:** `{len(synced)}` command(s)\n\n{cmd_list}",
                color=discord.Color.orange()
            )
        await self.tree.sync()

def run_bot():
    bot = KurumiBot()
    bot.run(TOKEN)
