import disnake
from disnake.ext import commands
import random

bite = [
    'https://media.tenor.com/5mVQ3ffWUTgAAAAC/anime-bite.gif?size=2048',
    'https://media.tenor.com/ECCpi63jZlUAAAAC/anime-bite.gif?size=2048',
    'https://media.tenor.com/mXc2f5NeOpgAAAAC/no-blood-neck-bite.gif?size=2048',
    'https://media.tenor.com/VXqink0UhmcAAAAi/bite.gif?size=2048',
    'https://media.tenor.com/4j3hMz-dUz0AAAAM/anime-love.gif?size=2048',
    'https://media.tenor.com/ECCpi63jZlUAAAAM/anime-bite.gif?size=2048',
    'https://media.tenor.com/6HhJw-4zmQUAAAAM/anime-bite.gif?size=2048',
    'https://media.tenor.com/48DDFOcNQBYAAAAM/anime-bite.gif?size=2048',
    'https://media.tenor.com/JEuY0WWcguIAAAAM/anime-bite.gif?size=2048',
    'https://media.tenor.com/aLeYKH2ebcoAAAAM/bite-hand.gif?size=2048'
]

kiss = [
    'https://media.tenor.com/QjMZ6Dx33_QAAAAM/kuss-kussi.gif?size=2048',
    'https://media.tenor.com/jnndDmOm5wMAAAAM/kiss.gif?size=2048',
    'https://media.tenor.com/4wUL9KIdlJAAAAAM/kiss.gif?size=2048',
    'https://media.tenor.com/DDmZqcOZJisAAAAM/anime.gif?size=2048',
    'https://media.tenor.com/NMBx4P4rHL8AAAAM/vanitas-no-carte-vanitas.gif?size=2048',
    'https://media.tenor.com/3xrkm45MqkIAAAAM/anime-kiss.gif?size=2048',
    'https://media.tenor.com/To_OGvH7UT4AAAAM/discord-top.gif?size=2048'
]

trax = [
    "https://media.tenor.com/Dx8XeOcQDpUAAAAM/gachi-gachi-muchi.gif",
    'https://media.tenor.com/Z0A3V-aC7T8AAAAM/gachi.gif',
    'https://media.tenor.com/Mb9DB6cucGYAAAAM/gachi.gif',
    'https://media.tenor.com/RNhkgQDsMdoAAAAM/bruh-what.gif',
    'https://media.tenor.com/BSYeNq2POsQAAAAM/gachimuchi.gif',
    'https://media.tenor.com/mkIlZ7OO0woAAAAM/gachi-%D1%8F%D0%BC%D0%B0%D1%82%D0%BE.gif'
]

beat = [
    'https://media.tenor.com/4p2gwNLsxBEAAAAM/whizzy-imposterfox.gif',
    'https://media.tenor.com/XiYuU9h44-AAAAAM/anime-slap-mad.gif',
    'https://media.tenor.com/M0Vi6oBi7RcAAAAM/ranma-akane-tendo.gif',
    'https://media.tenor.com/g_9NDHUmUdgAAAAM/anime.gif',
    'https://media.tenor.com/klNTzZNDmEgAAAAM/slap-hit.gif',
    'https://media.tenor.com/QszVFBEB4pAAAAAM/anime-grin.gif',
    'https://media.tenor.com/jDjvFwEX40QAAAAM/the-god-of-highschool-goh.gif',
    'https://media.tenor.com/UOSNzN8l-LkAAAAM/marumaru-seikatsu-spank.gif'
]

dance = [
    'https://media.tenor.com/Xg7QXqek2zkAAAAM/memes-anime.gif',
    'https://media.tenor.com/BgjMvz_ELtsAAAAM/anime-dance.gif',
    'https://media.tenor.com/d0ZjrEaLvHIAAAAM/anime-dance.gif',
    'https://media.tenor.com/uSilmq1xsdgAAAAM/netflix-netflix-show.gif'
]

