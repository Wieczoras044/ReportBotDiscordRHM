import os

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

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


#Uprawienia są pod osoby mające możliwość banowanie, na obecną chwile nie mam moderatorów dlatego uważałem to za zbędne.
@Client.command()
@commands.has_permissions(ban_members = True)
async def mute(ctx, user:discord.Member, time:int):
    await user.edit(mute=True)
    await asyncio.sleep(time)
    await user.edit(mute=False)
        
@Client.command()
@commands.has_permissions(ban_members = True)   
async def unmute(ctx, user:discord.Member):
    await user.edit(mute=False)



@Client.command()
@commands.has_permissions(ban_members = True)  
async def kick(ctx, user:discord.Member,time:int):
    await user.edit(voice_channel = None)
    await user.add_roles(discord.utils.get(user.guild.roles, name='Kick'))
    await asyncio.sleep(time)
    await user.remove_roles(discord.utils.get(user.guild.roles, name='Kick'))

@Client.command()
@commands.has_permissions(ban_members = True)  
async def ban(ctx, user:discord.Member,time:int):
    await user.edit(voice_channel = None)
    await user.add_roles(discord.utils.get(user.guild.roles, name='Kick'))
    time = time * 60
    await asyncio.sleep(time)
    await user.remove_roles(discord.utils.get(user.guild.roles, name='Kick'))

@Client.command()
@commands.has_permissions(ban_members = True)  
async def unban(ctx, user:discord.Member,time:int):
    await user.remove_roles(discord.utils.get(user.guild.roles, name='Kick'))






Client.run(os.environ['DISCORD_TOKEN'])
