# インストールした discord.py を読み込む
import discord
import requests
import datetime
import schedule
from discord.ext import commands
import io
import aiohttp

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'aa'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

async def job(message):
    await message.channel.send('そろそろ寝ましょう！')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')
    if message.content == '/konn':
        t_now = datetime.datetime.now().time()
        t_now = str(t_now)
        t_now = t_now[:2]
        print(t_now)
        t_now = int(t_now)
        print(type(t_now))
        print(t_now)

        if 5 <= t_now < 12:
            await message.channel.send('おはようございます')

        elif 12 <= t_now < 18:
            await message.channel.send('こんにちは')

        elif 18 <= t_now < 24:
            await message.channel.send('こんばんは')

        elif 0 <= t_now < 5:
            await message.channel.send('もう夜遅くです！寝ましょう！')

    if message.content == '明日の天気':
        url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'
        api_data = requests.get(url).json()
        weather = api_data['forecasts'][1]
        await message.channel.send(api_data['title'] + '\n' '明日の天気は'+ weather['telop'])
        
    if message.content == '今日の天気':
        url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'
        api_data = requests.get(url).json()
        weather = api_data['forecasts'][0]
        await message.channel.send(api_data['title'] + '\n' '今日の天気は'+ weather['telop'])

    if message.content == '極秘コマンド>>うんち<<':
        await message.channel.send('https://i.gzn.jp/img/2017/10/19/golden-unko-jewelry/00_m.jpg')

    if message.content == 'ンアッーー':
        ar1t = (
              '```(≧Д≦)' + '\n' +
              '.......................,,,z=~’ﾞ’+”ｯ彡ｯ,､' + '\n' + 
              '....................,ｨ´............“‘:’;:;ｯ;,' + '\n' + 
              '................’ ﾞ´`ﾞﾐﾞｯ,..............“‘,`,' + '\n' + 
              '...........,／.......`､ﾞミ.................ﾞ:;:,' + '\n' + 
              '........./........... =ヾ､ﾞｼｼ=;,z,..........ﾞ;ｼ::ﾐ' + '\n' + 
              '......./........,ｒ,´.../.´`ヽ.゛ﾞ`.........,ﾞ彡:ﾐ' + '\n' + 
              '..... /......, ‘-､.`ヽ....................ﾐ;::彡;:' + '\n' + 
              '... ,’.....,ｼ´｀｀ ヽ`i｀!.............. ,,彡;::ｼ:彡' + '\n' + 
              '..;.....､（´ ￣`ヽ / ‘..............シ:ｼ;:ﾐ::ｼ”' + '\n' + 
              '´:::::.ヾ.....￣´..............’ `,ｼﾐﾞ' + '\n' + 
              ':::::::::::::.`:ヽ､...........…:;’＿,ソ’ﾞ’' + '\n' + 
              'ンアッーーーーーーーーーーーーーーーーーーーーーーーーーーーー```')
        await message.channel.send(ar1t)

    if client.user in message.mentions:
        reply = f'{message.author.mention} 呼んだ？'
        await message.channel.send(reply)

    if message.content == 'うん' or message.content == 'は？':
        await message.channel.send('死ねよ')

    if message.content == '時刻':
        dt = datetime.datetime.now()
        dt = str(dt)
        await message.channel.send(dt[:-7])

    if message.content == '増税':
        await message.channel.send('https://pbs.twimg.com/media/EFUS5YlU0AIAwok?format=jpg&name=small')
    
    if message.content == 'かわいい子':
        await message.channel.send(file=discord.File('.\\img\\1.jpg'))



schedule.every().wednesday.at("02:10").do(job)

        


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)