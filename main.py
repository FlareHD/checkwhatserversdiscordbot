import discord


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
spaceString = " "

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# start the discord bot

@client.event
async def on_message(message):
    if message.author == client.user:
        return
#Displays total list of servers the bot is in with server IDs:
    if message.content.startswith('$servers'):
        serverListString = ""
        for guild in client.guilds:
            serverListString = serverListString + guild.name + ": " + str(guild.id) + "\n"
        await message.channel.send(serverListString)
# Displays the channels in a specified server:
    if message.content.startswith('$channels'):
        serverID = message.content.split(spaceString)[1]
        guild = client.get_guild(int(serverID))
        strChannels = "" + guild.name + "\n"
        printIDs = " " + guild.name + "\n"
#PrintIDs logs the channel name and ID to the console; whereas only sending channel names on discord:
        for channel in guild.channels:
            strChannels = strChannels + channel.name + "\n" 
            printIDs = printIDs + channel.name + " " + str(channel.id) + "\n"

        strChannels = strChannels[0:2000]
        await message.channel.send(strChannels)
        print(printIDs)
#Send a message to a discord server channel:
    channelID = ""
    content = ""
    if message.content.startswith("$send"):
        channelID = message.content.split(spaceString)[1]
        content = spaceString.join(message.content.split(spaceString)[2:])
        print(channelID)
        print(content)
        channel = client.get_channel(int(channelID))
        await channel.send(content)
#Send users a bot DM:
    userID = ""
    dmcontent = ""
    if message.content.startswith("$dm"):
        userID = message.content.split(spaceString)[1]
        dmcontent = spaceString.join(message.content.split(spaceString)[2:])
        print(userID)
        print(dmcontent)
        user = await client.fetch_user(userID)
        await user.send(dmcontent)
        await message.channel.send
# Shows DM content to bot:
    if message.guild is None and not message.author.bot:
        channel = client.get_channel(int(1251944380114141244)) # Testing channel in Flare's server
        await channel.send(f'DM from {message.author}: {message.content}')
# Leave a specified discord server:
    if message.content.startswith("$leave"):
        serverID = message.content.split(spaceString)[1]
        guild = client.get_guild(int(serverID))
        await guild.leave()
        await message.channel.send(f'Left server {guild.name}')

client.run('nonono upload ur own token')