#---Terms of Service:---#
#By use of the software that you are using released by me either custom or public, you are agreeing to the terms of use that I have outlined below:#

#1. My software is subject to copyright, any attempt to duplicate without giving proper credit is prohibited.#
#2. My released github software is public use and open-sourced, you are allowed to use my software for reference to design your own discord bots.#
#3. I am not responsible for any damage that is done by my software to your computer or any discord server.#
#4. Reselling any versions of my software for your own personal gain is prohibited.#
#5. Changing any of the creator lines outlined in the main.py file is prohibited unless specifically allowed by WebTheDev.#
#6. I am allowed to at any time to deny any attempt for support for my software.#
#7. I am allowed to prohibit custom software at any time for any reason.# 


#Imports:#
import discord, datetime, time
import asyncio
import os
import sys
from discord.ext import commands
from discord.ext import tasks
from discord.ext.tasks import loop
from datetime import datetime, timezone
from discord.utils import get
from config import token, CommandPrefix, activitytype, botstatusmessage, developerid, guildID, StaffRoleID, SystemLogsChannelID, embedcolor, customfooter, customfootvalue, GracePeriodForKicks, IncludeInviteLink, DiscordServerInviteLink

#Bot Setup:#
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix = f'{CommandPrefix}', intents=intents)
bot.remove_command('help')

#Global Values:#
antiraidv = False


#Events:#
@bot.event
async def on_ready():
    await bot.wait_until_ready()
    print("\n/////////////////////////////////")
    print("//                             //")
    print("//         Anti-RaidBot        //")
    print("//                             //")
    print("/////////////////////////////////\n")
    print("Bot Infomation:")
    print ("------------------------------------")
    print (f"Bot Name: {bot.user.name}#{bot.user.discriminator}")
    print (f"Bot ID: {bot.user.id}")
    creator = bot.get_user(387002430602346499) #DO NOT CHANGE#
    print(f'Creator: {creator}')    #DO NOT CHANGE#
    print ("Discord Version: " + discord.__version__)
    guild = bot.get_guild(guildID)
    print(f'Operating Guild Name: {guild}')
    print ("-----------------------------------------")
    if f'{activitytype}' == 'Playing':
        activity1 = discord.Activity(type=discord.ActivityType.playing, name=f'{botstatusmessage}')
        await bot.change_presence(status=discord.Status.online, activity=activity1)
    elif f'{activitytype}' == 'Streaming':
        activity1 = discord.Activity(type=discord.ActivityType.streaming, name=f'{botstatusmessage}')
        await bot.change_presence(status=discord.Status.online, activity=activity1)
    elif f'{activitytype}' == 'Watching':
        activity1 = discord.Activity(type=discord.ActivityType.watching, name=f'{botstatusmessage}')
        await bot.change_presence(status=discord.Status.online, activity=activity1)
    elif f'{activitytype}' == 'Listening':
        activity1 = discord.Activity(type=discord.ActivityType.listening, name=f'{botstatusmessage}')
        await bot.change_presence(status=discord.Status.online, activity=activity1)
    else:
        activity1 = discord.Activity(type=discord.ActivityType.playing, name=f'{botstatusmessage}')
        await bot.change_presence(status=discord.Status.online, activity=activity1)
        print('''[WARN]: You have incorrectly specified the bot's activity type, the default has been selected.''')
        print("----------------------------------------------------")
    print("[MESSAGE]: Bot has logged into discord sucessfully. Command for Anti-Raid Defense is standing by.")
    print("-------------------------------------------------------------------------------------------------")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        message1 = ctx.message
        await message1.delete()
        author = ctx.message.author
        message2 = await ctx.send(f'{author.mention}')
        await message2.delete()
        embed = discord.Embed(description=f'''{author.mention}, Huh? I don't know that command!''', color=embedcolor)
        embed.set_author(name=f'{author}', icon_url=f'{author.avatar_url}')
        embed.add_field(name='**__Debug Error:__**', value=f'```discord.ext.commands.errors.CommandNotFound: {error}```')
        if customfooter == True:
            embed.set_footer(text=f'{customfootvalue}', icon_url=f'{bot.user.avatar_url}')
        else:
            embed.set_footer(text=f'{bot.user.name} | {bot.user.id}', icon_url=f'{bot.user.avatar_url}')
        try:
            message3 = await ctx.send(embed=embed)
        except discord.HTTPException:
            message3 = await ctx.send(f'''{author.mention}, I don't know that command!''')
        await asyncio.sleep(15)
        await message3.delete()

