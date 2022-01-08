import discord
from discord.ext import commands
from discord.utils import get
import asyncio
from random import randint

bot = commands.Bot(command_prefix='!')
sauces = 0
timerSauce = 30

@bot.event
async def on_ready():
    print("Bot pret !")
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game("PANTSU!!!"))


@bot.event
async def on_member_join(member):
    await member.add_roles(765591416461983755)


#Padoru song
@bot.command()
async def padoru(ctx, j=None):
    if j:
        padoru = ["走れそりよ", "風の用に", "付き三原を", "**パドルパドル**"]
    else:
        padoru = ["HASIRE SORI YO", "KASE NO YOU NI", "TSUKIMIHARA WO", "**PADORU PADORU**"]
    print(padoru[0])
    for pdru in range(len(padoru)):
        await ctx.send(padoru[pdru])
        await asyncio.sleep(delay=1.5)
    await ctx.send(file=discord.File('padoru.png'))

#Sauce random
@bot.command()
async def srand(ctx):
    if ctx.channel.id != 773607649567965194:
        await ctx.send("Pas ici petit lapin !")
        return
    
    global sauces
    global timerSauce

    print("sauce en cours : ", sauces)
    if not ctx.message.author.guild_permissions.administrator:
        if sauces == 5:
            await ctx.send("T'as déjà de quoi faire pour l'instant !")
            await asyncio.sleep(delay=timerSauce)
            await ctx.send("C'est bon, tu peux me réutiliser!")
            sauces = 0
            return

        sauces += 1

    sauce = randint(10000, 360000)
    print(sauce)
    await ctx.send(f"SAUCE ALEATOIRE : https://nhentai.net/g/{sauce} (si t'as de la chance elle est bonne!)")

#Clear chat
@bot.command()
async def c(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"Adieu ! Chers {amount} messages !")
    await asyncio.sleep(delay=4)
    await ctx.channel.purge(limit=1)

#NICO
@bot.command()
async def nico(ctx, c=None):
    await ctx.send(file=discord.File('NICONICONII.gif'))
    await asyncio.sleep(delay=1.5)
    for i in range(2):
        await ctx.send("NICO")
        await asyncio.sleep(delay=1)
    await ctx.send("NIIIIIIIIIII")
    if c:
        await asyncio.sleep(delay=0.5)
        await ctx.send(file=discord.File('nicoTruck.gif'))


#MAELLE C LA BEST
@bot.command()
async def mlb(ctx):
    for member in bot.get_all_members():
        print(member)
        #await member.send("TEST - ignore moi ou prévient moi (pas le bot mais moi tuks) si tu le reçoit comme tu veux")


#Commande help
@bot.command()
async def h(ctx):
    await ctx.send(
        "Listes des ordres que tu peux me donner (car je suis très exigeante) :\n"
        "- c {nbr} : clear 'nbr' msg dans le chat\n"
        "- padoru : chante une très belle chanson (+option 'j' jap)\n"
        "- srand : je te donne un numéro et si ça marche tu devient une vache.\n"
        "- nico : ba nico (+mention spéciale 'c' au camion)"
    )

#erreur cmd
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"Y'a une erreur là: ({str(error)})\nTape - !h - pour voir mes commandes !")    




token = "ask me for this"

print("Lancement du bot...")
bot.run(token)
