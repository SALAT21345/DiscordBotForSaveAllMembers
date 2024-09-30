import discord
from discord.ext import commands
import json

# Настраиваем intents для доступа к участникам сервера и сообщениям
intents = discord.Intents.default()
intents.members = True  # Доступ к членам сервера
intents.message_content = True  # Доступ к содержимому сообщений

# Создаем объект бота с префиксом для команд
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f'Бот {bot.user} запущен и готов к работе!')


# Команда для записи участников сервера в json
@bot.command()
async def save_members(ctx):
    members = []

    # Перебираем всех участников сервера
    for member in ctx.guild.members:
        members.append({
            "name": member.name,
            "id": member.id,
            "discriminator": member.discriminator,
            "bot": member.bot
        })

    # Записываем список участников в JSON файл
    with open('members.json', 'w', encoding='utf-8') as f:
        json.dump(members, f, ensure_ascii=False, indent=4)

    await ctx.send(f'Список участников сервера был успешно сохранен в members.json')


# Запускаем бота
bot.run('')
