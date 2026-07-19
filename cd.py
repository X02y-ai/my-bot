import discord
from discord.ext import commands
import random

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "البوت يعمل الآن!"

def run():
  app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

import os
# احذف السطر الذي كتبت فيه التوكن يدوياً، واستبدله بهذا:
TOKEN = os.environ.get('DISCORD_TOKEN')

# تأكد من استخدام المتغير في أمر التشغيل:
bot.run(TOKEN)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None
)

hug_gifs = [
    "https://klipy.com/gifs/gilbert-pulls-violet-in-a-hug-violet-evergarden-gilbert-bougainvillea",
    "https://klipy.com/gifs/anime-comfort-hug-anime-hug",
    "https://klipy.com/gifs/haleys-ouo",
    "https://klipy.com/gifs/anime-cute-hug",
    "https://klipy.com/gifs/hug-anime-102",
    "https://klipy.com/gifs/shoval-anime",
    "https://klipy.com/gifs/chikako-hugging-otohime-for-the-first-and-she-confused",
    "https://klipy.com/gifs/anime-anime-hug-35",
    "https://klipy.com/gifs/cute-anime-bestie-hug"
]

slap_gifs = [
    "https://tenor.com/blgKM.gif",
    "https://tenor.com/rwKr4YXp8V1.gif",
    "https://klipy.com/gifs/anime-slap-mad-1",
    "https://klipy.com/gifs/boy-slap-girl-anime",
    "https://klipy.com/gifs/cat-angry-cat-22",
    "https://tenor.com/bnf3U.gif",
    "https://tenor.com/bFjvI.gif",
    "https://tenor.com/jWRmCvUb4Wu.gif",
    "https://tenor.com/jZ5VkuFc3jz.gif"
]

kill_gifs = [
    "https://klipy.com/gifs/whizzy-imposterfox-2",
    "https://tenor.com/jItzcdDTiss.gif",
    "https://tenor.com/tADeo3b18rI.gif",
    "https://tenor.com/bmJl8.gif",
    "https://tenor.com/yhMy.gif",
    "https://tenor.com/zafq.gif",
    "https://tenor.com/bypYi.gif"
]

kiss_gifs = [
    "https://tenor.com/D19A4LkpgG.gif",
    "https://tenor.com/sw04V4VKl72.gif",
    "https://tenor.com/oL9o7Am9EYi.gif",
    "https://tenor.com/eaJBn7UpGFt.gif",
    "https://tenor.com/b0RlL.gif",
    "https://tenor.com/poz2mv7uNwt.gif",
    "https://tenor.com/bLEYr.gif"
]

kick_gifs = [
    "https://tenor.com/beEJT.gif",
    "https://tenor.com/bsrjZ.gif",
    "https://tenor.com/blJ9I.gif",
    "https://tenor.com/bq7hv.gif",
    "https://tenor.com/cxCOSpUNq9u.gif",
    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXR3bWYxZ2t5d2o4Nnp3NzVwb3k4a2dpbnd4eXFxMTdnMjZjMGNkYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/sRYXGc13Mk9jHWfpBN/giphy.gif",
    "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMm5oY2RoeGlzYmNjM2Rjb2E4M3duZmp1YjkweGE4NDVnOW56NzVsbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IRbWyxAtSYZzzJhLvG/giphy.gif"
]

@bot.event
async def on_ready():
    print(f"تم تشغيل البوت: {bot.user}")

async def action(ctx, member, gifs, text):
    if member is None:
        await ctx.send(
            f"لازم تمنشن شخص مع الأمر.\n"
            f"مثال: `{ctx.prefix}{ctx.command.name} @الشخص`"
        )
        return

    gif = random.choice(gifs)

    await ctx.send(
        f"{ctx.author.mention} {text} {member.mention}\n{gif}"
    )

@bot.command(name="حضن")
async def hug(ctx, member: discord.Member = None):
    await action(ctx, member, hug_gifs, "حضن")

@bot.command(name="كف")
async def slap(ctx, member: discord.Member = None):
    await action(ctx, member, slap_gifs, "كف")

@bot.command(name="قتل")
async def kill(ctx, member: discord.Member = None):
    await action(ctx, member, kill_gifs, "قتل")

@bot.command(name="بوسه")
async def kiss(ctx, member: discord.Member = None):
    await action(ctx, member, kiss_gifs, "باس")

@bot.command(name="ارفس")
async def kick(ctx, member: discord.Member = None):
    await action(ctx, member, kick_gifs, "رفس")

@bot.command(name="قي")
async def gay_percentage(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send(
            "لازم تمنشن شخص مع الأمر.\n"
            "مثال: `!قي @الشخص`"
        )
        return

    percentage = random.randint(0, 100)

    await ctx.send(
        f"نسبة القي عند {member.mention} هي **{percentage}%**"
    )

@bot.command(name="الاوامر")
async def commands_list(ctx):
    embed = discord.Embed(
        title="قائمة الأوامر",
        description=(
            "━━━━━━━━━━━━━━━━━━━━\n"
            "أوامر التفاعل\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "`!حضن @الشخص` — حضن شخص\n"
            "`!كف @الشخص` — كف شخص\n"
            "`!بوسه @الشخص` — بوسة على الخد\n"
            "`!ارفس @الشخص` — رفس شخص\n"
            "`!قتل @الشخص` — قتل شخص\n"
            "`!قي @الشخص` — معرفة النسبة\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "جميع الأوامر التي تحتوي على شخص تحتاج إلى منشن.\n"
            "━━━━━━━━━━━━━━━━━━━━"
        ),
        color=discord.Color.blurple()
    )

    embed.set_footer(
        text=f"طلب بواسطة {ctx.author}",
        icon_url=ctx.author.display_avatar.url
    )

    await ctx.send(embed=embed)

bot.run(TOKEN)