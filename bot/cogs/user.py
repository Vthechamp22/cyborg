import discord
from discord.ext.commands import Context, command, Cog, Bot


class User(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @command(name="userinfo")
    async def user_info(self, ctx: Context, *, user: discord.User):  # Discord.Member?
        await ctx.send(user.created_at.strftime("%d/%m/%Y"))  # TODO: Add more info

    @command(name="usercount", help="How many users are there in the server")
    async def user_count(self, ctx: Context):
        guild = ctx.guild
        await ctx.send(f"There are {guild.member_count} people in {guild.name!r}")


def setup(bot):
    bot.add_cog(User(bot))
