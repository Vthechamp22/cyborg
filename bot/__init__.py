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


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("!help"))
    print(f"Ready. Connected to {', '.join([g.name for g in bot.guilds])}.")


@bot.event
async def on_member_join(member: discord.Member):
    welcome = bot.get_channel(welcome_channel)
    await welcome.send(
        f"{member.mention} has joined this server!\n"
        f"Welcome {member.mention}!\n"
        f"Total Members = {member.guild.member_count}"
    )


@bot.event
async def on_member_remove(member: discord.Member):
    bye = bot.get_channel(bye_channel)
    name = str(member).split("#")[0]
    await bye.send(f"Bye {name}!\n" f"Total Members = {member.guild.member_count}")


@bot.command(name="users", help="How many users are there in the server")
async def user_count(ctx):
    guild = ctx.guild
    await ctx.send(f"There are {guild.member_count} people in {guild.name!r}")


@bot.command(name="create_channel", help="Creates a channel")
@commands.has_role("admin")
async def create_channel(ctx: commands.Context, channel_name="new-channel"):
    guild = ctx.guild
    channel_exists = discord.utils.get(guild.channels, name=channel_name)
    if not channel_exists:
        print(f"Creating a new channel {channel_name}")
        await guild.create_text_channel(channel_name)


@bot.command()
@commands.has_role("admin")
async def load(ctx, ext):
    bot.load_extension(f"cogs.{ext}")
    await ctx.send(f"{ext} loaded")


@bot.command()
@commands.has_role("admin")
async def unload(ctx, ext):
    bot.unload_extension(f"cogs.{ext}")
    await ctx.send(f"{ext} unloaded")


@bot.command()
@commands.has_role("admin")
async def reload(ctx, ext):
    bot.reload_extension(f"cogs.{ext}")
    await ctx.send(f"{ext} reloaded")


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
