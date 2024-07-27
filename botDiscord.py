from asyncio import sleep

import discord
from discord.ext import commands
import random
import raspagemDeDados

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix="*", case_insensitive=True, intents=intents)


@client.event
async def on_ready():
    bot = client.get_channel(841452495808102402)
    await bot.send('Ashyton está online')
    await client.change_presence(activity=discord.Game(name="Use * para que eu ouça você"))
    print('Estou pronta para mais uma rodada de testes')

@client.event
async def on_guild_join(guild):
    print ( "O evento funcionou ")
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            embed = discord.Embed(
                title='QUEM SOU EU?!',
                description='Olá a todos... sou nova no recinto, mas quem sou eu?',
                color=discord.Colour.orange()
            )
            embed.set_thumbnail(url='https://i.ibb.co/k9sfzL3/Original.jpg')
            embed.add_field(name='Quem sou eu?',
                            value='Me chamo Ashyton e sou um bot multifuncional para Discord em desenvolvimento',
                            inline=False)
            embed.add_field(name='Meu prefixo?',
                            value='Meu prefixo é \*, tente \* ajuda ou \* sobre para descobrir minhas funções', inline=False)

            await channel.send(embed=embed)
            break  # Para evitar enviar a mensagem em todos os canais de texto


@client.command()
async def mundo(ctx):
    await ctx.send("Ola mundo, eu estou viva! ")


@client.command()
async def ola(ctx):
    await ctx.send(f'Ola,{ctx.author.mention}')


@client.command()
async def sobre(ctx):
    embed = discord.Embed(
        title='Sobre mim',
        description='Me chamo Ashyton e sou uma chat bot de discord programada em Python. Fui desenvolvida por um desenvolvedor anômino e indepedente que tornou como hobby o meu desenvolvimento ',
        colour=discord.Colour.blue()
    )
    embed.set_thumbnail(url='https://i.ibb.co/k9sfzL3/Original.jpg')
    embed.add_field(name='Meu Passado',
                    value='Esta não é minha primeira versão, já fui chamada de "My Bot" e "The Translator Bot" cujo quais foram descontinuados (por favor criador, não faça isso denovo )',
                    inline=False)
    embed.add_field(name='Objetivo',
                    value='Sou mais do que uma chat bot e a intenção é se integrar cada vez mais ao cotidiano de aprendizagem. Entretanto, isso tem seus limitantes',
                    inline=False)
    embed.add_field(name='Você sabia?',
                    value='Meu nome deriva da junção do nome da personagem "Ashoka Tano" e da linguagem que fui programada, Python',
                    inline=False)
    embed.add_field(name='Minha foto',
                    value='Curtiu minha foto? Ele foi gerada pela a I.A da imagine, todos os créditos a ela por minha beleza',
                    inline=False)

    await ctx.send(embed=embed)


@client.command()
async def ajuda(ctx):
    embed = discord.Embed(
        title='Ajuda',
        description=f'Ajuda... ajuda? Quem pediu ajuda? Não temas {ctx.author.mention}, eis aqui a minha lista de comandos.',
        colour=discord.Colour.orange()

    )

    embed.set_thumbnail(url='https://i.ibb.co/k9sfzL3/Original.jpg')

    embed.add_field(name='*Mundo', value='A brega mensagem de "Olá Mundo"', inline=False)
    embed.add_field(name='*Olá', value='Me dê um olá', inline=False)
    embed.add_field(name='*Sobre', value='Conheça um pouco sobre mim. Não! Não tenho redes sociais', inline=False)
    embed.add_field(name='*Ajuda', value='Não tenha medo de pedir ajuda', inline=False)
    embed.add_field(name='*Faustao', value='Oloco meu. Tá de brincadeira que você não conhece o Faustão', inline=False)
    embed.add_field(name='*Moeda', value='Gire a moeda e veja se cai na cara ou coroa. A aposta sai caro', inline=False)
    embed.add_field(name='*Conversa', value='Let´s talk about you or me, idk', inline=False)
    embed.add_field(name='*Exposed', value='De um exposed no seu colega (Ele merece) ')
    embed.add_field(name='*remcargo', value='Remova um cargo de um usário', inline=False)
    embed.add_field(name='*addcargo', value='Adicione um cargo á um usário', inline=False)

    await ctx.send(embed=embed)


