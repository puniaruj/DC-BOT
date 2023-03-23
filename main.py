import discord
from discord.ext import commands, tasks
import B
import os
key=os.getenv('key')

wkey=os.getenv('wkey')

client = discord.Client.intents()
client = commands.bot(command_prefix="(prefix)")
client.remove_command('help')
@client.command()
async def command(ctx):
    await ctx.send('This command was successful!')
  
@client.command() 
async def help(ctx):
    embed = discord.Embed(name="Help", value="help command", color=0xFFFFFF)
    
    embed.add_field(name="command", value="command description"  )
    await ctx.send(embed=embed)
B.b()
client.run(os.getenv('TOKEN'))