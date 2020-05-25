import discord, random
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import os
client=commands.Bot(command_prefix='/')
client.remove_command("help") 
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('with Senko /help'))   
@client.command()
async def mmstart(ctx):
    embed=discord.Embed()
    embed.title='MM Started!'
    embed.description='If youre not involved please do not talk / ping in this channel until were finished. :lock:'
    embed.set_image(url='https://images-ext-2.discordapp.net/external/kKeLfD1QibiNsOLlWIyp8UX6sbfHwdaZUJDu_rcCh5w/https/media.discordapp.net/attachments/706326604464259082/706326833494360194/linea.gif')
    await ctx.send(embed=embed)
@client.command()
async def mmcomplete(ctx):
    embed=discord.Embed()
    embed.title='MM Complete!'
    embed.description='You may now ping the middleman role. :unlock:'
    embed.set_image(url='https://images-ext-2.discordapp.net/external/kKeLfD1QibiNsOLlWIyp8UX6sbfHwdaZUJDu_rcCh5w/https/media.discordapp.net/attachments/706326604464259082/706326833494360194/linea.gif')
    await ctx.send(embed=embed)
@client.command()
@commands.has_permissions(ban_members=True)
async def ANTIRAID(ctx):
    embed=discord.Embed()
    embed.title='Server READY to LOCKDOWN!'
    embed.description='Are you sure to Lock the server to avoid Raids?, y/n IN CONSOLE.'
    embed.set_image(url='https://media.discordapp.net/attachments/704405458001199234/711601765480661059/giphy.gif')
    await ctx.send(embed=embed)
@client.command()
async def Info(ctx):
    embed=discord.Embed()
    embed.title='IndominusBot ©'
    embed.description='/-----A new view about botting. v1.2.1 Created for DBA and DX-----/          by IndominusVegito#3939. Thanks Deleto#5915 for gif sources            -/-------Code protected by Pylock © ---    Hosted 24/7 by Heroku ©'
    embed.set_image(url='https://images-ext-2.discordapp.net/external/kKeLfD1QibiNsOLlWIyp8UX6sbfHwdaZUJDu_rcCh5w/https/media.discordapp.net/attachments/706326604464259082/706326833494360194/linea.gif')
    await ctx.send(embed=embed)
@client.command()
@commands.has_permissions(ban_members=True)
async def Armor(ctx):
    embed=discord.Embed()
    embed.title='ARMOR MODE ON :white_check_mark:'
    embed.description='Locked commands, Waiting for input in Console...'
    embed.set_image(url='https://images-ext-2.discordapp.net/external/kKeLfD1QibiNsOLlWIyp8UX6sbfHwdaZUJDu_rcCh5w/https/media.discordapp.net/attachments/706326604464259082/706326833494360194/linea.gif')
    await ctx.send(embed=embed)
@client.command()
async def Hellosexy(ctx):
    embed=discord.Embed()
    embed.title='Im back! YOSHAAAAAAA!'
    embed.description='Hello there, boss!'
    embed.set_image(url='https://images-ext-2.discordapp.net/external/kKeLfD1QibiNsOLlWIyp8UX6sbfHwdaZUJDu_rcCh5w/https/media.discordapp.net/attachments/706326604464259082/706326833494360194/linea.gif')
    await ctx.send(embed=embed)
@client.command()
async def mmguide(ctx):
    embed=discord.Embed()
    embed.title='MM Starters Guide'
    embed.description='If youre a Android MM , you cant mm atm, we only use iOS mms.'
    embed.set_image(url='https://media.discordapp.net/attachments/632389484737986560/706174486826975323/Links.png')
    await ctx.send(embed=embed)
@client.command()
async def howmmwork(ctx):
    embed=discord.Embed()
    embed.title='This is how MMs Work.'
    embed.description='---/ Once your partner and you have a deal, you can call a mm /--- The mm will verify both accs and exchange them.'
    embed.set_image(url='https://images-ext-2.discordapp.net/external/kKeLfD1QibiNsOLlWIyp8UX6sbfHwdaZUJDu_rcCh5w/https/media.discordapp.net/attachments/706326604464259082/706326833494360194/linea.gif')
    await ctx.send(embed=embed)
