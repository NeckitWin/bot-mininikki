import disnake
from disnake.ext import commands

class Kom(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot
        
        # await ctx.channel.purge(limit = 1) действие для удаления 1 сообщения.

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def очистить(self, ctx, amount: int):
        await ctx.channel.purge(limit = amount + 1)
        await ctx.send(f'Пользователь {ctx.author.mention} удалил {amount} сообщений!')
        
    @commands.command(usage='!кик <@пользователь> [причина]')
    @commands.has_permissions(kick_members=True)
    async def кик(self,ctx, member: disnake.Member, *, reason=None):
        await member.kick(reason=reason)
        embed=disnake.Embed(name='Пользователь был кикнут!', description=f'Пользователь {ctx.author.mention} кикнул пользователя {member.mention}\nПо причине: {reason}', color=ctx.author.color)
        await ctx.send(embed=embed)
        
    @commands.slash_command(name='ban',description='!бан <@пользователь> [причина]')
    @commands.has_permissions(ban_members=True)
    async def бан(self,ctx, member: disnake.Member, *, reason=None):
        await member.ban(reason=reason)
        embed=disnake.Embed(name='Пользователь был забанен!', description=f'Пользователь {ctx.author.mention} забанил пользователя {member.mention}\nПо причине: {reason}', color=ctx.author.color)
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(Kom(bot))