import discord
from redbot.core.bot import Red
from redbot.core import commands
from redbot.core.commands import Cog
import logging


__author__ = "tmerc, Lifeismana"

log = logging.getLogger("red.Lifeismana.lenny")


class Test(commands.Cog):
    """My custom cog"""
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="test", guild_ids=[308999529485828098])
    async def test(self, ctx):
        """☞⇀‿↼☞"""
        

        await ctx.send("data")
