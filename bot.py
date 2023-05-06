import disnake
from disnake.ext import commands
from disnake.enums import ButtonStyle
import os

bot = commands.Bot(command_prefix="!", help_command=None, intents=disnake.Intents.all())

@bot.event
async def on_ready():
    print('Я успешно запустилась!')
    await bot.change_presence(status = disnake.Status.dnd, activity = disnake.Activity(name=f'/help',type=disnake.ActivityType.watching))
#бот успешно загрузился

#загрузка кога
@bot.slash_command(description="Выгрузка определённого кога. Доступна только создателю и разрабам бота.")
@commands.has_role(993270145302667307)
async def unload(ctx,extencion):
    extencion=extencion.lower()
    bot.unload_extension(f'cogs.{extencion}')
    await ctx.send(f'{extencion}выгружен')
#отгрузка кога
for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and not filename.startswith("_"):
        bot.load_extension(f"cogs.{filename[:-3]}")
#Загрузка когов
bot.run('')