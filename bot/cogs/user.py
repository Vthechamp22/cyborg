import discord
from discord.ext import commands
from discord.ext.commands import Context


class User(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="userinfo")
    async def user_info(self, ctx: Context, *, user: discord.User):  # Discord.Member?
        await ctx.send(f"{user.created_at}")


def setup(bot):
    bot.add_cog(User(bot))