@client.command()
@commands.has_permissions(ban_members=True)
async def Unlock(ctx):
    embed=discord.Embed()
    embed.title='Armor OFF! :unlock:'
    embed.description='Unlocking commands and main console.'
    embed.set_image(url='https://images-ext-2.discordapp.net/external/kKeLfD1QibiNsOLlWIyp8UX6sbfHwdaZUJDu_rcCh5w/https/media.discordapp.net/attachments/706326604464259082/706326833494360194/linea.gif')
    await ctx.send(embed=embed)
@client.command()
async def SayHi(ctx):
    embed=discord.Embed()
    embed.title='Hello'
    embed.description='Hows all going , gamer?'
    embed.set_image(url='https://media.discordapp.net/attachments/704405458001199234/711590906138066974/tenor.gif')
    await ctx.send(embed=embed)
@client.command()
@commands.has_permissions(ban_members=True)
async def Update(ctx):
    embed=discord.Embed()
    embed.title='Setting... :repeat:'
    embed.description='Ready to Update, commands in console UNLOCKED.'
    embed.set_image(url='https://cdn.discordapp.com/attachments/704405458001199234/711603286154805318/200.gif')
    await ctx.send(embed=embed)
@client.command()
async def Bot(ctx):
    embed=discord.Embed()
    embed.title='Bot News'
    embed.description='Getting updated, this is just a beta! :)'
    embed.set_image(url='https://images-ext-2.discordapp.net/external/kKeLfD1QibiNsOLlWIyp8UX6sbfHwdaZUJDu_rcCh5w/https/media.discordapp.net/attachments/706326604464259082/706326833494360194/linea.gif')
    await ctx.send(embed=embed)
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member=None):
    if not member:
        embed=discord.Embed()
        embed.title='Ban Command'
        embed.description='Please specify a member (ping him), you can also ban by ID using /ban <ID GOES HERE> :x: '
        embed.set_image(url='https://images-ext-2.discordapp.net/external/kKeLfD1QibiNsOLlWIyp8UX6sbfHwdaZUJDu_rcCh5w/https/media.discordapp.net/attachments/706326604464259082/706326833494360194/linea.gif')
        await ctx.send(embed=embed)
        return
    await member.ban()
    await ctx.send(f'{member.display_name} was banned from the server :white_check_mark:')
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed=discord.Embed()
        embed.title='IndominusBot ©'
        embed.description='You are not allowed to use this command! :x:'
        embed.set_image(url='https://images-ext-2.discordapp.net/external/kKeLfD1QibiNsOLlWIyp8UX6sbfHwdaZUJDu_rcCh5w/https/media.discordapp.net/attachments/706326604464259082/706326833494360194/linea.gif')                      
        await ctx.send(embed=embed)
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member=None):
    if not member:
        embed=discord.Embed()
        embed.title='Kick Command'
        embed.description='Please specify a member (ping him) :x:'
        embed.set_image(url='https://images-ext-2.discordapp.net/external/kKeLfD1QibiNsOLlWIyp8UX6sbfHwdaZUJDu_rcCh5w/https/media.discordapp.net/attachments/706326604464259082/706326833494360194/linea.gif')
        await ctx.send(embed=embed)
        return
    await member.kick()
    await ctx.send(f'{member.display_name} was kicked from the server :white_check_mark:')
@kick.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed=discord.Embed()
        embed.title='IndominusBot ©'
        embed.description='You are not allowed to use this command! :x:'
        embed.set_image(url='https://images-ext-2.discordapp.net/external/kKeLfD1QibiNsOLlWIyp8UX6sbfHwdaZUJDu_rcCh5w/https/media.discordapp.net/attachments/706326604464259082/706326833494360194/linea.gif')                      
        await ctx.send(embed=embed)
@client.command()
@commands.has_permissions(ban_members=True)
async def mute(ctx, member: discord.Member=None):
    if not member:
        embed=discord.Embed()
        embed.title='Mute Command'
        embed.description='Please specify a member (ping him) :x:'
        embed.set_image(url='https://images-ext-2.discordapp.net/external/kKeLfD1QibiNsOLlWIyp8UX6sbfHwdaZUJDu_rcCh5w/https/media.discordapp.net/attachments/706326604464259082/706326833494360194/linea.gif')
        await ctx.send(embed=embed)
        return
    role = discord.utils.get(ctx.guild.roles, name="Muted (Indo)")
    await member.add_roles(role)
    await ctx.send(f'{member.display_name} is now muted. :white_check_mark:')
    print('Muted user!') 
