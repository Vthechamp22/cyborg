# TODO: Add quadratic solving equation thingy

import math
from discord.ext import commands


class Math(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(
        name="add", aliases=["+", "plus"], help="Add numbers (or words :smirk:)"
    )
    async def add(self, ctx, *args):
        if len(args) == 0:
            await ctx.send("Please tell in numbers to add!")
            return
        elif not all([arg.isdigit() for arg in args]):
            summed = "".join(args)
        else:
            floatargs = list(map(float, args))
            summed = 0
            for n in floatargs:
                summed += n
            if summed.is_integer():
                summed = int(summed)

        await ctx.send(f'{ctx.author.mention} {" + ".join(args)}  is **{summed}**')

    @commands.command(
        name="subtract", aliases=["minus", "-"], help="Subtract two numbers"
    )
    async def subtract(self, ctx, n1=None, n2=None):
        if n1 is None or n2 is None:
            await ctx.send("Please specify two numbers!")
            return
        elif not all([n.isdigit() for n in [n1, n2]]):
            await ctx.send("Please type only numbers!")
            return

        n1, n2 = int(n1), int(n2)

        await ctx.send(f"{ctx.author.mention} {n1} - {n2} is **{n1 - n2}**")

    @commands.command(
        name="mult",
        aliases=["x", "multiply"],
        help="Multiply numbers (or a word and a num :smirk:)",
    )
    async def multiply(self, ctx, *args):
        if len(args) == 0:
            await ctx.send("Please tell in numbers to add!")
            return
        elif len(args) == 2 and args[1].isdigit() and not args[0].isdigit():
            await ctx.send(
                f'{ctx.author.mention} {" × ".join(args)}  \
is **{args[0] * int(args[1])}**'
            )
            return
        elif not all([arg.isdigit() for arg in args]):
            await ctx.send("Please type only numbers!")
            return
        floatargs = list(map(float, args))
        prod = math.prod(floatargs)
        if prod.is_integer():
            prod = int(prod)
        await ctx.send(
            f'{ctx.author.mention} {" × ".join(args)}  \
is **{prod}**'
        )

    @commands.command(name="div", aliases=["/", "divide"], help="Divides two numbers")
    async def divide(self, ctx, n1=None, n2=None):
        if n1 is None or n2 is None:
            await ctx.send("Please specify two numbers!")
            return
        elif not all([n.isdigit() for n in [n1, n2]]):
            await ctx.send("Please type only numbers!")
            return

        n1, n2 = float(n1), float(n2)

        res = n1 / n2
        if res.is_integer():
            res = int(res)
        await ctx.send(f"{ctx.author.mention} {n1} ÷ {n2} is **{res}**")


def setup(bot):
    bot.add_cog(Math(bot))
