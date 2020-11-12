from discord.ext import commands
import random
from bot.utils.constants import Responses
from discord.ext.commands import Context


class Random(commands.Cog):
    def __init__(self, bot):
        # super().__init__()
        self.bot = bot

    @commands.command(help="Rolls a dice and returns a random number")
    async def roll(self, ctx: Context, s: int = 6, d: int = 1):
        rsp = list(map(str, [random.randint(1, s) for _ in range(d)]))
        await ctx.send(
            f"{ctx.author.mention} rolled {d} die/dice with {s} sides and "
            f"got {', '.join(rsp)}"
        )

    @commands.command(help="Tosses a coin and gives back the result")
    async def toss(self, ctx: Context):
        await ctx.send(
            f"{ctx.author.mention}... it's {random.choice(['tails', 'heads'])}!"
        )

    @commands.command(name="8ball", help="Gives back a random 8ball response")
    async def _8ball(self, ctx: commands.Context, *, q=None):
        if not q:
            await ctx.send("Hey! Ask a question!")
            return

        await ctx.send(random.choice(Responses.eight_ball_outcomes))


def setup(bot):
    bot.add_cog(Random(bot))
