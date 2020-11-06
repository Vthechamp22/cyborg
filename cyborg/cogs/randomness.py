from discord.ext import commands
import random


class Random(commands.Cog):
    def __init__(self, client):
        # super().__init__()
        self.client = client

    @commands.command(
        name="roll",
        help="Rolls a dice and returns a random \
number",
    )
    async def roll(self,
                   ctx: commands.context.Context,
                   s: int = 6,
                   d: int = 1):
        rsp = list(map(str, [random.randint(1, s) for _ in range(d)]))
        await ctx.send(f"{ctx.author.mention} rolled {d} dice with {s} sides \
and got {', '.join(rsp)}")

    @commands.command(
        name="toss",
        help="Tosses a coin and gives back the \
result",
    )
    async def toss(self, ctx: commands.context.Context):
        await ctx.send(f"{ctx.author.mention}... it's \
{random.choice(['tails', 'heads'])}!")

    @commands.command(name="8ball", help="Gives back a random 8ball response")
    async def _8ball(self, ctx: commands.Context, *, q=None):
        if q is None:
            await ctx.send("Hey! Ask a question!")
            return
        outcomes = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes – definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful.",
        ]
        await ctx.send(random.choice(outcomes))


def setup(client):
    client.add_cog(Random(client))
