import discord
from discord.ext import commands
from random import randint

import VARIABLE

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


@bot.event
async def on_message(msg: discord.Message):
    await bot.process_commands(msg)
    autor = msg.author
    if autor.bot:
        return
    # await msg.reply("Olá, sou a Marriene, um BOT para a Guilda Velho Dragão")


bot.run(VARIABLE.BOT)
