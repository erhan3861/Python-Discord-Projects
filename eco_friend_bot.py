import discord
from discord.ext import commands
from settings import settings

intents = discord.Intents.default()
intents.message_content = True

# Botunuzu oluşturun
bot = commands.Bot(command_prefix='!', intents=intents)

# Yardım komutunu oluşturun
@bot.command()
async def yardim(ctx):
    yardim_mesaji = """
    Merhaba! Ben çevre dostu bir Discord botuyum. İşte kullanabileceğiniz komutlar:
    
    !bilgi - Çevre temizliği ve sürdürülebilirlik hakkında bilgi alın.
    !geri_donusum - Geri dönüşüm hakkında ipuçları alın.
    !enerji_tasarrufu - Enerji tasarrufu hakkında öneriler alın.
    """
    await ctx.send(yardim_mesaji)

# Bilgi komutunu oluşturun
@bot.command()
async def bilgi(ctx):
    bilgi_mesaji = "Çevre temizliği ve sürdürülebilirlik konusunda bilgi almak için çevre kuruluşlarının web sitelerini ziyaret edebilirsiniz."
    await ctx.send(bilgi_mesaji)

# Geri dönüşüm komutunu oluşturun
@bot.command()
async def geri_donusum(ctx):
    geri_donusum_mesaji = "Geri dönüşüm, atıkları yeniden kullanarak ve yeniden işleyerek çevreyi koruma konusunda önemli bir adımdır. Atıkları ayrıştırarak ve geri dönüşüm kutularını kullanarak geri dönüşüme katkıda bulunabilirsiniz."
    await ctx.send(geri_donusum_mesaji)

# Enerji tasarrufu komutunu oluşturun
@bot.command()
async def enerji_tasarrufu(ctx):
    enerji_tasarrufu_mesaji = "Enerji tasarrufu yapmak için evde ve işte küçük değişiklikler yapabilirsiniz. Örneğin, lambaları kapatmayı unutmayın ve gereksiz elektronikleri kapatın."
    await ctx.send(enerji_tasarrufu_mesaji)

# Botunuzu çalıştırın
bot.run(settings['token1'])
