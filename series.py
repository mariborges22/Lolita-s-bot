import discord
import  discord.ext.commands as commands

bot=commands.Bot(command_prefix='!')
#Comando para criar a embed interativa com o usuário
@bot.command()
async def séries(ctx):

    embed=discord.Embed(title='Séries mais populares do canal',description='Escolha a série que você deseja (re)assistir')
    embed.set_image(url='https://i.gifer.com/Glhw.gif')
    embed.set_footer(text='Gif by GIFER', icon_url='https://i.gifer.com/Glhw.gif')
    embed.add_field(name='Valentona da Escola',value="link da série",inline=False)
    embed.add_field(name='Yandere da Escola',value="link da série",inline=False)
    embed.add_field(name="Para mais séries:",value='link do canal com mais opções de séries',inline=False)

    message = await ctx.send(embed=embed)
    reactions = ['\U0001F44D', '\U0001F44E','\u2764','\u2b50']

    for reaction in reactions:
        await message.add_reaction(reaction)




bot.run(token)