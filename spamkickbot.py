import discord
import time
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user.name}')

@bot.command()
async def kick(ctx, member: discord.Member):
    if ctx.author.guild_permissions.kick_members:
        if ctx.author.voice:
            if member.voice:
                for _ in range(30):
                    await member.move_to(None)
                    time.sleep(1)
                await ctx.send(f"{member.mention} has been forcefully moved from voice channels.")
            else:
                await ctx.send(f"{member.mention} is not in a voice channel.")
        else:
            await ctx.send("You must be in a voice channel to use this command.")
    else:
        await ctx.send("You do not have the necessary permissions to use this command.")

@bot.command()
async def stop(ctx):
    await ctx.send("Bot is stopping. Goodbye!")
    await bot.close()

bot.run('YOUR_BOT_TOKEN')
