import disnake
from disnake.ext import commands
import datetime


class Info(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot
        
    @commands.command(aliases=['help','помощь','хелп','info'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def инфо(self,ctx):
        embed = disnake.Embed(
            title='**Информация о боте**',
            description='Она сделает всё, что вы пожелаете!',
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
        
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def юзер(self, ctx, member: disnake.Member = None):
        if member is None:
            member = ctx.author
        banner_url = "Null"
        req = await ctx.bot.http.request(disnake.http.Route("GET", "/users/{uid}", uid=member.id))
        banner_id = req["banner"]
        if banner_id:
            banner_url = f"https://cdn.discordapp.com/banners/{member.id}/{banner_id}{'.gif' if'a_' in banner_id else '.png'}?size=1024"
        roles = [role for role in member.roles]
        embed = disnake.Embed(title=f"Информация о пользователе {member.name}",color=ctx.author.color)
        embed.set_thumbnail(url=member.avatar.url)
        if member.status == disnake.Status.online:
            embed.add_field(name="Статус пользователя:", value="🟢В сети", inline=False)
        elif member.status == disnake.Status.offline:
            embed.add_field(name="Статус пользователя:", value="⚪Не в сети", inline=False)
        elif member.status == disnake.Status.idle:
            embed.add_field(name="Статус пользователя:", value="🌙Не активен", inline=False)
        elif member.status == disnake.Status.dnd:
            embed.add_field(name="Статус пользователя:", value="🔴Не беспокоить", inline=False)
        embed.add_field(name="Роли:", value="\n".join(role.mention for role in roles), inline=True)
        embed.add_field(name="Высшая роль:", value=member.top_role.mention, inline=True)
        embed.add_field(name="Установленный ник на сервере:", value=member.display_name, inline=False)
        embed.add_field(name="ID пользователя:", value=member.id, inline=False)
        embed.add_field(name="Аккаунт создан:", value=member.created_at.strftime("Время: %H:%M:%S\nДата: %d.%m.%Y"), inline=True)
        embed.add_field(name="Присоединился на сервер:", value=member.joined_at.strftime("Время: %H:%M:%S\nДата: %d.%m.%Y"), inline=True)
        if member.bot==True:
            embed.add_field(name = "Пользователь", value='Бот🤖', inline=False)
        elif member.bot==False:
            embed.add_field(name = "Пользователь", value='Верифицирован ✅', inline=False)
        if banner_id:    
            embed.set_image(url=banner_url)
        embed.set_footer(text=f'Запрос от пользователя {ctx.author}')
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def сервер(self,ctx):
        all=len(ctx.guild.members)
        members = len(list(filter(lambda m: not m.bot, ctx.guild.members)))
        bots = len(list(filter(lambda m: m.bot, ctx.guild.members)))
        emoji = 0
        anim_emoji = 0
        for emojik in ctx.guild.emojis:
            if emojik.animated == True:
                anim_emoji += 1
            elif emojik.animated == False:
                emoji +=1
        online = 0
        idle = 0
        offline = 0
        dnd = 0
        #kanalbI
        text = 0
        voice = 0
        for member in ctx.guild.members:
            if str(member.status) == "online":
                online += 1
            if str(member.status) == "idle":
                idle += 1
            if str(member.status) == "dnd":
                dnd += 1
            if str(member.status) == "offline":
                offline += 1
        for channel in ctx.guild.channels:
            if str(channel.type) == "text":
                text+=1
            if str(channel.type) == "voice":
                voice+=1
        
        region=ctx.guild.region
        owner=ctx.guild.owner.mention
        
        embed = disnake.Embed(
            title='**Информация о сервере**',
            description='И как у нас тут делишки?)',
            color=ctx.author.color
        )
        embed.set_thumbnail(url=ctx.guild.icon.url)
        embed.add_field(name ="👥Всего пользователей: ", value=f"{all}", inline=False)
        embed.add_field(name ="😊Людей на сервере: ", value=f"{members}", inline=False)
        embed.add_field(name ="🤖Ботов на сервера: ", value=f"{bots}", inline=False)
        embed.add_field(name ="😀Эмодзи: ", value=f"{emoji}", inline=False)
        embed.add_field(name ="🤪Гиф-эмодзи: ", value=f"{anim_emoji}", inline=False)
        onl=online+dnd+idle
        embed.add_field(name ="🟢Онлайн пользователей: ", value=f"{onl}", inline=False)
        embed.add_field(name ="🔴Оффлайн пользователей: ", value=f"{offline}", inline=False)
        embed.add_field(name ="✉️Текстовые каналы: ", value=f"{text}", inline=False)
        embed.add_field(name ="📞Голосовые каналы: ", value=f"{voice}", inline=False)
        embed.add_field(name ="🌎Регион: ", value=f"{region}", inline=False)
        embed.add_field(name ="😈Владелец: ", value=f"{owner}", inline=False)
        embed.set_footer(text=f'Запрос от пользователя {ctx.author}')
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(Info(bot))