@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed=discord.Embed()
        embed.title='IndominusBot ©'
        embed.description='You are not allowed to use this command! :x:'
        embed.set_image(url='https://images-ext-2.discordapp.net/external/kKeLfD1QibiNsOLlWIyp8UX6sbfHwdaZUJDu_rcCh5w/https/media.discordapp.net/attachments/706326604464259082/706326833494360194/linea.gif')                      
        await ctx.send(embed=embed)
@client.command()
@commands.has_permissions(ban_members=True)
async def unmute(ctx, member: discord.Member=None):
    if not member:
        embed=discord.Embed()
        embed.title='Unmute Command'
        embed.description='Please specify a member (ping him) :x:'
        embed.set_image(url='https://images-ext-2.discordapp.net/external/kKeLfD1QibiNsOLlWIyp8UX6sbfHwdaZUJDu_rcCh5w/https/media.discordapp.net/attachments/706326604464259082/706326833494360194/linea.gif')
        await ctx.send(embed=embed)
        return
    role = discord.utils.get(ctx.guild.roles, name="Muted (Indo)")
    await ctx.send(f'{member.display_name} is now unmuted. :white_check_mark:')
    await member.remove_roles(role)
@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed=discord.Embed()
        embed.title='IndominusBot ©'
        embed.description='You are not allowed to use this command! :x:'
        embed.set_image(url='https://images-ext-2.discordapp.net/external/kKeLfD1QibiNsOLlWIyp8UX6sbfHwdaZUJDu_rcCh5w/https/media.discordapp.net/attachments/706326604464259082/706326833494360194/linea.gif')                      
        await ctx.send(embed=embed)
@client.command(aliases=['bc'])
async def Broadcast(ctx, *, msg):
    await ctx.send(msg)
    await ctx.message.delete()
@client.command(aliases=['rbc'])
async def Richbroadcast(ctx, *, msg):
    embed=discord.Embed()
    embed.title='Broadcast Message'
    embed.description=msg
    await ctx.send(embed=embed)
    await ctx.message.delete()
@client.command()
async def Hello(ctx):
    embed=discord.Embed()
    embed.title='IndominusBot says:'
    replies=['Hola amigo!','Hello, good day!','Getting fixed','Hola, se hablar español!','I would like to understand more, hello btw!','Im learning some languages','Ah yeah, Family Guy is great','https://www.youtube.com/watch?v=nM__lPTWThU&list=PLmXxqSJJq-yVWpRFGImHYZBQTuBGLjG4t&index=30',]
    embed.description=random.choice(replies)
    await ctx.send(embed=embed)
@client.command()
async def Music(ctx):
    embed=discord.Embed()
    embed.title='This is one of my Favorites:'
    replies=['https://youtu.be/SRvCvsRp5ho','https://youtu.be/VvyBiHGr2b8','https://youtu.be/9maDHDtWo1o','https://youtu.be/btPJPFnesV4','https://youtu.be/AGM8BMqBcTo','https://youtu.be/j64-Soj11UQ','https://youtu.be/_Yhyp-_hX2s','https://youtu.be/ytQ5CYE1VZw','https://youtu.be/5EbiRRpaYB4','https://youtu.be/bNawbNsx52A',]
    embed.description=random.choice(replies)
    await ctx.send(embed=embed)
@client.command()
async def helps(ctx):
    embed=discord.Embed()
    embed.title='IndominusBot'
    embed.description='BLOCKED COMMAND, asking Console to unlock.'
    embed.set_image(url='https://2.bp.blogspot.com/-j5ea0bWoNo0/VLgdY-YSEmI/AAAAAAAADpI/sNCKeTgFWC4/s1600/giphy%2B(19).gif')
    await ctx.send(embed=embed)
@client.command()
async def List(ctx):
    embed=discord.Embed()
    embed.title='IndominusBot'
    embed.description='BLOCKED COMMAND, asking Console to unlock. :lock:'
    embed.set_image(url='https://cdn.discordapp.com/attachments/704405458001199234/711603286154805318/200.gif')
    await ctx.send(embed=embed)
