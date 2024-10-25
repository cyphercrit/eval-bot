import discord
from discord.ext import commands
import io
import contextlib
import asyncio
import concurrent.futures

class Eval(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.executor = concurrent.futures.ThreadPoolExecutor()
    
    @commands.command(name="eval")
    @commands.is_owner()  # owner only command
    async def eval(self, ctx, *, code: str):
        # strips the code block indicators (```py, ``` or any spaces)
        code = code.strip('` ')  # removes backticks and spaces
        
        if code.startswith("py"):
            code = code[2:].strip()  # removes py prefix

        output = io.StringIO()
        
        # redirects stdout
        with contextlib.redirect_stdout(output):
            try:
                # uses asyncio to run the code with a timeout
                await asyncio.wait_for(self.run_code(code, output), timeout=5)
            except asyncio.TimeoutError:
                await ctx.send(f"```Error: Exceeded maximum timeout of 5 seconds.```")
                return
            except Exception as e:
                # captures any exceptions and return them
                await ctx.send(f"```Error: {e}```")
                return
        
        # gets the output from the stringio
        result = output.getvalue()
        
        # notifies user if there is no output
        if not result:
            result = "No output."
        
        # sends the output back to the discord channel
        await ctx.send(f"```py\n{result}```")

    async def run_code(self, code, output):
        # runs code in separate thread
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(self.executor, self.exec_code, code, output)

    def exec_code(self, code, output):
        try:
            exec(code, {"__builtins__": __builtins__})
        except SyntaxError as e:
            output.write(f"SyntaxError: {e}")
        except Exception as e:
            output.write(f"Exception: {e}")

async def setup(bot):
    await bot.add_cog(Eval(bot))
