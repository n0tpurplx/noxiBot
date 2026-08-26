import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="_", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()

    await bot.change_presence(
        status=discord.Status.dnd,
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=f"{len(bot.guilds)} servers"
        )
    )

    print(f"Logged in as {bot.user}")

@bot.tree.command(name="ping")
async def slash_ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")

@bot.tree.command(name="emtest")
async def emtest(interaction: discord.Interaction):
    embed = discord.Embed(
    title="Test Embed",
    description="This is a test embed!",
    color=discord.Color.blue()
)

embed.add_field(name="Status", value="All Services operational", inline=True)
embed.add_field(name="Servers", value="1", inline=True)
embed.set_footer(text="NoxiBkt")

await interaction.response.send_message(embed=embed)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(os.getenv("DISCORD_TOKEN"))
