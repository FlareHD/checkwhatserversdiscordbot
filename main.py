import discord


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
spaceString = " "

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$servers'):
         serverListString = ""
         str1 = ""
         for guild in client.guilds:
            str1 = str1 + guild.name + ": " + str(guild.id) + "\n"
         for guild in client.guilds:
            serverListString = serverListString + guild.name + ": " + str(guild.id) + "\n"

         await message.channel.send(str1)
         await message.channel.send(serverListString)

    if message.content.startswith('$channels'):
        serverID = message.content.split(" ")[1]
        serverID = message.content.split(spaceString)[1]
        guild = client.get_guild(int(serverID))
        strChannels = "" + guild.name + "\n"
        for channel in guild.channels:
          strChannels = strChannels + channel.name + "\n"
          strChannels = strChannels + channel.name + "\n"

        strChannels = strChannels[0:2000]
        await message.channel.send(strChannels)

    channelID = ""
    content = ""
    if message.content.startswith("$send"):
        channelID = message.content.split(" ")[1]
        content = message.content.split(" ")[2]
        channelID = message.content.split(spaceString)[1]
        content = spaceString.join(message.content.split(spaceString)[2:])
        print(channelID)
        print(content)
        channel = client.get_channel(int(channelID))
        await channel.send(content)



    

  
client.run('hahaha upload your own token sausage')