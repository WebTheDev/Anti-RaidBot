#----Discord Anti-Raid Bot Config:----#
#----Made by: WebTheDev @ https://github.com/WebTheDev/ ----#

#Main Config:#
token = 'INSERT BOT TOKEN HERE'                 #Insert the token to your discord bot here
CommandPrefix = 'INSERT COMMAND PREFIX HERE'    #Insert the character you would like to use for the command prefix here, there is only one command.
activitytype = 'Playing'                        #Accepted Values are Watching, Listening, Playing, or Streaming.
botstatusmessage = 'INSERT STATUS MESSAGE HERE' #Insert the status message you would like to give the bot.
developerid = 0000000000000000000               #Insert the userID here were the bot will send all error dms too. THE USER MUST BE IN THE SAME DISCORD SERVER THAT THE BOT IS IN!
guildID = 0000000000000000000                   #Insert the guildID of the server that the bot will be running in here.
StaffRoleID = 0000000000000000000               #Change this value to the role in the server that will give bot perms to the anti-raid commands
SystemLogsChannelID = 0000000000000000000       #Change this value to where the bot will send all logs of commands too

#Embed Config:#
embedcolor = 0x000000                           #Change this value to the color value of the hex code that you would like the embeds the bot sends to be (KEEP THE 0x!)

customfooter = False                            #Set this the True if you like to have a custom footer at embeds            
customfootvalue = ''                            #Place the text of the custom footers

#Anti-Raid Config:
GracePeriodForKicks = 600                       #Adjust this value for the bot to look for members to kick who joined during a certain amount of time before anti-raid is enabled, default is 10 minutes, seconds only 
IncludeInviteLink = False                       #Change this to True for Yes, False for No. This allows for a discord invite to be on the message that the bot sends to a member who is kicked due to anti-raid
DiscordServerInviteLink = ''                    #Place in here the link to the discord. Use https, for example: https://discord.gg/yourvanityurl