import discord
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select
import discord.ext.commands as commands
bot = commands.Bot("!")
DiscordComponents(bot)

@bot.event
async def on_ready():
    print("ready !")

@bot.command()
async def hello(ctx):
    await ctx.send("Bonjour @"+ctx.author.name)
    await ctx.send("Pour pouvoir vous aider, veuillez choisir votre filière parmis les choix suivant :", components = [
        [Button(label="Grande école", style="1", custom_id="GrandeEcole"), Button(label="Master", style="1", custom_id="master"), Button(label="Prépa", style="1", custom_id="prepa"), Button(label="Bachelor", style="1", custom_id="bachelor")]
        ])

@bot.command()
async def coucou(ctx):
    print("coucou")
    await ctx.send("Coucou !")

@bot.command()
async def serverInfo(ctx):
    server = ctx.guild
    serverName = server.name
    numberOfTextChannels = len(server.text_channels)
    numberOfVoiceChannels = len(server.voice_channels)
    serverDescription = server.description
    numberOfPerson = server.member_count
    message = f"Le server **{serverName}** contient {numberOfPerson} personnes. \n La description du serveur {serverDescription}. \n Ce serveur possède {numberOfTextChannels} salons écrit ainsi que {numberOfVoiceChannels} vocaux."
    await ctx.send(message)

@bot.command()
async def say(ctx, *texte):
    print(texte)
    await ctx.send(" ".join(texte))

@bot.command()
async def clear(ctx, nombre : int):
    messages = await ctx.channel.history(limit = nombre+1).flatten()
    for message in messages :
        await message.delete()

@bot.command()
async def kick(ctx, user : discord.User, *raison):
    raison = " ".join(raison)
    await ctx.guild.kick(user, raison = raison)
    await ctx.send(f"{user} à été kick.")

@bot.command()
async def ban(ctx, user : discord.User, *raison):
    raison = " ".join(raison)
    await ctx.guild.ban(user, raison=raison)
    await ctx.send(f"{user} à été ban pour la raison suivante : {raison}")

@bot.command()
async def unban(ctx, user, *raison):
    raison = " ".join(raison)
    userName, userId = user.split("#")
    bannedUser = await ctx.guild.bans()
    for i in bannedUser:
        if i.user.name == userName and i.user.id == userId:
            ctx.guild.unban(i.user, raison = raison)
            await ctx.send(f"{user} à été unban" )
            return
    await ctx.send("l'utilisateur que vous chercher n'est pas disponnible.")

@bot.command()
async def cuisiner(ctx):
	await ctx.send("Envoyez le plat que vous voulez cuisiner")

	def checkMessage(message):
		return message.author == ctx.message.author and ctx.message.channel == message.channel

	try:
		recette = await bot.wait_for("message", timeout = 10, check = checkMessage)
	except:
		await ctx.send("Veuillez réitérer la commande.")
		return
	message = await ctx.send(f"La préparation de {recette.content} va commencer. Veuillez valider en réagissant avec ✅. Sinon réagissez avec ❌")
	await message.add_reaction("✅")
	await message.add_reaction("❌")


	def checkEmoji(reaction, user):
		return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")

	try:
		reaction, user = await bot.wait_for("reaction_add", timeout = 10, check = checkEmoji)
		if reaction.emoji == "✅":
			await ctx.send("La recette a démarré.")
		else:
			await ctx.send("La recette a bien été annulé.")
	except:
		await ctx.send("La recette a bien été annulé.")


bot.run('OTc4MjI5MTgwMjc5OTUxMzYw.Gz91wd.5qmKnbDlQo97EjLlPl6urguX2Fj0L1pEmpd3DA')