@client.command()
@commands.has_permissions(ban_members=True)
async def ANTIRAIDy(ctx):
    embed=discord.Embed()
    embed.title='WARNING /LOCKING SERVER/ WARNING! :trident:'
    embed.description='LOCKING MAIN CHANNELS AND ROLES, SEARCHING AND BANNING RAIDERS.'
    embed.set_image(url='https://cdn.discordapp.com/attachments/704405458001199234/711644991507791982/descarga.gif')
    await ctx.send(embed=embed)
@client.command()
@commands.has_permissions(ban_members=True)
async def ANTIRAIDn(ctx):
    embed=discord.Embed()
    embed.title='UNLOCKING SERVER!'
    embed.description='UNLOCKING MAIN CHANNELS AND ROLES. Armor mode ON, need Auth from Console. :white_check_mark:'
    embed.set_image(url='https://cdn.discordapp.com/attachments/707052425097248818/711649609331507200/24d484972fa1651b44d0c31dd9e682b4.gif')
    await ctx.send(embed=embed)
@client.command()
@commands.has_permissions(ban_members=True)
async def Checkupdate(ctx):
    embed=discord.Embed()
    embed.title='Checking Update...'
    embed.description='Bot updated, running on v1.2.1!  Code protected by Pylock© :white_check_mark:'
    embed.set_image(url='https://images-ext-2.discordapp.net/external/kKeLfD1QibiNsOLlWIyp8UX6sbfHwdaZUJDu_rcCh5w/https/media.discordapp.net/attachments/706326604464259082/706326833494360194/linea.gif')
    await ctx.send(embed=embed)
@client.command()
async def RateMeSenko(ctx):
    embed=discord.Embed()
    embed.title='Hmmmm...'
    embed.description='Always a 999 out of 10, youre the best! :heart: '
    embed.set_image(url='https://media.discordapp.net/attachments/541951178531930114/541951301777358858/happy.png')
    await ctx.send(embed=embed)
@client.command()
async def Yesorno(ctx):
    embed=discord.Embed()
    embed.title='Yes or Na? Hmmmm...'
    replies=['I say... Yes','I say... No']
    embed.description=random.choice(replies)
    embed.set_image(url='https://images-ext-2.discordapp.net/external/kKeLfD1QibiNsOLlWIyp8UX6sbfHwdaZUJDu_rcCh5w/https/media.discordapp.net/attachments/706326604464259082/706326833494360194/linea.gif')
    await ctx.send(embed=embed)
@client.command()
async def mmcancel(ctx):
    embed=discord.Embed()
    embed.title='MM Cancelled!'
    embed.description='You may now ping the middleman role. Dont waste MMs time. :white_check_mark:'
    embed.set_image(url='https://images-ext-2.discordapp.net/external/kKeLfD1QibiNsOLlWIyp8UX6sbfHwdaZUJDu_rcCh5w/https/media.discordapp.net/attachments/706326604464259082/706326833494360194/linea.gif')
    await ctx.send(embed=embed)
@client.command()
async def RPS(ctx):
    embed=discord.Embed()
    embed.title='Play Rock Paper Scissors with Senko!:'
    replies=['You choose Paper, I choose Scissors,  *I win!*','You choose Rock, I choose paper, *I win!*','You choose Scissors, I choose paper, *You win!*','You choose Scissors, I choose paper, *You win!*','You choose Scissors, I choose Scissors, *DRAW!*','You choose Scissors, I choose paper, *You win!*','You choose Rock, I choose Rock, *DRAW!*']
    embed.description=random.choice(replies)
    embed.set_image(url='https://media.discordapp.net/attachments/541951178531930114/558252413434200074/huh.png')
    await ctx.send(embed=embed)
@client.command()
async def Ping(ctx):
    embed=discord.Embed()
    embed.title='Ping!'
    embed.description='Pong! :ping_pong:'
    embed.set_image(url='https://media.discordapp.net/attachments/541951178531930114/541951295813189632/whistle.png?width=677&height=677')
    await ctx.send(embed=embed)