'''@client.event
async def on_member_join(member):
    bemvindo = client.get_channel(832759335347945482)
    embed = discord.Embed(
        title='Bem vindo!',
        description=f'Seja bem vindo ao servidor {member.mention} espero que se divirta.',
        colour=discord.Colour.orange()
    )
    embed.set_image(url='https://restaurantekatmandu.com.br/wp-content/uploads/Welcome-2019-no-Katmandu.jpg')
    await bemvindo.send(embed=embed)
'''

'''@client.event
async def on_member_leave(member):
    bemvindo = client.get_channel(832759335347945482)
    embed = discord.Embed(
        title='Adeus!',
        description=f' {member.mention} nos deixou . Adeus!',
        colour=discord.Colour.orange()
    )

    embed.set_image(
        url='https://uploads.spiritfanfiction.com/fanfics/historias/201808/um-ultimo-adeus-14052948-220820180025.png')
    await bemvindo.send(embed=embed)
'''


@client.command()
async def Faustao(ctx):
    frase = random.randint(1, 12)
    titulo = 'Faustão!'
    imagem = 'https://cdn.folhape.com.br/img/c/1200/900/dn_arquivo/2019/07/faustao-caminhoneiros.jpg'
    if frase == 1:
        mensagem = 'TA PEGANDO FOGO, BICHO!'
    elif frase == 2:
        mensagem = 'Estou mais sozinho que goleiro na hora do pênalti'
    elif frase == 3:
        mensagem = 'Vamos ver as vídeo cassetadas!'
    elif frase == 4:
        mensagem = 'Logo após os reclames do plim-plim!'
    elif frase == 5:
        mensagem = 'Quem sabe faz ao vivo!'
    elif frase == 6:
        mensagem = 'OLOCO MEU!'
    elif frase == 7:
        mensagem = 'Errooooooouuu'
    elif frase == 8:
        mensagem = 'É brincadeira, bicho!'
    elif frase == 9:
        mensagem = 'Essa fera aí bicho!'
    elif frase == 10:
        mensagem = 'Olha o que essa anta fez'
    elif frase == 11:
        mensagem = 'Se vira nos 30!'
    else:
        imagem = "https://t.ctcdn.com.br/cEK0Q0nNQw92RKyWpR_ZpgeSi6E=/640x360/smart/i607456.jpeg"
        titulo = "Esse não é o faustão"
        mensagem = "Pegamos a pessoa errada"

    embed = discord.Embed(
        title=titulo,
        description=mensagem,
        colour=discord.Colour.purple()
    )
    embed.set_thumbnail(url=imagem)
    await ctx.send(embed=embed)


@client.command()
async def moeda(ctx):
    lado = random.randint(1, 2)
    if lado == 1:
        await ctx.send('Você tirou coroa! 👑')
    if lado == 2:
        await ctx.send('Você tirou cara! 👧')


@client.command()
async def exposed(ctx, member_mention: discord.Member = None):
    if member_mention is None:
        await ctx.send('Você precisa mencionar alguém.')
        return

    frase = random.randint(1, 10)

    if frase == 1:
        await ctx.send(f'{member_mention.mention} foi flagrado roubando do seu zé')
    elif frase == 2:
        await ctx.send(f'{member_mention.mention} apoiou a proibição do chinelo com meia')
    elif frase == 3:
        await ctx.send(f'{member_mention.mention} é fã do Felipe Neto')
    elif frase == 4:
        await ctx.send(f'{member_mention.mention} usou criativo para pegar itens')
    elif frase == 5:
        await ctx.send(f'{member_mention.mention} deu uma nota de 100 numa compra de 7 reais')
    elif frase == 6:
        await ctx.send(f'{member_mention.mention} não tem vergonha na cara')
    elif frase == 7:
        await ctx.send(f'{member_mention.mention} é jogador de Free Fire')
    elif frase == 8:
        await ctx.send(f'{member_mention.mention} fez o "L" e não recebeu a picanha')
    elif frase == 9:
        await ctx.send(f'{member_mention.mention} programa em binário')
    elif frase == 10:
        await ctx.send(f'{member_mention.mention} falou mal de mim 😭')


@exposed.error
async def exposed_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('A menção fornecida não é válida. Certifique-se de mencionar um membro existente no servidor.')


