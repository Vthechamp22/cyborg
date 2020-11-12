from discord.ext import commands
from discord.ext.commands.context import Context


class Server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is online.")

    @commands.command(name="get_reactions")
    async def get_reactions(ctx: Context, *, url: str):
        message_id = url.split("/")[-1]
        msg = await ctx.fetch_message(message_id)
        await ctx.send(", ".join([
            f"{reaction.count} reaction(s) of the {reaction.emoji}"
            for reaction in msg.reactions
        ]))


def setup(bot):
    bot.add_cog(Server(bot))