@bot.event
async def on_message(message):
    try:
        await bot.process_commands(message)
        if message.content.startswith("Ping") or message.content.startswith("ping"):
            embed = discord.Embed(description=f'Pong!', color=embedcolor)
            if customfooter == True:
                embed.set_footer(text=f'{customfootvalue}', icon_url=f'{bot.user.avatar_url}')
            else:
                embed.set_footer(text=f'{bot.user.name} | {bot.user.id}', icon_url=f'{bot.user.avatar_url}')
            try:
                try:
                    async with message.channel.typing():
                        await asyncio.sleep(1)
                    await message.reply(embed=embed, mention_author=False)
                except discord.HTTPException:
                    await message.reply(f'Pong!', mention_author=False)
            except Exception:
                pass
        elif message.content.startswith(f"<@!{bot.user.id}>") or message.content.startswith(f"<@{bot.user.id}>"):
            embed = discord.Embed(description=f'Hi there! I see that you have mentioned me! My bot command prefix is `{CommandPrefix}`.', color=embedcolor)
            if customfooter == True:
                embed.set_footer(text=f'{customfootvalue}', icon_url=f'{bot.user.avatar_url}')
            else:
                embed.set_footer(text=f'{bot.user.name} | {bot.user.id}', icon_url=f'{bot.user.avatar_url}')
            try:
                try:
                    async with message.channel.typing():
                        await asyncio.sleep(1)
                    await message.reply(embed=embed, mention_author=True)
                except discord.HTTPException:
                    await message.reply(f'Hi there! I see that you have mentioned me! My bot command prefix is `{CommandPrefix}``.', mention_author=True)
            except Exception:
                pass
        elif (f"<@!{bot.user.id}>" in message.content) or (f"<@!{bot.user.id}>" in message.content):
            embed = discord.Embed(description=f'Hi there! I see that you have mentioned me in your message! My bot command prefix is `{CommandPrefix}`.', color=embedcolor)
            if customfooter == True:
                embed.set_footer(text=f'{customfootvalue}', icon_url=f'{bot.user.avatar_url}')
            else:
                embed.set_footer(text=f'{bot.user.name} | {bot.user.id}', icon_url=f'{bot.user.avatar_url}')
            try:
                try:
                    async with message.channel.typing():
                        await asyncio.sleep(1)
                    await message.reply(embed=embed, mention_author=False)
                except discord.HTTPException:
                    await message.reply(f'Hi there! I see that you have mentioned me in your message! My bot command prefix is `{CommandPrefix}`.', mention_author=False)
            except Exception:
                pass
        else:
            pass
    except Exception as e:
        developer = bot.get_user(developerid)
        text = str('''Error on line {}'''.format(sys.exc_info()[-1].tb_lineno))
        embed = discord.Embed(title='on_message event fail', description=f'{text}, {str(e)}', color=embedcolor)
        try:
            await developer.send(embed=embed)
        except discord.HTTPException:
            await developer.send("on_message event fail" + str(e))
        print('[ERROR][Line {}]:'.format(sys.exc_info()[-1].tb_lineno) + f'{str(e)}')
        print("----------------------------------------")

