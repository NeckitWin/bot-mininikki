import disnake
from disnake.ext import commands

class Button(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def react(self, ctx):
        # Проверяем, что есть сообщение, на которое дан ответ
        if ctx.message.reference:
            referenced_message = await ctx.fetch_message(ctx.message.reference.message_id)
            guild = self.bot.get_guild(984079879802876035)  # ID вашего сервера
            emoji = await guild.fetch_emoji(1059584089549717614)  # ID вашей реакции
            if emoji:
                # Устанавливаем реакцию под сообщением
                await referenced_message.add_reaction(emoji)
            else:
                await ctx.send("Реакция не найдена на вашем сервере.")
        else:
            await ctx.send("Ответьте на сообщение, чтобы установить реакцию.")

def setup(bot):
    bot.add_cog(Button(bot))
