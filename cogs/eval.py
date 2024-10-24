import discord
from discord.ext import commands
import io
import contextlib

class Eval(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="eval")
    @commands.is_owner()  # owner only command
    async def eval(self, ctx, *, code: str):
        # strips the code block indicators (```py, ``` or any spaces)
        code = code.strip('` ')  # removes backticks and spaces
        
        if code.startswith("py"):
            code = code[2:].strip()  #removes py prefix

        output = io.StringIO()
        
        # redirects stdout
        with contextlib.redirect_stdout(output):
            try:
                # Use exec to run the code
                exec(code, {"__builtins__": __builtins__})
            except Exception as e:
                # captures any exceptions and return them
                await ctx.send(f"Error: {e}")
                return
        
        # gets the output from the stringio
        result = output.getvalue()
        
        # notifies user if there is no output
        if not result:
            result = "No output."
        
        # sends the output back to the Discord channel
        await ctx.send(f"```py\n{result}```")

async def setup(bot):
    await bot.add_cog(Eval(bot))
