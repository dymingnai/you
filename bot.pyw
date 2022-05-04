import discord
import random
import random
import time
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')
arr = ['3star', '2star', '1star', '0star']
rate = [1.33, 13, 85, 0.67]#控制機率
img_3star='<:3star:928684158803411034>'#discord img
img_2star='<:2star:928684145398407259>'
img_1star='<:1star:928684127518068767>'
img_0star='<:neww:928684172128690196>'

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def 抽卡(ctx,som:str=''):#som為抓 "!抽卡" 後的文字
    card = [None]*10
    for i in range(10):
        prob_card=arr[random_index(rate)]#先給定  避免每次if都是不同的
		
        if prob_card == '3star':#去discord加入三星的表情後，反斜線\+表情按送出，所顯示的那一串 自行更改
            card[i]=img_3star
        elif prob_card == '2star':
            card[i]=img_2star
        elif prob_card == '1star':
            card[i]=img_1star
        elif prob_card == '0star':
            card[i]=img_0star
        else:
            card[i]=img_0star

    if card.count(img_1star)==10:#保底
        for x in range(9,-1,-1):
            if  card[x]==img_1star:
                card[x]=img_2star
                break

    msg=''
    if card.count(img_1star)==9:#保底嘲諷
        if card.count(img_3star)!=1:
            msg='笑死保底，非洲人4你?'+'<:emoji_04:885782471738802177>'

    if card.count(img_0star)>=1:#抽到彩的恭喜
        msg='哇！抽到PU聖裝！！'+'<:nana26:885761691919478814>'	
	
    if card.count(img_3star)>=1:#抽到彩的恭喜
        msg='恭喜抽中彩！'+'<:mj15:885779556869480478>'

    lol="".join('%s' %id for id in card)
    await ctx.send(str(ctx.message.author)+' > '+lol+msg+'\t'+som)#ctx.message.author獲取discord用戶id

@bot.command()
async def 抽卡機率(ctx):
    await ctx.send( "PU.."+'{:>5}'.format(str(rate[3]))+"%\n"
	            "★3.."+'{:>5}'.format(str(rate[0]))+"%\n"
                    "★2.."+'{:>5}'.format(str(rate[1]))+"%\n"
                    "★1.."+'{:>5}'.format(str(rate[2]))+"%\n")

@bot.command()
async def 加倍(ctx):
    global rate
    rate = [2.66,26,70,1.34]
    await ctx.send('加倍成功')

@bot.command()
async def 取消加倍(ctx):
    global rate
    rate = [1.33,13,85,0.67]
    await ctx.send('取消加倍成功')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="愛麗絲秘跡抽卡模擬", description="沒有反應，就只是一個抽卡ㄐ器人，以下是指令", color=0xcc25de)
    embed.add_field(name="!抽卡", value="抽10張卡 有保底", inline=False)
    embed.add_field(name="!抽卡 空格 \'任意文字\' ", value="與抽卡相同，後方輸入的任意文字會回傳", inline=False)
    embed.add_field(name="!抽卡機率", value="顯示當前抽卡機率", inline=False)
    embed.add_field(name="!加倍", value="加倍成三星機率4%，PU聖裝也會加倍", inline=False)
    embed.add_field(name="!取消加倍", value="變成未加倍時的機率2%", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def 艾希莉(ctx):
    await ctx.send( "https://cdn.discordapp.com/attachments/910204008587743282/971230831286829096/QQ20210914192631.jpg")

def random_index(rate):
    start = 0
    index = 0
    randnum = random.randint(0, sum(rate))

    for index, scope in enumerate(rate):
        start += scope
        if randnum <= start:
            break
    return index

bot.run('')#輸入你的discord bot token