@bot.event
async def on_member_join(member):
    try:
        global antiraid
        guild = bot.get_guild(guildID)
        userid = member.id
        if antiraidv == True:
            embed2 = discord.Embed(title=f'''You have been kicked from {guild.name}''', description=f"Hi there {member.mention}, you have been kicked from {guild.name}.", color=embedcolor)
            embed2.set_author(name=f'{member}', icon_url=member.avatar_url)
            embed2.add_field(name="**__Reason:__**", value="Anti-Raid mode is enabled!! Please try joining back later.", inline=True)
            embed2.add_field(name='**__Moderator:__**', value='Auto-Mod', inline=True)
            if IncludeInviteLink == True:
                embed2.add_field(name='**__Discord Invite Link:__**', value=f'{DiscordServerInviteLink}', inline=True)
            else:
                pass
            if customfooter == True:
                embed2.set_footer(text=f'{customfootvalue}', icon_url=f'{bot.user.avatar_url}')
            else:
                embed2.set_footer(text=f'{bot.user.name} | {bot.user.id}', icon_url=f'{bot.user.avatar_url}')
            try:
                try:
                    await member.send(embed=embed2)
                except discord.HTTPException:
                    await member.send(f"You have been kicked from {guild.name} for **Anti-Raid mode is enabled! Please try joining back later!**")
            except Exception:
                pass
            await member.kick(reason=f'Anti-Raid Mode is enabled!!')
            user = bot.get_user(userid)
            syslogc = bot.get_channel(SystemLogsChannelID)
            embed3 = discord.Embed(color=embedcolor)
            embed3.set_author(name=f'[AUTO-KICK] {user}', icon_url=user.avatar_url)
            embed3.add_field(name='**__Mention/ID:__**', value=f'{user.mention}\n{user.id}', inline=True)
            embed3.add_field(name="**__Reason:__**", value="Anti-Raid mode is enabled!! Please try joining back later.", inline=True)
            embed3.add_field(name='**__Moderator:__**', value='Auto-Mod', inline=True)
            if customfooter == True:
                embed3.set_footer(text=f'{customfootvalue}', icon_url=f'{bot.user.avatar_url}')
            else:
                embed3.set_footer(text=f'{bot.user.name} | {bot.user.id}', icon_url=f'{bot.user.avatar_url}')
            try:
                await syslogc.send(embed=embed3)
            except discord.HTTPException:
                await syslogc.send(f"[AUTO-KICK][{user.mention} - {user.id}]\n**__Reason:__** Anti-Raid mode is enabled!! Please try joining back later.\n**__Moderator:__** Auto-Mod")
        else:
            pass 
    except Exception as e:
        developer = bot.get_user(developerid)
        text = str('''Error on line {}'''.format(sys.exc_info()[-1].tb_lineno))
        embed = discord.Embed(title='on_member_join event fail', description=f'{text}, {str(e)}', color=embedcolor)
        try:
            await developer.send(embed=embed)
        except discord.HTTPException:
            await developer.send("on_member_join event fail" + str(e))
        print('[ERROR][Line {}]:'.format(sys.exc_info()[-1].tb_lineno) + f'{str(e)}')
        print("----------------------------------------")


