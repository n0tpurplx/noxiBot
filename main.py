import os
import discord
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="_", intents=intents)


@bot.event
async def on_ready():
    await bot.tree.sync()

    update_presence.start()

    print(f"Logged in as {bot.user}")


@tasks.loop(seconds=60)
async def update_presence():
    # Watching server count
    await bot.change_presence(
        status=discord.Status.dnd,
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=f"{len(bot.guilds)} servers"
        )
    )

    # Wait another 60 seconds
    await discord.utils.sleep_until(
        discord.utils.utcnow() + discord.timedelta(seconds=60)
    )

    # Invite presence
    await bot.change_presence(
        status=discord.Status.dnd,
        activity=discord.Activity(
            type=discord.ActivityType.playing,
            name="Join .gg/3dqrSEKWT4"
        )
    )


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

    embed.add_field(
        name="Status",
        value="All Services operational",
        inline=True
    )
    embed.add_field(
        name="Servers",
        value="1",
        inline=True
    )
    embed.set_footer(text="NoxiBkt")

    await interaction.response.send_message(embed=embed)


@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


bot.run(os.getenv("DISCORD_TOKEN"))
