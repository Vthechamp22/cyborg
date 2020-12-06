from discord.ext.commands import Context, Bot, Cog, command, group
from discord import Member


class Moderation(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @command(name="kick", help="Kicks a member")
    async def kick(self, ctx: Context, member: Member = None, reason=None):
        if member is None:
            await ctx.send("Please give in a member name!")
            return
        await member.kick(reason=reason)
        await ctx.send(f"Kicked {member.name}")

    @command(name="unban", help="Unbans a member")
    async def unban(self, ctx: Context, member=None, reason=None):
        if member is None:
            await ctx.send("Please give in a member name!")
            return

        banned = await ctx.guild.bans()
        name, disc = member.split("#")
        for banned_user in banned:
            user = banned_user.user

            if (user.name, user.discriminator) == (name, disc):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {name}#{disc}")
                return

    @command(name="ban", help="Bans a member")
    async def ban(self, ctx: Context, member: Member = None, reason=None):
        if member is None:
            await ctx.send("Please give in a member name!")
            return
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member.name}")

    @command(name="clear", help="Clear the number of messages specified (5 by default)")
    async def clear(self, ctx: Context, amt: int = 5):
        await ctx.channel.purge(limit=amt + 1)

    @group(name="cogs", invoke_without_context=False)
    async def cogs(self, ctx: Context):
        pass

    @cogs.command()
    async def load(self, ctx: Context, ext: str):
        self.bot.load_extension(f"bot.cogs.{ext}")
        await ctx.send(f"Cog {ext!r} loaded")

    @cogs.command()
    async def unload(self, ctx: Context, ext: str):
        self.bot.unload_extension(f"bot.cogs.{ext}")
        await ctx.send(f"Cog {ext!r} unloaded")

    @cogs.command()
    async def reload(self, ctx: Context, ext: str):
        self.bot.reload_extension(f"bot.cogs.{ext}")
        await ctx.send(f"Cog {ext!r} reloaded")

    def cog_check(self, ctx: Context):
        return "admin" in [role.name for role in ctx.author.roles]


def setup(bot):
    bot.add_cog(Moderation(bot))
