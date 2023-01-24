import discord

from AnilistPython import Anilist
import discord.ext.commands as commands
import random



bot=commands.Bot(command_prefix='!')

# Inicializar a classe Anilist
anilist = Anilist()

# Credenciais de acesso
anilist.client_id = "ID de acesso da API do Anilist"
anilist.client_secret = "Senha de acesso da API do Anilist"

generos_adultos = ["Hentai"]
# Criar comando para recomendação de anime
@bot.command()
async def recomendar(ctx):
    #Exportando animes do database do Anilist usando a liby AnilistPython

    results = anilist.get_anime_from_database(anime_name=' ')
    random_index = random.randint(0, len(results))
    anime = results[random_index]
    #Faz uma verfificação para restringir conteúdo adulto caso a escolha aleatória recaia nesse tipo de gênero
    for genero in anime["genres"]:
        if genero in generos_adultos:
            await ctx.send("Este anime é do gênero adulto e não será exibido na recomendação.")
            return

   #Caso não haja nenhum conteúdo restrito, exibe normalmente a embed com todas as informações do anime:Título,banner,descrição,status,duaração,formato,temporada,gêneros e nota
    embed = discord.Embed(title=anime["name_romaji"], color=0x00ff00,)
    embed.set_thumbnail(url=anime["banner_image"])
    embed.set_thumbnail(url=anime["cover_image"])
    embed.add_field(name="Descrição", value=anime["desc"])
    embed.add_field(name="Status", value=anime["airing_status"] )
    duration = anime.get("duration")
    if duration:
     embed.add_field(name="Duração", value=duration)
    embed.add_field(name='Quantidade de episódios',value=anime["airing_episodes"])
    embed.add_field(name='Formato',value=anime["airing_format"],)
    embed.add_field(name='Temporada', value=anime['season'])
    embed.add_field(name="Gêneros", value=", ".join(anime["genres"]))
    embed.add_field(name="Nota", value=anime["average_score"])
    await ctx.send(embed=embed)

bot.run(token do bot)
