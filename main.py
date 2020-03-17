import discord
from discord.ext import commands
from symptomCheckerClientDemo import SymptomCheckerClientDemo

client = commands.Bot(command_prefix = '.')
symptomChecker = SymptomCheckerClientDemo()

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    print(f'{member} has join a server')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong ! {round(client.latency * 1000)}ms')

@client.command(aliases = ['diag'])
async def diagnosis(ctx, *, question)
    bodyLocations = symptomChecker._diagnosisClient.loadBodyLocations()
    # response = "This features will be implemented later"
    await ctx.send(f'{bodyLocations}')

client.run('Njg4MzA2ODMwNTY0MjYxOTMw.Xm4SZw.71Fk1Kc1mBMeQp47hZlM3HAZ1aw')