#Commands:#
@bot.command()
async def antiraid(ctx):
    try:
        author = ctx.message.author
        message = ctx.message
        await message.delete()
        guild = ctx.guild
        staffrole = get(guild.roles, id=StaffRoleID) 
        if staffrole in author.roles:
            global antiraidv
            if antiraidv == False:
                antiraidv = True
                await ctx.channel.edit(slowmode_delay=300)
                embed = discord.Embed(title=f'Anti-Raid Mode Enabled', description=f'Anti-Raid has been enabled, no new members will be able to join, this channel has been set to a 5 minute cooldown.', color=embedcolor)
                embed.set_author(name=f'{author}', icon_url=f'{author.avatar_url}')
                if customfooter == True:
                    embed.set_footer(text=f'{customfootvalue}', icon_url=f'{bot.user.avatar_url}')
                else:
                    embed.set_footer(text=f'{bot.user.name} | {bot.user.id}', icon_url=f'{bot.user.avatar_url}')
                try:
                    message1 = await ctx.send(embed=embed)
                except discord.HTTPException:
                    message1 = await ctx.send(f"Anti-Raid Mode Enabled\nAnti-Raid has been enabled, no new members will be able to join, this channel has been set to a 5 minute cooldown.")
                syslogc = bot.get_channel(SystemLogsChannelID)
                embed2 = discord.Embed(title='Anti-Raid Mode Enabled', description=f'{author.mention} has enabled anti-raid mode for this server.', color=embedcolor)
                embed2.set_author(name=f'{author}', icon_url=f'{author.avatar_url}')
                if customfooter == True:
                    embed2.set_footer(text=f'{customfootvalue}', icon_url=f'{bot.user.avatar_url}')
                else:
                    embed2.set_footer(text=f'{bot.user.name} | {bot.user.id}', icon_url=f'{bot.user.avatar_url}')
                try:
                    await syslogc.send(embed=embed2)
                except discord.HTTPException:
                    await syslogc.send(f"Anti-Raid Mode Enabled\n{author.mention} has enabled anti-raid mode for this server.")
                now = (datetime.now(tz=timezone.utc))
                for member in guild.members:
                    current = (time.mktime(now.timetuple()))
                    memberjoin = member.joined_at
                    joinsec = (time.mktime(memberjoin.timetuple()))
                    total = (current - joinsec)
                    if (total <= GracePeriodForKicks):
                        embed2 = discord.Embed(title=f'''You have been kicked from {guild.name}''', description=f"Hi there {member.mention}, you have been kicked from {guild.name}.", color=embedcolor)
                        embed2.set_author(name=f'{member}', icon_url=member.avatar_url)
                        embed2.add_field(name="**__Reason:__**", value="Anti-Raid mode was enabled, all recently joined members are kicked!! Please try joining back later.", inline=True)
                        embed2.add_field(name='**__Moderator:__**', value='Auto-Mod', inline=True)
                        if IncludeInviteLink == True:
                            embed2.add_field(name='**__Discord Invite Link:__**', value=f'{DiscordServerInviteLink}', inline=True)
                        else:
                            pass
                        if customfooter == True:
                            embed2.set_footer(text=f'{customfootvalue}', icon_url=f'{bot.user.avatar_url}')
                        else:
                            embed2.set_footer(text=f'{bot.user.name} | {bot.user.id}', icon_url=f'{bot.user.avatar_url}')
                        try:
                            try:
                                await member.send(embed=embed2)
                            except discord.HTTPException:
                                await member.send(f"You have been kicked from {guild.name} for **Anti-Raid mode was enabled, all recently joined members are kicked!! Please try joining back later.**")
                        except Exception:
                            pass
                        await member.kick(reason=f'Anti-Raid mode was enabled, all recently joined members are kicked!! Please try joining back later.')
                        user = bot.get_user(member.id)
                        syslogc = bot.get_channel(SystemLogsChannelID)
                        embed3 = discord.Embed(color=embedcolor)
                        embed3.set_author(name=f'[AUTO-KICK] {user}', icon_url=user.avatar_url)
                        embed3.add_field(name='**__Mention/ID:__**', value=f'{user.mention}\n{user.id}', inline=True)
                        embed3.add_field(name="**__Reason:__**", value="Anti-Raid mode was enabled, all recently joined members are kicked!! Please try joining back later.", inline=True)
                        embed3.add_field(name='**__Moderator:__**', value='Auto-Mod', inline=True)
                        if customfooter == True:
                            embed3.set_footer(text=f'{customfootvalue}', icon_url=f'{bot.user.avatar_url}')
                        else:
                            embed3.set_footer(text=f'{bot.user.name} | {bot.user.id}', icon_url=f'{bot.user.avatar_url}')
                        try:
                            await syslogc.send(embed=embed3)
                        except discord.HTTPException:
                            await syslogc.send(f"[AUTO-KICK][{user.mention} - {user.id}]\n**__Reason:__** Anti-Raid mode was enabled, all recently joined members are kicked!! Please try joining back later.\n**__Moderator:__** Auto-Mod")
                    else:
                        pass
                await asyncio.sleep(30)
                await message1.delete()
            elif antiraidv == True:
                await ctx.channel.edit(slowmode_delay=300)
                embed = discord.Embed(title=f'Anti-Raid Mode', description=f'Anti-Raid has already been enabled! No new members will be able to join, this channel has been set to a 5 minute cooldown.', color=embedcolor)
                embed.set_author(name=f'{author}', icon_url=f'{author.avatar_url}')
                if customfooter == True:
                    embed.set_footer(text=f'{customfootvalue}', icon_url=f'{bot.user.avatar_url}')
                else:
                    embed.set_footer(text=f'{bot.user.name} | {bot.user.id}', icon_url=f'{bot.user.avatar_url}')
                try:
                    message1 = await ctx.send(embed=embed)
                except discord.HTTPException:
                    message1 = await ctx.send(f"Anti-Raid Mode\nAnti-Raid has already been enabled! No new members will be able to join, this channel has been set to a 5 minute cooldown.")
                await asyncio.sleep(30)
                await message1.delete()
        else:
            message5 = await ctx.send(f'{author.mention}')
            await message5.delete()
            embed5 = discord.Embed(description=f'''{author.mention}, you can't use that command!''', color=embedcolor)
            embed5.set_author(name=f'{author}', icon_url=f'{author.avatar_url}')
            if customfooter == True:
                embed5.set_footer(text=f'{customfootvalue}', icon_url=f'{bot.user.avatar_url}')
            else:
                embed5.set_footer(text=f'{bot.user.name} | {bot.user.id}', icon_url=f'{bot.user.avatar_url}') 
            try:
                message6 = await ctx.send(embed=embed5)
            except discord.HTTPException:
                message6 = await ctx.send(f'''{author.mention}, **you can't use that command!**''')
            await asyncio.sleep(20)
            await message6.delete()
    except Exception as e:
        developer = bot.get_user(developerid)
        text = str('''Error on line {}'''.format(sys.exc_info()[-1].tb_lineno))
        embed = discord.Embed(title='commands.antiraid function fail', description=f'{text}, {str(e)}', color=embedcolor)
        try:
            await developer.send(embed=embed)
        except discord.HTTPException:
            await developer.send("commands.antiraid function fail" + str(e))
        print('[ERROR][Line {}]:'.format(sys.exc_info()[-1].tb_lineno) + f'{str(e)}')
        print("----------------------------------------") 
        await asyncio.sleep(10)

