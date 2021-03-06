import discord

from auth import setAuth
from discord.ext import commands
#https://gist.github.com/vbe0201/ade9b80f2d3b64643d854938d40a0a2d
from music import *

auth = setAuth()
token = auth[0]
prefix = auth[1]

banned_users = (0, 467518086262816769, 464930509101858826, 220250919093272576, 205557510256590848) #Trung has been banned.
debug = False

bot = commands.Bot(prefix, description='RoEW')
bot.add_cog(Music(bot))

#https://discordpy.readthedocs.io/en/latest/api.html#discord-models
#https://discordpy.readthedocs.io/en/latest/faq.html
#https://www.w3schools.com/python/python_ref_list.asp

@bot.event
async def on_ready():
    print(':mima:')
    print('Logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    pieces = message.content.split()
    cmd = pieces[0]

    if message.content.startswith(prefix) and debug:
        log_channel = bot.get_channel(541002881688666133)
        await log_channel.send(message.author.name + "#" + message.author.discriminator + ' used the ' + cmd + ' command in ' + message.guild.name + '.')
    
    if banned_users.count(message.author.id) == 0:
        await bot.process_commands(message)
    else:
        if message.content.startswith(prefix):
            print('Banned user ' + message.author.name + "#" + message.author.discriminator + ' tried to use the ' + cmd + ' command in ' + message.guild.name + '.')
        

class Mima(commands.Cog):

    @bot.command(name='xfis')
    async def _xfis(ctx, *, arg: str):
        """
        Wish's personal mischief function.
        """
        if ctx.author.id == 123211683052257280:
            await ctx.send(arg)
            await ctx.message.delete()
        else:
            await ctx.send('denied')
    
    @bot.command(name='mine')
    async def _mine(ctx, diff: str="lunatic"):
        """
        Sets up a game of minesweeper. (Old Meema functions under reconstruction.)
        """
        await ctx.send('under construction')
    
    @bot.command(name='update')
    async def _update(ctx, *, arg: str):
        """
        Updates/refreshes the bot.  Only usable by Wish.
        """
        if ctx.author.id == 123211683052257280:
            await ctx.send('Rebooting...')
            bot.close()
        else:
            await ctx.send('denied')
    
#bot.add_cog(Mima(bot))

bot.run(token)
