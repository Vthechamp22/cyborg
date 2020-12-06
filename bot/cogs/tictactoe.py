# from PIL import Image, ImageDraw
import discord
import json
from discord.ext import commands
from discord.ext.commands.context import Context

# import typing
from discord.ext.commands import Bot
from pathlib import Path

ttt_path = Path("bot", "resources", "tictactoe.json")

with ttt_path.open("r") as f:
    data = json.load(f)


def update():
    with ttt_path.open("w") as f:
        json.dump(data, f)


# CONSTANTS:
BOX_SIZE = 30
L_M = 20
T_M = 20

EMPTY_BOARD = [["" for _ in range(3)] for _ in range(3)]


class Tictactoe(commands.Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @commands.command(name="start_t")
    async def start_tictactoe(self, ctx: Context):
        if data.get(str(ctx.author)) is None:
            data[str(ctx.author)] = {
                "board": EMPTY_BOARD,
                "chance": str(ctx.author),
                "other": None,
                "invited": None,
            }
            update()
            await ctx.send("Game started!")
        else:
            await ctx.send("You already have a game started!")

    @commands.command(name="invite_t")
    async def invite_tictactoe(self, ctx, mem: discord.User = None):
        if mem is None:
            await ctx.send("You need to mention a user to invite them!")
            return
        elif data.get(str(ctx.author)) is None:
            await ctx.send("Start a game using !start_t first!")
            return
        elif (au_data := data.get(str(ctx.author))) is not None:
            if au_data["other"] is not None:
                await ctx.send("You have already invited another player!")
                return
        invitee = str(mem)
        au_data["invited"] = invitee
        update()
        if (dm_channel := mem.dm_channel) is None:
            dm_channel = await mem.create_dm()
        await dm_channel.send(
            f"**{ctx.author.mention}** has invited you to a game \
of tictactoe!\nGo to **{ctx.guild.name!r}** and type `!accept_t` to accept the\
invite or\
`!decline_t` to decline it."
        )

    @commands.command(name="play_t")
    async def play_tictactoe(self, ctx, A: str, N: int):
        if data.get(ctx.author) is None:
            await ctx.send("You haven't started any game yet!!")
        else:
            await ctx.send("LESS PLAY!")

    @commands.command(name="accept_t")
    async def accept(self, ctx):
        print("HERE!")
        for player in data.keys():
            if data[player]["invited"] == str(ctx.author):
                if data[player]["other"] == str(ctx.author):
                    await ctx.send(
                        "You have already accepted the challenge." " :neutral_face:"
                    )
                    return
                await ctx.send(
                    f"{ctx.author.mention} has accepted \
{ctx.guild().get_member_named(player).mention}'s challenge!"
                )
            data[player]["other"] = str(ctx.author)
            update()
            return
        else:
            await ctx.send("No one had ever invited you... :eyes:. Use")


def setup(bot):
    bot.add_cog(Tictactoe(bot))


"""
for i in range(5):
    for j in range(5):
        t = 20 * i
        b = t + 20
        l = 20 * j
        r = l + 20
        draw.rectangle([(l, t), (r, b)], fill='red', width=1, outline='black')
"""
