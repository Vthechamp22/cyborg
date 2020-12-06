from pathlib import Path
import discord

import os
from discord.ext import commands
from bot.utils.constants import Channels

welcome_channel, bye_channel = Channels.welcome, Channels.bye


def get_static(filename: str) -> Path:
    return Path("resources", filename)


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)
bot.remove_command("help")


@bot.command(name="create_channel", help="Creates a channel")
@commands.has_role("admin")
async def create_channel(ctx: commands.Context, channel_name="new-channel"):
    guild = ctx.guild
    channel_exists = discord.utils.get(guild.channels, name=channel_name)
    if not channel_exists:
        print(f"Creating a new channel {channel_name}")
        await guild.create_text_channel(channel_name)


# Load all Cogs
for filename in os.listdir(Path("bot", "cogs")):
    if filename.endswith(".py"):
        bot.load_extension(f"bot.cogs.{filename[:-3]}")


@bot.command()
async def help(ctx):
    embed_msg = discord.Embed(
        title="Help", description="Help on commands", color=0x0077B6
    )

    embed_msg.set_thumbnail(
        url=(
            "https://cdn.discordapp.com/avatars/"
            "732582128134389830/8265922627d3cdab6d7a7af15709ef5f.png?size=256"
        )
    )

    for command in bot.commands:
        embed_msg.add_field(name=command, value=command.help, inline=False)  # + "\n",
    embed_msg.set_footer(text="You can type out the command for more information")

    await ctx.send(embed=embed_msg)


@bot.event
async def on_command_error(ctx: commands.Context, err):
    if isinstance(err, commands.errors.CheckFailure):
        await ctx.send("You do not have the correct role for this command :eyes:")
    else:
        await ctx.send(", ".join(err.args))