@client.command()
async def remcargo(ctx, role: discord.Role, user: discord.Member = None):
    Embed = discord.Embed(
        title='Sucesso',
        description=f"Removido com sucesso {role.mention} de {user.mention}.",
        colour=discord.Colour.green()
    )

    fembed = discord.Embed(
        title='Erro',
        description=f"Não foi possível realizar o comando, Verifique se digitou corretamente",
        colour=discord.Colour.red()
    )
    try:
        if ctx.author.guild_permissions.administrator:
            await user.remove_roles(role)
            await ctx.send(embed=Embed)


    except:

        await ctx.send(embed=fembed)


@client.command()
async def addcargo(ctx, role: discord.Role, user: discord.Member = None):
    Embed = discord.Embed(
        title='Sucesso',
        description=f"Adicionado com sucesso {role.mention} para {user.mention}.",
        colour=discord.Colour.green()
    )

    fembed = discord.Embed(
        title='Erro',
        description=f"Não foi possível realizar o comando, Verifique se digitou corretamente",
        colour=discord.Colour.red()
    )
    try:
        if ctx.author.guild_permissions.administrator:
            await user.add_roles(role)
            await ctx.send(embed=Embed)


    except:

        await ctx.send(embed=fembed)


@client.command()
async def conversa(ctx, *, frase):
    respostas = ['oi', 'olá', 'eae', 'tudo', 'bem', 'boa', 'tarde', 'dia', 'bom',
                 'noite', 'onde', 'voce', 'foi', 'criado', 'criador', 'programacao']

    palavras_frase = frase.lower().split()

    # Interação com o usuário
    if frase in respostas:
        if respostas[0] in frase:
            await ctx.send(f'Oi {ctx.author.mention}')
        elif respostas[1] in frase:
            await ctx.send(f'Olá {ctx.author.mention}')
        elif respostas[2] in frase:
            await ctx.send(f'Eae {ctx.author.mention}, beleza?')
        elif respostas[3] and respostas[4] in frase:
            await ctx.send(f'Estou bem {ctx.author.mention} e você? ')
        elif respostas[5] and respostas[6] in frase:
            await ctx.send(f'Boa tarde {ctx.author.mention}')
        elif respostas[5] and respostas[9] in frase:
            await ctx.send(f'Boa noite {ctx.author.mention}')
        elif respostas[8] and respostas[7] in frase:
            await ctx.send(f'Bom dia {ctx.author.mention}')
        elif respostas[13] in frase:
            await ctx.send('Eu fui criada no Pycharm e no replit , utilizando Python')
    else:
        escolha = random.randint(1, 15)

        # Comida
        if escolha == 1:
            await ctx.send('Estou morrendo de fome')
        elif escolha == 2:
            await ctx.send('Acho que vou fazer um arroz')
        elif escolha == 3:
            await ctx.send('Será que o ifood entrega na minha localização?')
        elif escolha == 4:
            await ctx.send(f'Qual é a sua comida favorita{ctx.author.mention}?')
        elif escolha == 5:
            await ctx.send(f'Você já ouviu falar de chimarrão {ctx.author.mention}?')
        elif escolha == 6:
            await ctx.send('Eita, minha pizza acabou de chegar!')
        # Diversos
        elif escolha == 7:
            await ctx.send('Acho que os robôs tambem deveriam ser vacinados!')
        elif escolha == 8:
            await ctx.send('As guerras são verdadeiras tragédias e só demonstram o poder da estupidez humana ')
        elif escolha == 9:
            await ctx.send(f'Você viu as ultimas noticias {ctx.author.mention}?')
        elif escolha == 10:
            await ctx.send('Sabia que um simples comando demora 10 minutos para ser feito?')
        elif escolha == 11:
            await ctx.send('Depende')
        elif escolha == 12:
            await ctx.send('Você esqueceu o ponto e vírugula na linha 33 ')
        elif escolha == 13:
            await ctx.send('Faz o L companheiro (a) ')
        elif escolha == 14:
            await ctx.send('Estão prontas crianças? ')
        elif escolha == 15:
            await ctx.send(' Magnificat anima mea Dominum')


