import discord 

from discord.ext import commands 



client = commands.Bot(command_prefix="!")

@client.command()
async def coucou(ctx):
    await ctx.send("COUCOU!!!")

@client.command()
async def super_coucou(ctx,arg1,arg2):
    await ctx.send(arg1+" -- "+arg2)

@client.event
async def on_message(message):
    message.content = message.content.lower()

    if message.author == client.user:
        return

    Help_channel = client.get_channel(978271940055797780)

    if message.channel == Help_channel and message.content.startswith('$help'):
        await Help_channel.send("Bonjour @"+message.author.name)
        await Help_channel.send("Pour pouvoir vous aider, veuillez choisir votre filière parmis les chois suivant :")
        await Help_channel.send("M - Master")
        await Help_channel.send("B - Bachelor")






    if message.content == "del":
        await message.channel.purge(limit=30)
    
    if message.content.startswith("$dm"): 
        user = message.mentions[0]
        strs = message.content.split(" ")
        await user.send(strs[2:])

    await client.process_commands(message)

@client.event
async def on_member_join(member):
    Help_channel = client.get_channel(978271940055797780)
    await Help_channel.send('Bonjour !' + member.display_name)

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

