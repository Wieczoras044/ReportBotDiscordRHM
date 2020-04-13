import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot

Client = commands.Bot(command_prefix='$')

@Client.command()
async def pomoc(ctx):
    await ctx.send('$report <@(osoba)>, <skarga>.')

@Client.command()
async def report(ctx, *arg):
    await ctx.channel.purge(limit=1)
    tekst = ''
    for item in arg:
        tekst = tekst + ' ' + str(item)
    skargi = Client.get_channel(697108237388087448)
    await skargi.send(tekst)

@Client.command()
async def clear(ctx, arg):
    await ctx.channel.purge(limit=int(arg))





Client.run(os.environ['DISCORD_TOKEN'])
