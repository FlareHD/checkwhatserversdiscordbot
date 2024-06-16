import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$servers'):
         str1 = ""
         for guild in client.guilds:
            str1 = str1 + guild.name + ": " + str(guild.id) + "\n"

         await message.channel.send(str1)

    if message.content.startswith('$channels'):
        serverID = message.content.split(" ")[1]
        guild = client.get_guild(int(serverID))
        strChannels = "" + guild.name + "\n"
        for channel in guild.channels:
          strChannels = strChannels + channel.name + "\n"

        strChannels = strChannels[0:2000]
        await message.channel.send(strChannels)

    channelID = ""
    content = ""
    if message.content.startswith("$send"):
        channelID = message.content.split(" ")[1]
        content = message.content.split(" ")[2]
        print(channelID)
        print(content)
        channel = client.get_channel(int(channelID))
        await channel.send(content)
    

  
client.run('add ur own token here silly')