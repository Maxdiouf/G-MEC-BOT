import discord 
from datetime import datetime

from discord.ext import commands 
datetime.now().strftime('%H:%M')
client = commands.Bot(command_prefix="$")

class Node :
    def __init__(self,question,keyword,list_child_node):
        self.question = question
        self.keyword = keyword
        self.list_child_node = list_child_node

    def user_response(self):
        print(self.question)
        txt = input()
        for child in self.list_child_node:
            if child.keyword in txt:
                child.user_response()
administration = [
    Node("Frais de scolarité ! Les frais sont de 7500 €, qui peuvent etre payé en 7 mensulatées(avec frais)","frais",[]),
    Node("debut octobre ","date",[]),
    Node("envoi un mp a Brontis","offre",[]),
    Node("https://assets.jobteaser.com/upload_file/uploads/Convention_de_Stage_2022_-_fran%C3%A7ais.3417430645.pdf","convention",[])
]
stage = [
    Node("4 juillet ","date",[]),
    Node("envoi un mp a Brontis","offre",[]),
    Node("https://assets.jobteaser.com/upload_file/uploads/Convention_de_Stage_2022_-_fran%C3%A7ais.3417430645.pdf","convention",[])
]
alternance = [
    Node("1er année 2s/1s, 2eme année 3s/1s","rythme",[]),
    Node("debut octobre ","date",[]),
    Node("envoi un mp a Brontis","offre",[]),
    Node("https://assets.jobteaser.com/upload_file/uploads/Convention_de_Stage_2022_-_fran%C3%A7ais.3417430645.pdf","convention",[])
]
cours = [
    Node("Back-end ! Quel language ?","back",[]),
    Node("Front-end ! Quel language ?","front",[]),
    Node("Programation ! Quel language ?","programation",[]),
    Node("Design ! Tu veut en savoir plus sur le logiciel FIGMA ou la théorie","design",[]),
    Node("Outils graphique ! quel logiciel (indisign, photoshop, illustrator)","graphique",[]),
    Node("Shell Unix ! De quoi à-tu besoin (un tuto , un cours)","shell",[]),
    Node("Prise de parol ! De quoi à-tu besoin (un tuto , un cours)","prise de parole",[]),
    Node("SCRUM ! De quoi à-tu besoin (un tuto , un cours)","scrum",[]),
    Node("SGBDR ! De quoi à-tu besoin (un tuto , un cours)","SGBDR",[]),
    Node("Technologie web ! De quoi à-tu besoin (une vidéo , un cours)","techno",[])
]
first_list = [
    Node("Un cours ! Sur quel matière","cours",cours),
    Node("L'alternance ! Que veut tu savoir dessus ?","alternance",alternance),
    Node("Le stage ! Que veut tu savoir dessus ?","stage",stage),
    Node("Secraitariat ! De quoi à-tu besoin","Administration",administration)
]
first_node = Node("Salut !\nJe suis G-SHAME, HETIC m'a engager afin d'apporter de l'aide et répondre à ses (nouveaux) étudiants en développement WEB.\nA tout moment tu peut ecrire '$info' pour comprendre mon fonctionnement.\nDit moi comment je peut t'aider ?","help",first_list)


#
@client.event
async def on_message(message):
    global start
    start = False

    message.content = message.content.lower()
    if message.author == client.user:
        return

    Help_channel = client.get_channel(978271940055797780)
    if message.channel == Help_channel and message.content =='$help':
        await Help_channel.send("@"+message.author.name)
        await Help_channel.send(first_node.question)

    for i in range(len(first_node.list_child_node)):
        print(i)
        if first_node.list_child_node[i].keyword in message.content:
            print("ok")
            await Help_channel.send(first_node.list_child_node[i].question)

    await client.process_commands(message)

#ABOUT
@client.command()
async def info(ctx):
    await ctx.send("ABOUT :")
    await ctx.send("Comment je fonctionne?")
    await ctx.send("Je dirige la discussion et je repère les mots clèfs pour répondre la plus précisement.")
    await ctx.send("Les commandes possibles : ")
    await ctx.send("$help -> démarrer une nouvelle discussion (uniquement sur le chanel 'G-SHAME help').")
    await ctx.send("$clear nb -> supprimer des messages (nb=nombre de message à supprimer).")
    await ctx.send("$server -> afficher les information relative au serveur.")
    await ctx.send("$date -> afficher la date.")
    await ctx.send("$heure -> afficher l'heure'.")

#Heure
@client.command
async def heure():
    await client.send(datetime.now().strftime('%H:%M:%S'))

#Date
@client.command
async def date():
    await client.send(datetime.now().strftime('%d-%m-%Y'))
#nouveau membre
@client.event
async def on_member_join(member):
    Help_channel = client.get_channel(978271940055797780)
    await Help_channel.send('Bonjour !' + member.display_name + 'bienvenu sur G-SHAME.')


#CLEAR
@client.command()
async def clear(ctx, nombre : int):
    messages = await ctx.channel.history(limit = nombre+1).flatten()
    for message in messages :
        await message.delete()


#SERVER
@client.command()
async def server(ctx):
    name = ctx.guild.name
    description = ctx.guild.description
    owner = ctx.guild.owner
    id = ctx.guild.id
    region = ctx.guild.region
    member_count = ctx.guild.member_count
    icon = ctx.guild.icon_url

    embed = discord.Embed(
        title = name ,
        description = description,
        color = discord.Color.red()
    )
    embed.set_thumbnail(url = icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server Id", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=member_count, inline=True)

    await ctx.send(embed = embed)

client.run("OTc4MjI5MTgwMjc5OTUxMzYw.Gz91wd.5qmKnbDlQo97EjLlPl6urguX2Fj0L1pEmpd3DA")


