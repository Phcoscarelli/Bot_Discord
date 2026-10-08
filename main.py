import discord 
from discord.ext import commands

intets = discord.Intents.all() 
bot = commands.Bot(".", intents=intets)

audio = "/home/phcoscarelli/Downloads/audio/Treta Axt e Skipnho - A Gente não é um Time？ 16⧸01⧸2018.mp3"


@bot.command()
async def eai(ctx:commands.Context):
    nome = ctx.author.display_name
    await ctx.send(f"não, eai não, {nome}! a gente não é um time ?")

@bot.command()
async def xiu(ctx:commands.Context):
    nome = ctx.author.display_name
    await ctx.send("xiu é o caralho")

@bot.command()
async def play(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        voice_client = await channel.connect()
    try:
        source = discord.FFmpegPCMAudio(audio)
        voice_client.play(source, after=lambda e: print("Reprodução concluída.", e))
    except Exception as e:
        await ctx.send(f"Erro ao tocar o arquivo: {e}")
        print(e)


@bot.command()
async def sai(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Seu merda")




bot.run("")
