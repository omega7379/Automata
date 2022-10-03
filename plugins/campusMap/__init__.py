from nextcord.ext import commands

from Plugin import AutomataPlugin


class campusMap(AutomataPlugin):
    """Campus Map"""

    @commands.command()
    async def map(self, ctx: commands.Context, *, search_terms: str):
        """Replies with image of indexed map for quick navigation"""

# TODO figure out how to show local png files.
# create dictionary
# use search_terms to call indexed answers

        if search_terms == 'AA' or 'Arts & Admin':
            await ctx.send()
