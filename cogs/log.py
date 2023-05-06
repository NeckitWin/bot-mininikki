import disnake
from disnake.ext import commands

class Logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def стикер(self, ctx):
        """Извлекает стикер из ответного сообщения и отправляет его как изображение"""
        if ctx.message.reference is not None:
            message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
            if len(message.stickers) > 0:
                sticker = message.stickers[0]
                sticker_url = sticker.url
                embed = disnake.Embed(title="Извлеченный стикер", color=ctx.author.color)
                embed.set_image(url=sticker_url)
                await ctx.send(embed=embed)
            else:
                await ctx.send("Нет стикеров в ответном сообщении")
        else:
            await ctx.send("Пожалуйста, ответьте на сообщение, содержащее стикер")


def setup(bot):
    bot.add_cog(Logs(bot))