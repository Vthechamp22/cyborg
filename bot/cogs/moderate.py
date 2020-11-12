import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="kick", help="Kicks a member")
    @commands.has_role("admin")
    async def kick(self,
                   ctx: commands.Context,
                   member: discord.Member = None,
                   reason=None):
        if member is None:
            await ctx.send("Please give in a member name!")
            return
        await member.kick(reason=reason)
        await ctx.send(f"Kicked {member.name}")

    @commands.command(name="unban", help="Unbans a member")
    @commands.has_role("admin")
    async def unban(self, ctx: commands.Context, member=None, reason=None):
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

    @commands.command(name="ban", help="Bans a member")
    @commands.has_role("admin")
    async def ban(self,
                  ctx: commands.Context,
                  member: discord.Member = None,
                  reason=None):
        if member is None:
            await ctx.send("Please give in a member name!")
            return
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member.name}")

    @commands.command(
        name="clear",
        help="Clear the number of messages specified (5 by default)")
    @commands.has_role("admin")
    async def clear(self, ctx: commands.Context, amt: int = 5):
        await ctx.channel.purge(limit=amt + 1)


def setup(bot):
    bot.add_cog(Moderation(bot))