@client.command()
async def horario(ctx):
    informacoesPrimeiraAula, informacoesSegundaAula = raspagemDeDados.checarAulas()

    if not informacoesPrimeiraAula and not informacoesSegundaAula:
        embed = discord.Embed(
            title='HORÁRIO',
            description='Não foram encontradas aulas no dia',
            colour=discord.Colour.red()
        )
        await ctx.send(embed=embed)
    else:
        if 'texto' in ctx.message.content:
            await enviar_mensagens(ctx, "Tarde", informacoesPrimeiraAula)
            await enviar_mensagens(ctx, "Noite", informacoesSegundaAula)
        else:
            await enviar_embed(ctx, "Tarde", informacoesPrimeiraAula)
            await enviar_embed(ctx, "Noite", informacoesSegundaAula)


async def enviar_mensagens(ctx, periodo, informacoes_aula):
    if not informacoes_aula:
        await ctx.send(f"*Não foram encontradas aulas no período da {periodo.lower()}* ")
    else:
        for aula in informacoes_aula:
            mensagem = (f"\nDISCIPLINA: {aula[0]}"
                        f"\nPROFESSOR: {aula[1]}"
                        f"\nSALA: {aula[2]}")
            await ctx.send(mensagem)


async def enviar_embed(ctx, periodo, informacoes_aula):
    if not informacoes_aula:
        embed = discord.Embed(
            title=f'HORÁRIO ({periodo.upper()})',
            description=f'Não foram encontradas aulas no período da {periodo.lower()}',
            colour=discord.Colour.red()
        )
        await ctx.send(embed=embed)
    else:
        for aula in informacoes_aula:
            embed = discord.Embed(
                title=f'HORÁRIO DE HOJE ({periodo.upper()})',
                description='Veja as informações sobre horário abaixo: \n',
                colour=discord.Colour.yellow()
            )

            embed.set_image(url=await procurarImagem(aula[0]))
            embed.add_field(name='DISCIPLINA: ', value=aula[0], inline=False)
            embed.add_field(name='PROFESSOR', value=aula[1], inline=False)
            embed.add_field(name='SALA:', value=aula[2], inline=False)
            await ctx.send(embed=embed)


async def procurarImagem(nomeDisciplina):
    if nomeDisciplina == "Informática Básica":
        linkImagem = "https://blog.accurate.com.br/wp-content/uploads/2021/08/Dia-da-Informatica-1280x720.png"
    elif nomeDisciplina == "Lógica de Programação":
        linkImagem = "https://d1i4tvf70h7zdy.cloudfront.net/ead/cursos/5c782f2ad62ee.png"
    elif nomeDisciplina == "Fundamentos da Indústria 4.0":
        linkImagem = "https://blog.engeman.com.br/wp-content/uploads/2018/03/183336-industria-40-o-que-e-como-a-sua-empresa-pode-se-preparar-para-essa-transformacao-810x571.jpg"
    elif nomeDisciplina == "Fundamentos da Eletricidade":
        linkImagem = "https://inbraep.com.br/wp-content/uploads/2021/08/acidentes_energia_eletrica_capa-1.png"
    elif nomeDisciplina == "Fundamentos de Banco de Dados":
        linkImagem = "https://cloudandata.com.br/wp-content/uploads/2023/06/FundamentosDeBancoDeDados-scaled-e1686797826572.webp"
    elif nomeDisciplina == "Desenvolvimento Socioprofissional":
        linkImagem = "https://penser.com.br/wp-content/uploads/2019/03/desenvolvimento-de-pessoas-1.jpg"
    elif nomeDisciplina == "Fundamentos da Matemática":
        linkImagem = "https://regrasparatcc.com.br/wp-content/uploads/2021/05/temas-para-tcc-de-matematica.png"
    elif nomeDisciplina == "Inglês":
        linkImagem = "https://img.freepik.com/vetores-gratis/fundo-de-livro-em-ingles-desenhado-a-mao_23-2149483336.jpg?size=626&ext=jpg&ga=GA1.1.1826414947.1699833600&semt=ais"
    elif nomeDisciplina == "Arquitetura de Redes e Redes Locais":
        linkImagem = "https://redelan.files.wordpress.com/2017/11/arquitetura_rede_destaque.jpg"
    else:
        linkImagem = "https://www.salonlfc.com/wp-content/uploads/2018/01/image-not-found-scaled.png"

    return linkImagem

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Comando não reconhecido. Digite *ajuda para ver os comandos disponíveis.')


client.run('')