@bot.command()
async def unantiraid(ctx):
    try:
        author = ctx.message.author
        message = ctx.message
        await message.delete()
        guild = ctx.guild
        staffrole = get(guild.roles, id=StaffRoleID) 
        if staffrole in author.roles:
            global antiraidv
            if antiraidv == True:
                antiraidv = False
                await ctx.channel.edit(slowmode_delay=0)
                embed = discord.Embed(title=f'Anti-Raid Mode Disabled', description=f'''Anti-Raid has been disabled! New members will now be able to join. This channel's cooldown time has been set to 0.''', color=embedcolor)
                embed.set_author(name=f'{author}', icon_url=f'{author.avatar_url}')
                if customfooter == True:
                    embed.set_footer(text=f'{customfootvalue}', icon_url=f'{bot.user.avatar_url}')
                else:
                    embed.set_footer(text=f'{bot.user.name} | {bot.user.id}', icon_url=f'{bot.user.avatar_url}')
                try:
                    message1 = await ctx.send(embed=embed)
                except discord.HTTPException:
                    message1 = await ctx.send(f'''Anti-Raid is disabled!\nThis channel's cooldown time has been set to 0.''')
                syslogc = bot.get_channel(SystemLogsChannelID)
                embed2 = discord.Embed(title='Anti-Raid Mode Disabled', description=f'{author.mention} has disabled anti-raid mode for this server.', color=embedcolor)
                embed2.set_author(name=f'{author}', icon_url=f'{author.avatar_url}')
                if customfooter == True:
                    embed2.set_footer(text=f'{customfootvalue}', icon_url=f'{bot.user.avatar_url}')
                else:
                    embed2.set_footer(text=f'{bot.user.name} | {bot.user.id}', icon_url=f'{bot.user.avatar_url}')
                try:
                    await syslogc.send(embed=embed2)
                except discord.HTTPException:
                    await syslogc.send(f"Anti-Raid Mode Disabled\n{author.mention} has disabled anti-raid mode for this server.")
                await asyncio.sleep(30)
                await message1.delete()
            if antiraidv == False:
                await ctx.channel.edit(slowmode_delay=0)
                embed = discord.Embed(title=f'Anti-Raid Mode', description=f'''Anti-Raid is disabled! This channel's cooldown time has been set to 0.''', color=embedcolor)
                embed.set_author(name=f'{author}', icon_url=f'{author.avatar_url}')
                if customfooter == True:
                    embed.set_footer(text=f'{customfootvalue}', icon_url=f'{bot.user.avatar_url}')
                else:
                    embed.set_footer(text=f'{bot.user.name} | {bot.user.id}', icon_url=f'{bot.user.avatar_url}')
                try:
                    message1 = await ctx.send(embed=embed)
                except discord.HTTPException:
                    message1 = await ctx.send(f"Anti-Raid is disabled!\nThis channel's cooldown time has been set to 0.")
                await asyncio.sleep(30)
                await message1.delete() 
        else:
            message5 = await ctx.send(f'{author.mention}')
            await message5.delete()
            embed5 = discord.Embed(description=f'''{author.mention}, you can't use that command!''', color=embedcolor)
            embed5.set_author(name=f'{author}', icon_url=f'{author.avatar_url}')
            if customfooter == True:
                embed5.set_footer(text=f'{customfootvalue}', icon_url=f'{bot.user.avatar_url}')
            else:
                embed5.set_footer(text=f'{bot.user.name} | {bot.user.id}', icon_url=f'{bot.user.avatar_url}')
            try:
                message6 = await ctx.send(embed=embed5)
            except discord.HTTPException:
                message6 = await ctx.send(f'''{author.mention}, **you can't use that command!**''')
            await asyncio.sleep(20)
            await message6.delete()
    except Exception as e:
        developer = bot.get_user(developerid)
        text = str('''Error on line {}'''.format(sys.exc_info()[-1].tb_lineno))
        embed = discord.Embed(title='commands.unantiraid function fail', description=f'{text}, {str(e)}', color=embedcolor)
        try:
            await developer.send(embed=embed)
        except discord.HTTPException:
            await developer.send("commands.unantiraid function fail" + str(e))
        print('[ERROR][Line {}]:'.format(sys.exc_info()[-1].tb_lineno) + f'{str(e)}')
        print("----------------------------------------") 
        await asyncio.sleep(10)