@client.command()
async def Shutdown(ctx):
    embed=discord.Embed()
    embed.title='Saving Commands!'
    embed.description='Shutting down...'
    embed.set_image(url='https://images-ext-2.discordapp.net/external/kKeLfD1QibiNsOLlWIyp8UX6sbfHwdaZUJDu_rcCh5w/https/media.discordapp.net/attachments/706326604464259082/706326833494360194/linea.gif')
    await ctx.send(embed=embed)
@client.command()
async def Vegito(ctx):
    embed=discord.Embed()
    embed.title='THIS IS WHERE IT ENDS!'
    embed.description='FINAL KAMEHAMEHAAAAAAAAAA!'
    embed.set_image(url='https://media.discordapp.net/attachments/632389484737986560/711755904634191882/FinalKamehameha.gif')
    await ctx.send(embed=embed)
@client.command()
async def Allah(ctx):
    embed=discord.Embed()
    embed.title='قرد الله مذهل جدا'
    embed.description='هيريس قرد الله ، يحب الله ومشروبات الغازية الرائعة اللطيفة والرائعة ، أحبها'
    embed.set_image(url='https://cdn.discordapp.com/attachments/704405458001199234/711770428019965952/9k.png')
    await ctx.send(embed=embed)
@client.command()
async def Gogeta(ctx):
    embed=discord.Embed()
    embed.title='Youre going STRAIGHT TO HELL!ا'
    embed.description='KA..ME....HAA..MEE.HAAAAAA!'
    embed.set_image(url='https://media.discordapp.net/attachments/607323165047390248/711741143980703775/UltimateKamehameha.gif')
    await ctx.send(embed=embed)
@client.command()
async def Sex(ctx):
    embed=discord.Embed()
    embed.title='Have'
    embed.description='Sex'
    embed.set_image(url='https://media.discordapp.net/attachments/366226102663774228/701082554840645652/have_sex.gif')
    await ctx.send(embed=embed)
@client.command()
async def mmrules(ctx):
    embed=discord.Embed()
    embed.title='IMPORTANT. GUIDELINES ON HOW TO TRADE AND SELL WHILST USING A MIDDLEMAN'
    embed.description='Use a middleman! To use a middleman for a trade, you will have to use the  #mm-chat-1, #mm-chat-2, and #whale-mm-chat channels.  Just ping Middlemen or Whale Middlemen (only in the appropriate channels) and wait for one to assist you. If no one responds, just wait. Its better to wait for one to respond rather than doing the trade and risking the chance of getting scammed. Remember to check their roles or check #staff-list to make sure it is a real middleman.  Buying, selling, trading, vendors, and farm bots are against Dokkan ToS. We are not responsible if you get banned.'
    embed.set_image(url='https://images-ext-2.discordapp.net/external/kKeLfD1QibiNsOLlWIyp8UX6sbfHwdaZUJDu_rcCh5w/https/media.discordapp.net/attachments/706326604464259082/706326833494360194/linea.gif')
    await ctx.send(embed=embed)
@client.command()
async def help(ctx):
    embed=discord.Embed()
    embed.title='IndominusBot ©'
    embed.description='For IndominusBot you can use /Info, /Hello , /SayHi , /Music, /info, /RateMeSenko, /RPS,/Ping, /Yesorno, /Allah, /Vegito, /Gogeta, /Sex, /Movie, /cheems, /afk (Troll Command) ,  ------------------------Coded by :tada: IndominusVegito#3939 :tada:------------------------  Questions? Contact me. ----------------------------------------'
    embed.add_field(name="Moderation Commands", value="/ban, /kick , /mute, /clear, /Update, /Armor , /Unlock", inline=False)
    embed.add_field(name="With /Broadcast Indo will say anything that you like!", value="You can also use /rbc, /bc, or /Richbroadcast", inline=False)
    embed.add_field(name="About Middlemen Commands", value="/mmrules, /howmmwork, /mmstart , /mmcomplete , /mmcancel", inline=False)
    embed.set_image(url='https://images-ext-2.discordapp.net/external/kKeLfD1QibiNsOLlWIyp8UX6sbfHwdaZUJDu_rcCh5w/https/media.discordapp.net/attachments/706326604464259082/706326833494360194/linea.gif')
    await ctx.author.send(embed=embed)
    embed=discord.Embed()
    embed.title='IndominusBot ©'
    embed.description='Sent DM with commands. Please check Direct Messages :white_check_mark:'
    embed.set_image(url='https://images-ext-2.discordapp.net/external/kKeLfD1QibiNsOLlWIyp8UX6sbfHwdaZUJDu_rcCh5w/https/media.discordapp.net/attachments/706326604464259082/706326833494360194/linea.gif')                      
    await ctx.send(embed=embed)
