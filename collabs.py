import discord
import  discord.ext.commands as commands

bot=commands.Bot(command_prefix='!')
#Comando para criar a embed interativa com o usuário
@bot.command()
async def collabs(ctx):

    embed=discord.Embed(title='Collabs mais populares do canal',description='Escolha a collab que você deseja (re)assistir')
    embed.set_image(url='https://i.gifer.com/g01Q.gif')
    embed.set_footer(text='Gif by GIFER', icon_url='https://i.gifer.com/g01Q.gif')
    embed.add_field(name='Realeza brigando por você',value="link da collab",inline=False)
    embed.add_field(name='Garotas brigando por você',value="link da collab",inline=False)
    embed.add_field(name="Irmãs adotivas",value="link da collab",inline=False)
    embed.add_field(name="Garotas paquerando você",value="link da collab",inline=False)
    embed.add_field(name="Festa de Halloween",value="link da collab")
    message = await ctx.send(embed=embed)
    reactions = ['\U0001F44D', '\U0001F44E', '\U0001F937','\u2764','\u2b50']
    #Laço de repetição para adicionar as reações embaixo da embed
    for reaction in reactions:
        await message.add_reaction(reaction)


bot.run(token)
