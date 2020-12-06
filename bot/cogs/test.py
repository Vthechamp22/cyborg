import discord
from discord.ext import commands
from discord.ext.commands import Context


class Server(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Events
    @commands.has_role("admin")
    @commands.command(name="embed")
    async def send_embed(self, ctx: commands.Context):
        embed = discord.Embed(title="Test", description="This is a test embed")
        embed.add_field(name="Test_name", value="[Test_value](https://google.com)")

        await ctx.send(embed=embed)

    @commands.command(name="test")
    async def create_dm_channel_test(self, ctx: Context, *, user: discord.User):
        print(type(user))
        print("\n".join(dir(user)))


def setup(bot):
    bot.add_cog(Server(bot))
