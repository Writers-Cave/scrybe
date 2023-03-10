import discord
import os
from dotenv import load_dotenv

bot = discord.Bot()

# register cogs in ./cogs dir
exts_to_load = len([fn for fn in os.listdir('../src/cogs') if fn.endswith('.py')])

for i, fn in enumerate(os.listdir('../src/cogs')):
    if fn.endswith('.py'):
        bot.load_extension(f'cogs.{fn[:-3]}')
        print(f"loaded {fn} - {(i+1)/exts_to_load*100}% - {i+1} of {exts_to_load} completed")

load_dotenv()
bot.run(os.getenv("BOT_TOKEN"))
