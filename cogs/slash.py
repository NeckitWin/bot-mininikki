import disnake
from disnake.ext import commands

class Slashx(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot

    @commands.slash_command(description="Это команда, чтобы увидить аватар определённого пользователя.")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ava(self,ctx,member: disnake.Member):
        embed=disnake.Embed(title="Аватар пользователя:", color=ctx.author.color)
        embed.set_image(url=member.avatar)
        await ctx.send(embed=embed)
    # аватар
    @commands.slash_command(description="Эта команда отображает баннер пользователя Discord")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def banner(self, ctx, member: disnake.Member):
        banner_url = "Null"
        req = await ctx.bot.http.request(disnake.http.Route("GET", "/users/{uid}", uid=member.id))
        banner_id = req["banner"]
        if banner_id:
            banner_url = f"https://cdn.discordapp.com/banners/{member.id}/{banner_id}{'.gif' if 'a_' in banner_id else '.png'}?size=1024"
            embed = disnake.Embed(title="Баннер пользователя:",description=f"{member.mention}", color=ctx.author.color)
            embed.set_image(url=banner_url)
            await ctx.send(embed=embed)
        else:
            embed = disnake.Embed(title="Цвет баннера", description=f"{member.mention} имеет цвет баннера: {ctx.member.color}", color=ctx.author.color)
            await ctx.send(embed=embed)

    #баннер
    @commands.slash_command(description="Команда для помощи по боту.")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def help(self,ctx):
        embed=disnake.Embed(
                title='**Информация о боте**',
                description='Она сделает вам всё, что вы пожелаете!',
                color=ctx.author.color
            )
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url=ctx.guild.icon.url)
        embed.add_field(name = "Информационные команды:", value='**!инфо | !юзер | !сервер**', inline=False)
        embed.add_field(name = "Слеш команды:", value='**/help | /ava | /creatembed**', inline=False)
        embed.add_field(name = "Команды для администрации:", value='**!мут | !бан | !очистить**', inline=False)
        embed.add_field(name = "Кастомные команды:", value='**Действие**\n!плакать | !танцевать | !непон\n**Действие с другим пользователем**\n!кусь | !цем | !ударить | !секс \n !облизать | !обнять', inline=False)
        embed.add_field(name = "Полезные команды:", value='**Вытащить изображение из стикера**\n!стикер', inline=False)
        embed.set_image(url='https://aniyuki.com/wp-content/uploads/2022/08/aniyuki-anime-eyes-31.gif')
        embed.set_footer(text='Количество серверов бота: ' + str(len(ctx.bot.guilds)))
        await ctx.send(embed=embed)

    @commands.slash_command(description="Команда для проверки пинга")
    @commands.cooldown(1,5,commands.BucketType.user)
    async def ping(self,inter: disnake.ApplicationCommandInteraction):
        embed=disnake.Embed(
            title='Понг',
            color=inter.author.color
        )
        await inter.send(embed=embed, ephemeral=True)

    @commands.slash_command(description="Создание эмбета. 1) Загаловок 2) Описание 3) Изображение/гиф[необязательно]")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def creatembed(self,ctx,title,description,link:str=''):
        embed=disnake.Embed(title=f"{title}", description=f"{description}", color=ctx.author.color)
        embed.set_image(url=f"{link}")
        await ctx.send(embed=embed)

    @commands.slash_command(description="Команда для очистки сообщений. Доступна для участников с правами управления сообщениями")
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit = amount + 1)
        await ctx.send(f'Пользователь {ctx.author.mention} удалил {amount} сообщений!')

def setup(bot):
    bot.add_cog(Slashx(bot))