@bot.command()
async def logout(ctx):
    try:
        message1 = ctx.message
        author = ctx.message.author
        if author.id == developerid:
            await message1.add_reaction('✅')
            await bot.logout()
        else:
            await message1.delete()
            message5 = await ctx.send(f'{author.mention}')
            await message5.delete()
            embed5 = discord.Embed(description=f'''{author.mention}, you can't use that command!''', color=embedcolor)
            if customfooter == True:
                embed5.set_footer(text=f'{customfootvalue}', icon_url=f'{bot.user.avatar_url}')
            else:
                embed5.set_footer(text=f'{bot.user.name} | {bot.user.id}', icon_url=f'{bot.user.avatar_url}')
            try:
                message6 = await ctx.send(embed=embed5)
            except discord.HTTPException:
                message6 = await ctx.send(f'''{author.mention}, **you can't use that command!**''')
            await asyncio.sleep(20)
            await message6.delete()
    except Exception as e:
        developer = bot.get_user(developerid)
        text = str('''Error on line {}'''.format(sys.exc_info()[-1].tb_lineno))
        embed = discord.Embed(title='commands.logout function fail', description=f'{text}, {str(e)}', color=embedcolor)
        try:
            await developer.send(embed=embed)
        except discord.HTTPException:
            await developer.send("commands.logout function fail" + str(e))
        print('[ERROR][Line {}]:'.format(sys.exc_info()[-1].tb_lineno) + f'{str(e)}')
        print("----------------------------------------") 
        await asyncio.sleep(10)

