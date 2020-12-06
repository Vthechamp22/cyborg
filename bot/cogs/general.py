# from discord import Guild
from discord.channel import TextChannel
from discord.ext import commands
from discord.ext.commands.cog import Cog
from discord.ext.commands.context import Context
from discord.ext.commands import Bot
from discord import Game, Member
from bot.utils.constants import Channels


class Server(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    # Events
    @Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=Game("!help"))
        print("Bot is online.")

    @commands.command(name="get_reactions")
    async def get_reactions(ctx: Context, *, url: str):
        message_id = url.split("/")[-1]
        msg = await ctx.fetch_message(message_id)
        await ctx.send(
            ", ".join(
                [
                    f"{reaction.count} reaction(s) of the {reaction.emoji}"
                    for reaction in msg.reactions
                ]
            )
        )

    @Cog.listener()
    async def on_member_join(self, member: Member):
        welcome: TextChannel = self.bot.get_channel(Channels.welcome)
        await welcome.send(
            f"**{member.mention} has joined this server!\n**"
            f"Welcome {member.mention}!\n"
            f"Total Members = {member.guild.member_count - 1}"
        )

    @Cog.listener()
    async def on_member_remove(self, member: Member):
        bye = self.bot.get_channel(Channels.bye)
        name = str(member).split("#")[0]
        await bye.send(
            f"Bye {name} :cry:!\n" f"Total Members = {member.guild.member_count - 1}"
        )


def setup(bot: Bot):
    bot.add_cog(Server(bot))