@client.command()
async def Movie(ctx):
    await ctx.send('Here: https://cdn.discordapp.com/attachments/421481948871917569/713965424387293245/spongebob_first_movie.mp4')
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    embed=discord.Embed()
    embed.title='IndominusBot ©'
    embed.description='Cleared messages successfully :white_check_mark:'
    embed.set_image(url='https://images-ext-2.discordapp.net/external/kKeLfD1QibiNsOLlWIyp8UX6sbfHwdaZUJDu_rcCh5w/https/media.discordapp.net/attachments/706326604464259082/706326833494360194/linea.gif')                      
    await ctx.send(embed=embed)

@clear.error
async def clear_error(ctx, error):
 if isinstance(error, commands.CheckFailure):
   embed=discord.Embed()
   embed.title='IndominusBot ©'
   embed.description='You are not allowed to use this command! :x:'
   embed.set_image(url='https://images-ext-2.discordapp.net/external/kKeLfD1QibiNsOLlWIyp8UX6sbfHwdaZUJDu_rcCh5w/https/media.discordapp.net/attachments/706326604464259082/706326833494360194/linea.gif')                      
   await ctx.send(embed=embed)

@client.command()
async def unban(ctx, user):
 user=await client.fetch_user(user)
 await ctx.guild.unban(user)
 await ctx.send(f'Unbanned {user.name} :white_check_mark:')

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='welcome-bye')
    await channel.send(f'{member.mention}')
    embed=discord.Embed()
    embed.title='Hello! :tada:'
    embed.description='Welcome! to Dragon Ball Allegiance! Go to #rules to get full access to the server!'
    embed.set_image(url='https://media.discordapp.net/attachments/704402769536221205/714304458300981268/DBABanner2.jpg?width=1204&height=677')
    embed.set_footer(text="Coded by IndominusVegito#3939",icon_url="https://i.imgur.com/CbQHgfm.gif")
    await channel.send(embed=embed)
@client.command()
async def cheems(ctx):
    embed=discord.Embed()
    embed.title='Hemlo, welcome to cheems thermpy!'
    embed.description='Whats your issue, friemd?'
    embed.set_image(url='https://media.discordapp.net/attachments/704421692113682434/714506401807990804/image0.jpg')
    await ctx.send(embed=embed)
@client.command()
async def afk(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/704447325879402518/714387893291974737/video0.mov')
@client.command()
@commands.has_permissions(ban_members=True) 
async def warn(ctx, member: discord.Member=None):
    if not member:
        embed=discord.Embed()
        embed.title='Warn Command'
        embed.description='Please specify a member (ping him) :x:'
        embed.set_image(url='https://images-ext-2.discordapp.net/external/kKeLfD1QibiNsOLlWIyp8UX6sbfHwdaZUJDu_rcCh5w/https/media.discordapp.net/attachments/706326604464259082/706326833494360194/linea.gif')
        await ctx.send(embed=embed)
        return
    embed=discord.Embed()
    embed.title='Warn Command'
    embed.description='User warned successfully, saving warn in logs :white_check_mark:.'
    embed.set_image(url='https://images-ext-2.discordapp.net/external/kKeLfD1QibiNsOLlWIyp8UX6sbfHwdaZUJDu_rcCh5w/https/media.discordapp.net/attachments/706326604464259082/706326833494360194/linea.gif')
    await ctx.send(embed=embed)
@warn.error
async def warn_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed=discord.Embed()
        embed.title='IndominusBot ©'
        embed.description='You are not allowed to use this command! :x:'
        embed.set_image(url='https://images-ext-2.discordapp.net/external/kKeLfD1QibiNsOLlWIyp8UX6sbfHwdaZUJDu_rcCh5w/https/media.discordapp.net/attachments/706326604464259082/706326833494360194/linea.gif')                      
        await ctx.send(embed=embed)
client.run(os.gevenv('TOKEN'))
