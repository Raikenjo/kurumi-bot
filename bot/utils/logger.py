import discord
import os
from dotenv import load_dotenv

load_dotenv()
LOG_CHANNEL_IDS = [int(cid.strip()) for cid in os.getenv("logChannelId", "").split(",")]

async def send_log(bot: discord.Client, title: str, description: str, color: discord.Color = discord.Color.blurple()):
    embed = discord.Embed(title=title, description=description, color=color)
    embed.set_footer(text="Kurumi Bot Logging")
    
    for channel_id in LOG_CHANNEL_IDS:
        channel = bot.get_channel(channel_id)
        if isinstance(channel, discord.TextChannel):
            try:
                await channel.send(embed=embed)
            except Exception as e:
                print(f"⚠️ Gagal kirim log ke channel {channel_id}: {e}")