cry = [
    'https://media.tenor.com/GFvNUbRLbm8AAAAM/supernatural-crying.gif',
    'https://media.tenor.com/pRTPXrxI2UAAAAAM/crying-meme-black-guy-cries.gif',
    'https://media.tenor.com/UIXwsWt9n9cAAAAM/crying-girl-crying.gif',
    'https://media.tenor.com/q9V98YHPZX4AAAAM/anime-umaru.gif',
    'https://media.tenor.com/0ZNy-QfbcBYAAAAM/anime.gif',
    'https://media.tenor.com/iSOANTCPvHYAAAAM/aestheic-black.gif'
]

nepon = [
    'https://media.tenor.com/HyMI_xkXHIIAAAAd/bebra.gif',
    'https://media.tenor.com/t70YMlLQ47YAAAAM/nipon.gif',
    'https://media.tenor.com/4nJQELh3_csAAAAM/i-dont-get-it-frustrated.gif',
    'https://media.tenor.com/6ufT60tjtj8AAAAM/i-dont-understand-i-dont-get-it.gif',
    'https://media.tenor.com/AmVuhEWlPPUAAAAM/confused-confusing.gif'
]

hug = [
    'https://media.tenor.com/gyiM68xD1MQAAAAM/anime-cute.gif',
    'https://media.tenor.com/sX_vDDaD2-4AAAAM/hug-anime.gif',
    'https://media.tenor.com/vp-9EqYmYGsAAAAM/anime-zertwo.gif',
    'https://media.tenor.com/8BqG6yTLCLEAAAAM/anime.gif'
]

lick = [
    'https://media.tenor.com/bN30aeLC0WMAAAAM/akeno-anime.gif',
    'https://media.tenor.com/FErgiOjRHOoAAAAM/redhead-girl.gif',
    'https://media.tenor.com/Vdse-phR5V0AAAAM/magialight-lick.gif',
    'https://media.tenor.com/3ZWnpdxhqOUAAAAM/lick.gif',
    'https://media.tenor.com/rWtIltahEoAAAAAM/kawaii-lick.gif',
    'https://media.tenor.com/nZxVjstzs5QAAAAM/anime-datealive.gif',
    'https://media.tenor.com/Go7wnhOWjSkAAAAM/anime-lick-face.gif'
]

class Custom(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def кусь(self, ctx, member: disnake.Member):
        embed=disnake.Embed(description=f"Пользователь {ctx.author.mention} больно укусил {member.mention}!",color=ctx.author.color)
        embed.set_image(url=random.choice(bite))
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ударить(self, ctx, member: disnake.Member):
        embed=disnake.Embed(description=f"Пользователь {ctx.author.mention} не сдержался и ударил {member.mention}!",color=ctx.author.color)
        embed.set_image(url=random.choice(beat))
        await ctx.send(embed=embed)
    
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def секс(self, ctx, member: disnake.Member):
        embed=disnake.Embed(description = f"Пользователь {ctx.author.mention} жоска отшпилил {member.mention}!",  color=ctx.author.color)
        embed.set_image(url=random.choice(trax))
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def плакать(self, ctx):
        embed=disnake.Embed(description=f"Пользователь {ctx.author.mention} плачет от боли((",color=ctx.author.color)
        embed.set_image(url=random.choice(cry))
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def цем(self, ctx, member: disnake.Member):
        embed=disnake.Embed(description=f"Пользователь {ctx.author.mention} нежно чмокнул {member.mention}...", color=ctx.author.color)
        embed.set_image(url=random.choice(kiss))
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def танцевать(self, ctx):
        embed=disnake.Embed(description=f"Пользователь {ctx.author.mention} затанцевал от счастья!", color=ctx.author.color)
        embed.set_image(url=random.choice(dance))
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def непон(self, ctx):
        embed=disnake.Embed(description=f"Пользователь {ctx.author.mention} ничего не понял...", color=ctx.author.color)
        embed.set_image(url=random.choice(nepon))
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def облизать(self, ctx, member: disnake.Member):
        embed=disnake.Embed(description = f"Пользователь {ctx.author.mention} лизнул {member.mention}!", color=ctx.author.color)
        embed.set_image(url=random.choice(lick))
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def обнять(self, ctx, member: disnake.Member):
        embed=disnake.Embed(description = f"Пользователь {ctx.author.mention} обнял со всей силы {member.mention}!", color=ctx.author.color)
        embed.set_image(url=random.choice(hug))
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Custom(bot))