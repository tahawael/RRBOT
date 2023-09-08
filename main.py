import random
import discord
import time
from discord.ext import commands
from PIL import Image, ImageDraw, ImageSequence
import io
import requests
from img import generate





intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(intents=intents, command_prefix='!')

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.upper().startswith ('/RR'):
        playerA = message.author.avatar.url
        mentionA = message.mentions[0].avatar.url



        
        emojis = [
            "❤️", "👍", "🔥", "😍", "🙏", "👏", "🤔", "😭",
            "👉", "👌", "💪", "✨", "🙌", "😎", "💕",
            "💯", "🙈", "🤣", "🤷‍♀️", "🤦‍♂️", "👀", "😋", "👇", "🤩",
            "💖", "🤗", "😜", "😱", "👊", "👋", "😉", "💔",
            "🤭", "😓", "🤪", "🤫", "👑", "💥", "😇", "😈",
            "🌟", "😸",
            "🌈", "🌸", "🍄", "🍆", "🍉", "💅", "🍋",
            "🍌", "🍍", "🍑", "🍒", "🍓", "🍔", "🍕",
            "🍗", "🍞", "🍟","👩‍❤️‍💋‍👩",
             "🍤", "🍦", "🍩","💋","🤢","👨‍❤️‍💋‍👨",
            "🍪", "🍫", "🍯", "🍰","🍳",
        ]
        randomEmo = random.choice(emojis)
        if message.mentions:
            print('')
        else:
            await message.reply(f'stop being emo 💀  ||This aint no solo game, u gotta mention someone to play with. {randomEmo} ||')

        player = message.author.display_name
        mention = message.mentions[0].display_name
        if mention == player:
            await message.reply(
                f'stop being emo 💀  ||This aint no solo game, u gotta mention someone to play with. {randomEmo} ||'
            )
            exit()
        # print(mention)
        Answer= ['a bullet', 'no bullet', 'no bullet', 'no bullet', 'no bullet', 'no bullet']
        a=0
        b=6
        turn = [1,-1]
        turn = random.choice(turn)
        global finalMsg
        finalMsg =''
        while a < b:
            boomOrGun= [':boom:', ':gun:']
            theNum= 1
            aa= random.choice(Answer)
            finalMsg
            if aa == 'a bullet':
                theNum=0
            else:
                theNum=1
            if turn == 1 :
                finalMsg += (f'`{player}` pulled the trigger and there is {aa} {boomOrGun[theNum]} \n')
                a=a+1
                turn = turn*-1  
            else:
                finalMsg += (f'`{mention}` pulled the trigger and there is {aa} {boomOrGun[theNum]} \n')
                a=a+1
                turn = turn*-1 
            Answer.remove(aa)
            if aa == 'a bullet' and turn != 1:
                title = f'{randomEmo}  {player.upper()} VS {mention.upper()}  {randomEmo}'
                embed = discord.Embed(description=f'{finalMsg}`{player}` died lol :skull:', title=title)
                async with message.channel.typing():
                    generate(url=requests.get(playerA).content)
                    file = discord.File("C:/Users/Mohamed Wael/Desktop/vscode/out1.gif", filename="image.gif")
                    embed.set_image(url='attachment://image.gif')
                    await message.reply(embed=embed, file=file)
                break

            if aa == 'a bullet' and turn == 1:
                
                title = f'{randomEmo}  {player.upper()} VS {mention.upper()}  {randomEmo}'
                embed = discord.Embed(description=f'{finalMsg}`{mention}` died lol :skull:', title=title)
                # await tt()
                async with message.channel.typing():
                    generate(url=requests.get(mentionA).content)
                    # do expensive stuff here                        
                    file = discord.File("out1.gif", filename="image.gif")
                    embed.set_image(url='attachment://image.gif')
                    await message.reply(file=file, embed=embed)
                break
            # if aa == 'a bullet' and turn != 1:
            #     title = f' {randomEmo}  {player.upper()} VS {mention.upper()}  {randomEmo} '
            #     await message.reply(embed=discord.Embed(description=f'{finalMsg}`{player}` died lol :skull:', title=title))
            #     embed.set_thumbnail(url=player.avatar_url) 
            #     break

            # if aa == 'a bullet' and turn == 1:
            #     title = f' {randomEmo}  {player.upper()} VS {mention.upper()}  {randomEmo} '
            #     await message.reply(embed=discord.Embed(description=f'{finalMsg}`{mention}` died lol :skull:', title=title))
            #     embed.set_thumbnail(url=mention.avatar_url) 
            #     break


client.run(TOKEN)
      