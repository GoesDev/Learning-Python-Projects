import discord
from discord.ext import commands
from random import randint

import Discord_Bot.VARIABLE as VARIABLE

permissions = discord.Intents.default()
permissions.message_content = True
permissions.members = True
bot = commands.Bot(command_prefix="-", intents=permissions)


@bot.command()
async def play(ctx: commands.Context):
    die = randint(1, 6)
    await ctx.send(f"Primeiro Dragão: **{die}**")


@bot.command()
async def m_help(ctx: commands.Context):
    await ctx.reply(VARIABLE.ALL_COMMANDS)


bot.run(VARIABLE.BOT)