import discord 
from datetime import datetime

from discord.ext import commands 
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

docu=[
    Node("Tu peut acceder à la convention de stage 2021/2022 ici : https://assets.jobteaser.com/upload_file/uploads/Convention_de_Stage_2022_-_fran%C3%A7ais.3417430645.pdf","convention",[]),
    Node("T'on emploi du temps se trouve sur hyperplanningn si tu as oublié t'es codes envoi un mp à Brontis","emploi du temps",[]),
]
administration = [
    Node("Frais de scolarité ! Que souhaite tu savoir?","frais",[Node("Les frais de scolarités pour cette années s'élèvent à 7 500€","montant",[]),Node("Les modalitées de paiment sont indiquées sur t'on contrat d'inscription, si tu souhaite plus d'information je t'invite à te raprocher de la compta : compta@hetic.com","modalité",[]),]),
    Node("De quel document à tu besoin ?","document",docu)
]
stage = [
    Node("4 juillet ","date",[]),
    Node("envoi un mp à Brontis (@ErwinTheCat#8778)","offre",[]),
    Node("envoi un mp à Giuseppe (@Giuseppe#1810)","CV",[]),
    Node("Bravo ! envoi toute suite un mp à Brontis (@ErwinTheCat#8778) pour lui annoncer la bonne nouvelle, il te dira comment s'y prendre","trouvé",[]),
    docu[0]
]
alternance = [
    Node("1er année 2s/1s, 2eme année 3s/1s","rythme",[]),
    Node("debut octobre ","date",[]),
    Node("envoi un mp à Brontis (@ErwinTheCat#8778)","offre",[]),
    Node("envoi un mp à Giuseppe (@Giuseppe#1810)","CV",[]),
    Node("Bravo ! envoi toute suite un mp à Brontis (@ErwinTheCat#8778) pour lui annoncer la bonne nouvelle, il te dira comment s'y prendre","trouvé",[]),
    docu[0]
]
programation = [
    Node("DISCORD ! Voici une serie de petit tuto pour bien débuter avec les bots discord ","discord",[]),
    Node("BOUCLES ! Voici un tuto qui explique bien le fonctionnement des boucles ","boucle",[]),
    Node("FONCTIONS ! Voici un tuto pour mieux comprendre les fonctions en python ","fonction",[]),
    Node("CLASSES ! Voici un tuto pour mieux comprendre le fonctionnement des classes","classe",[]),
    Node("DICTIONNAIRES ! Voici un tuto pour mieux comprendre le fonctionnement des dictionnaires","dictionnaire",[]),
    Node("ARBRE ! Voici un tuto pour mieux comprendre le fonctionnement des arbres","arbre",[])
]
php = [
    Node("BOUCLES ! Voici un tuto qui explique bien le fonctionnement des boucles ","boucle",[]),
    Node("FONCTIONS ! Voici un tuto pour mieux comprendre les fonctions en php ","fonction",[]),
    Node("Variables ! Voici comment s'y prendre avec les variables en php","variable",[]),
    Node("Session ! Voici comment s'y prendre avec les session en php","session",[])
]
sql = [
    Node("PDO ! Voici  comment fonctionne la fonction PDO ","pdo",[]),
    Node("Insertion d'un element dans la base de donnée ! Voici comment s'y prendre ","insert",[]),
    Node("Selectionner un element dans la base de donnée ! Voici comment s'y prendre ","select",[]),
    Node("Metre a jour la base de donnée ! Voici comment s'y prendre ","update",[]),
    Node("Suprimer un element de la base donnée ! Voici comment s'y prendre ","delete",[])
]
back = [
    Node("PHP ! qu'est-ce qui vous pose problème plus précisément ?","php",php),
    Node("PYTHON ! qu'est-ce qui vous pose problème plus précisément ?","python",programation),
    Node("SQL ! qu'est ce qui vous pose problème plus précisément ?","sql",sql)
]
html = [
    Node("LES BALISES ! Voici un tuto qui explique bien le fonctionnement des balises html ","balises",[]),
    Node("LES HEADERS ! Voici un tuto pour mieux comprendre le fonctionnement du header ","header",[]),
    Node("LE BODY ! Voici un tuto pour mieux comprendre le fonctionnement du body de la page","body",[]),
    Node("LES FOOTERS ! Voici un tuto pour mieux comprendre le fonctionnement du footer","footer",[])
]
css = [
    Node("Rendre son site responsive ! Si t'a pas capté bien capté le cours voici un petit tuto qui le resume","responsive",[]),
    Node("GRID ! Pas encore famillier avec cette propriete ? Regarde cette vidéo elle va surement t'aider ","grid",[]),
    Node("Position ! Pas encore famillier avec cette propriete ? Regarde cette vidéo elle va surement t'aider","position",[]),
    Node("Le style du texte ! Tu veut savoir comment bien mairiser le style de t'es textes  ? vient voir par la :","text",[])
]
javascript = [
    Node("BOUCLES ! Voici un tuto qui explique bien le fonctionnement des boucles ","boucle",[]),
    Node("FONCTIONS ! Voici un tuto pour mieux comprendre les fonctions en js ","fonction",[]),
    Node("Variables ! Voici comment s'y prendre avec les variables en js","variable",[])
]
front = [
    Node("HTML ! qu'est-ce qui vous pose problème plus précisément ?","html",html),
    Node("CSS ! qu'est-ce qui vous pose problème plus précisément ?","css",css),
    Node("JAVASCRIPT ! qu'est ce qui vous pose problème plus précisément ?","javascript",javascript)
]
scrum = [
    Node("Le product owner","owner",[]),
    Node("le scrum master","master",[]),
    Node("Lz scrum team","team",[]),
    Node("Le sprint","sprint",[])
]
techno = [
    Node("Le reseau","reseau",[]),
    Node("l'ia","ia",[]),
    Node("Les email","email",[])
]
graphism=[
    Node("Indesign","indesign",[]),
    Node("Photoshop","photoshop",[]),
    Node("Illustrator","illustrator",[])
]
design=[
    Node("UI","ui",[]),
    Node("UX","ux",[]),
    Node("FIGMA","figma",[])
]
cours = [
    Node("Back-end ! Quel language ?","back",back),
    Node("Front-end ! Quel language ?","front",front),
    Node("Programation ! En première année tu aborde que python, dit qu'est ce qui ne va pas avec ce language ?","programation",programation),
    Node("Design ! Tu veut en savoir plus sur le logiciel FIGMA ou la théorie ui/ux","design",design),
    Node("Outils graphique ! quel logiciel (indesign, photoshop, illustrator)","graphique",graphism),
    Node("SCRUM ! Quel rôle t'interesse ?","scrum",scrum),
    Node("SGBDR ! Que veut tu savoir en sql ?","SGBDR",sql),
    Node("Technologie web ! De quoi à-tu besoin (une vidéo , un cours)","techno",techno)
]
first_list = [
    Node("Un cours ! Sur quel matière","cours",cours),
    Node("L'alternance ! Que veut tu savoir dessus ?","alternance",alternance),
    Node("Le stage ! Que veut tu savoir dessus ?","stage",stage),
    Node("Secraitariat ! De quoi à-tu besoin","Administration",administration)
]
first_node = Node("Salut !\nJe suis G-MEC, HETIC m'a engager afin d'apporter de l'aide et répondre à ses (nouveaux) étudiants en développement WEB.\nA tout moment tu peut ecrire '$info' pour comprendre mon fonctionnement.\nDit moi comment je peut t'aider ?","help",first_list)

current_node = first_node
#
@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    Help_channel = client.get_channel(978271940055797780)
    global current_node

    if message.channel == Help_channel and message.content =='$help':
        await Help_channel.send("@"+message.author.name)
        await Help_channel.send(first_node.question)

    for child in current_node.list_child_node:
        if child.keyword in message.content:
            await Help_channel.send(child.question)
            current_node = child
        

#ABOUT
@client.command()
async def info(ctx):
    print("ok")
    await ctx.send("info :\nComment je fonctionne?\nJe dirige la discussion et je repère les mots clèfs pour répondre le plus précisement.\nLes commandes possibles : \n$help -> démarrer une nouvelle discussion (uniquement sur le chanel 'G-SHAME help').\n$clear nb -> supprimer des messages (nb=nombre de message à supprimer).\n$server -> afficher les information relative au serveur.\n$date -> afficher la date.\n$heure -> afficher l'heure'.")

#Heure
@client.command()
async def heure(ctx):
    await ctx.send(datetime.now().strftime('%H:%M:%S'))

#Date
@client.command()
async def date(ctx):
    await ctx.send(datetime.now().strftime('%d-%m-%Y'))

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


