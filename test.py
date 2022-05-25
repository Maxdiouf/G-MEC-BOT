import discord
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select
import discord.ext.commands as commands

client = commands.Bot("!")
DiscordComponents(client)

@client.command()
async def hello(ctx):
    await ctx.send("Bonjour @"+ctx.author.name)
    await ctx.send("Pour pouvoir vous aider, veuillez choisir votre filière parmis les choix suivant :", components = [
        [Button(label="Grande école", style="1", custom_id="GrandeEcole"), Button(label="Master", style="1", custom_id="master"), Button(label="Prépa", style="1", custom_id="prepa"), Button(label="Bachelor", style="1", custom_id="bachelor")]
        ])

@client.command()
async def ge(ctx):
    #grande ecole
    interaction_grande_ecole = await client.wait_for("button_click", check = lambda i: i.custom_id == "GrandeEcole")
    await interaction_grande_ecole.send("Faire un choix :", components = [
        [Button(label="Grande école", style="4", custom_id="ok")]
        ])

@client.command()
async def master(ctx):
    #master
    interaction_master = await client.wait_for("button_click", check = lambda i: i.custom_id == "master")
    await interaction_master.send("choisissez votre master :", components = [
        [Button(label="Marketing digital & UX", style="1", custom_id="marketdigit"), Button(label="Data & IA", style="1", custom_id="data"), Button(label="CTO & tech lead", style="1", custom_id="cto"), Button(label="Product manager", style="1", custom_id="po"), Button(label="Cybersécurité", style="1", custom_id="cyber") , Button(label="Design tech", style="1", custom_id="design") , Button(label="Métaverse & univers virtuel", style="1", custom_id="meta")]
        ])

@client.command()
async def prepa(ctx):
        #prepa
    interaction_master = await client.wait_for("Faire un choix", check = lambda i: i.custom_id == "prepa")
    await interaction_master.send("choisissez votre formation :", components = [
        [Button(label="Grande école", style="4", custom_id="ko")]
        ])

@client.command()
async def bachelor(ctx):
    #bachelor
    interaction_bachelor = await client.wait_for("button_click", check = lambda i: i.custom_id == "bachelor")
    await interaction_bachelor.send("choisissez votre formation :", components = [
        [Button(label="Developpeur Web", style="1", custom_id="devweb"), Button(label="Data & IA", style="1", custom_id="dataia"), Button(label="3D", style="1", custom_id="3d"), Button(label="WebMarketing & UX", style="1", custom_id="marketux")]
        ])

@client.command()
async def select(ctx):
    await ctx.send("Select", components = [
        Select(
            placeholder = "Select something!",
            options = [
                SelectOption(label="A", value="A"),
                SelectOption(label="B", value="B")
            ]
        )
    ])

    while True:
        try:
            select_interaction = await client.wait_for("select_option")
            await select_interaction.send(content = f"{select_interaction.values[0]} selected!", ephemeral = False)
        except:
            await ctx.send("urmom")
    

client.run('OTc4MjI5MTgwMjc5OTUxMzYw.Gz91wd.5qmKnbDlQo97EjLlPl6urguX2Fj0L1pEmpd3DA')