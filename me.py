import discord
import discord.ext.commands as commands

bot=commands.Bot(command_prefix="!")

@bot.command()
async def me(ctx,nome="ASMR LOLITA",idade=25,estado="SP",pais="BR",hardkills="Youtuber/writer",animefavorito="Toradora",canal="https://youtube.com/@asmrlolita",instagram='https://www.instagram.com/asmr_lolita/',tiktok="https://www.tiktok.com/@asmrlolita_?lang=pt-BR&is_from_webapp=1&sender_device=mobile&sender_web_id=7177059007311087110"):
    embed=discord.Embed(title='About me', color=0xff0000)
    embed.set_image(url='https://i.gifer.com/Bl62.gif')
    embed.set_footer(text='Gif by GIFER', icon_url='https://i.gifer.com/Bl62.gif')
    embed.add_field(name="Nome",value=nome)
    embed.add_field(name="Idade",value=idade)
    embed.add_field(name="Estado",value=estado)
    embed.add_field(name="País",value=pais)
    embed.add_field(name='Hard Kills',value=hardkills)
    embed.add_field(name='Anime favorito',value=animefavorito)
    embed.add_field(name="Canal no Youtube",value=canal)
    embed.add_field(name="Instagram",value=instagram)
    embed.add_field(name="Tiktok",value=tiktok)
   
    await ctx.send(embed=embed)
bot.run(token)