@bot.command()
async def help(ctx):
    message1 = ctx.message
    await message1.delete()
    author = ctx.message.author
    creator = bot.get_user(387002430602346499) #DO NOT CHANGE#
    guild = ctx.guild
    try:
        text1 = str(f'''
        `{CommandPrefix}antiraid` | Enables Anti-Raid for the server
        `{CommandPrefix}unantiraid` | Disables Anti-Raid for the server
        `{CommandPrefix}help` | Gives infomation on the commands for this bot.
        `{CommandPrefix}logout` | Turns the bot off (Developer only)
        `{CommandPrefix}ping` | Shows the bot's latency miliseconds''')
        embed = discord.Embed(title=f'''**__{bot.user.name} Commands:__**''', description=f'**Command Prefix: {CommandPrefix}**', color=embedcolor)
        embed.add_field(name=f'**Commands:**', value=f'{text1}', inline=False)
        embed.set_thumbnail(url=f'{guild.icon_url}')
        embed.set_author(name=f'{author}', icon_url=f'{author.avatar_url}')
        if customfooter == True:
            embed.set_footer(text=f'{customfootvalue} | Made by {creator}', icon_url=f'{bot.user.avatar_url}')
        else:
            embed.set_footer(text=f'{bot.user.name} | Made by {creator}', icon_url=f'{bot.user.avatar_url}')
        try:
            message2 = await ctx.send(embed=embed)
        except discord.HTTPException:
            message2 = await ctx.send(f'''**__{bot.user.name} Bot Commands:__**\n**Commands:**\n''' + text1)
        await asyncio.sleep(45)
        await message2.delete()
    except Exception as e:
        developer = bot.get_user(developerid)
        text = str('''Error on line {}'''.format(sys.exc_info()[-1].tb_lineno))
        embed = discord.Embed(title='commands.help function fail', description=f'{text}, {str(e)}', color=embedcolor)
        try:
            await developer.send(embed=embed)
        except discord.HTTPException:
            await developer.send("commands.help function fail" + str(e))
        print('[ERROR][Line {}]:'.format(sys.exc_info()[-1].tb_lineno) + f'{str(e)}')
        print("----------------------------------------") 
        await asyncio.sleep(10)

@bot.command()
async def ping(ctx):
    message = ctx.message
    await message.delete()
    try:
        guild = ctx.guild
        author = ctx.message.author
        srole = get(guild.roles, id=StaffRoleID)
        if srole in author.roles:
            latency = bot.latency * 1000
            embed6 = discord.Embed(title='Ping Command!', description=f'Bot Latency ❤️: `{latency:.2f}ms`', color=embedcolor)
            if customfooter == True:
                embed6.set_footer(text=f'{customfootvalue}', icon_url=f'{bot.user.avatar_url}')
            else:
                embed6.set_footer(text=f'{bot.user.name} | {bot.user.id}', icon_url=f'{bot.user.avatar_url}')
            embed6.set_author(name=f'{author}', icon_url=author.avatar_url)
            try:
                message8 = await ctx.send(embed=embed6)
            except discord.HTTPException:
                message8 = await ctx.send(f'Bot Latency: {latency:.2f}ms ❤️')
            await asyncio.sleep(15)
            await message8.delete()
        else:
            message5 = await ctx.send(f'{author.mention}')
            await message5.delete()
            embed5 = discord.Embed(description=f'''{author.mention}, you can't use that command!''', color=embedcolor)
            embed5.set_author(name=f'{author}', icon_url=f'{author.avatar_url}')
            if customfooter == True:
                embed5.set_footer(text=f'{customfootvalue}', icon_url=f'{bot.user.avatar_url}')
            else:
                embed5.set_footer(text=f'{bot.user.name} | {bot.user.id}', icon_url=f'{bot.user.avatar_url}') 
            try:
                message6 = await ctx.send(embed=embed5)
            except discord.HTTPException:
                message6 = await ctx.send(f'''{author.mention}, **you can't use that command!**''')
            await asyncio.sleep(20)
            await message6.delete()    
    except Exception as e:
        developer = bot.get_user(developerid)
        text = str('''Error on line {}'''.format(sys.exc_info()[-1].tb_lineno))
        embed = discord.Embed(title='commands.ping function fail', description=f'{text}, {str(e)}', color=embedcolor)
        try:
            await developer.send(embed=embed)
        except discord.HTTPException:
            await developer.send("commands.ping function fail" + str(e))
        print('[ERROR][Line {}]:'.format(sys.exc_info()[-1].tb_lineno) + f'{str(e)}')
        print("----------------------------------------") 

try:
    bot.run(f'{token}')
except Exception as e:
    print('[ERROR][Line {}]:'.format(sys.exc_info()[-1].tb_lineno) + f'{str(e)}')