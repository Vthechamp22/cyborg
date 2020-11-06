# TODO: Clear all messages
# TODO: get profile_pic
# TODO: pixelate
# TODO: announce when clearing messages
# TODO: Random number guessing game
# TEST: Handle error when cog isn't loaded and you try to reload it
# TODO: Meme adder
# TODO: Finish Tictactoe

from pathlib import Path
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

assert TOKEN is not None, f"Token is {TOKEN!r}, please check .env"


def get_static(filename: str) -> Path:
    return Path("resources", filename)


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)
bot.remove_command("help")

welcome_channel_id = 761266399078252575
bye_channel_id = 761266399078252575


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("!help"))
    print(f"Ready. Connected to {', '.join([g.name for g in bot.guilds])}.")


@bot.event
async def on_member_join(member: discord.Member):
    welcome_channel = bot.get_channel(welcome_channel_id)
    await welcome_channel.send(f"{member.mention} has joined this server!\
\nWelcome {member.mention}!\nTotal Members = {member.guild.member_count}")


@bot.event
async def on_member_remove(member: discord.Member):
    bye_channel = bot.get_channel(bye_channel_id)
    name = str(member).split("#")[0]
    await bye_channel.send(f"Bye {name}!\
\nTotal Members = {member.guild.member_count}")


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
for filename in os.listdir(Path("cogs")):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


@bot.command()
async def help(ctx):
    embed_msg = discord.Embed(title="Help",
                              description="Help on commands",
                              color=0x0077B6)

    embed_msg.set_thumbnail(url="https://cdn.discordapp.com/avatars/\
732582128134389830/8265922627d3cdab6d7a7af15709ef5f.png?size=256")

    for command in bot.commands:
        embed_msg.add_field(name=command,
                            value=command.help + "\n",
                            inline=False)
    embed_msg.set_footer(
        text="You can type out the command for more information")

    await ctx.send(embed=embed_msg)


@bot.event
async def on_command_error(ctx: commands.Context, err):
    if isinstance(err, commands.errors.CheckFailure):
        await ctx.send(
            "You do not have the correct role for this command :eyes:")
    else:
        await ctx.send(", ".join(err.args))


bot.run(TOKEN)
