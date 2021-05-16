### Discord-AntiRaidBot
- A discord bot that is designed to contain and manage chat raids/spams within a discord server!
- Designed and Tested on Python 3.7.3 for Linux and Windows
- If you would like a custom version of this bot please create a ticket in my [discord](https://discord.gg/kejhHFrA9t)!

<p align="center">
  <img height="186" width="585" alt="" src="https://media.discordapp.net/attachments/828110039956455444/843594317763313734/unknown.png" />
</p>

---
### Features:
- With the Anti-Raid enabled, this bot will auto-kick all new members automatically upon joining of your server. Allowing you to keep all of your discord invite links active!
- Upon running the command to enable Anti-Raid, the bot will auto-kick all new members who joined within the last 10 minutes (this value can be adjusted in the [config.py](https://github.com/WebTheDev/Anti-RaidBot/blob/main/config.py) file). 
- Simple permissions system for use of the antiraid commands.
- Auto 5 Minute slowmode for channel that the antiraid command is executed in. (Will be removed upon running disable antiraid command)
- DM's Member on Auto-Kick
- Custom Embed Footers
- Logging for all Auto-Kicks and use of the Anti-Raid system.
- Customizable bot status. 
- Ping and Logout Commands.
- A couple other "easter eggs". 

---
### [Python](https://www.python.org/downloads/) Packages Required (Install with [Pip](https://pip.pypa.io/en/stable/installing/)):
- [Discord](https://pypi.org/project/discord.py/)
- [Asyncio](https://pypi.org/project/asyncio/) (If not already installed)
---
### Setup
- Place "[main.py](https://github.com/WebTheDev/Anti-RaidBot/blob/main/main.py)" and "[config.py](https://github.com/WebTheDev/Anti-RaidBot/blob/main/config.py)" into a folder (this is too allow the bot to be able to find the "[config.py](https://github.com/WebTheDev/Anti-RaidBot/blob/main/config.py)" file.)

- Create a bot application at the [discord developer panel](https://discord.com/developers/applications) and add to your discord server.

- Allow the "Server Member Intent" under the "Privileged Gateway Intents" in the [discord developer panel](https://discord.com/developers/applications). (THIS IS VERY IMPORTANT! The bot will not work propertly without and will not be able to find or kick server members.)

- Place your bot token and adjust the "[config.py](https://github.com/WebTheDev/Anti-RaidBot/blob/main/config.py)" to your liking.

- Start the bot and watch the magic happen! (For windows right click on the main.py and click open, a cmd panel should appear. For linux, choose a starting resource that is best for your linux environment.) 
---
### Support
- If you need further support with setting up this bot or find unknown errors you would like to report. Please either ask for support in my [discord](https://discord.gg/kejhHFrA9t) or open a new [issue](https://github.com/WebTheDev/serverstatsbot/issues).
---
### Known Errors:
Listed below are known errors that can not be solved due to discord limiations not software bugs:
- Task Run Errors.
- Discord Related Errors.
- Ratelimits (similar to dyno or carl), discord only allows you to do so much at once. This can result in the antiraid command or kicking members to be a bit laggy. The bigger the server, the more likely that the bot can be a bit laggy. 
