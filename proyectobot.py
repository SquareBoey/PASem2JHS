from sys import prefix
import discord
import random
from discord.ext import commands

client= commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("Getting ready"))
    print("bot is ready")
    print('Hliwis, ya regrese ')

@client.command()
async def ping(ctx):
    await ctx.send("pong!")

@client.command()
async def saludo(ctx):
    print("saludando al usuario")
    await ctx.send("Hola perro come mocos que tal todo")

@client.command(aliases=["8ball","bolita"])
async def _8ball(ctx, *,question):
    responses = ["It is certain.",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes - definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes.",
                    "Reply hazy, try again.",
                    "Ask again later.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def say(ctx, *,dile):
    await ctx.channel.purge(limit =1)
    await ctx.send(dile)

client.run('Token de su bot ')
