import discord
import time

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if (message.content.count('cock') >= 1):
        await message.channel.send('cock https://media.discordapp.net/attachments/296056831514509312/659169975541432320/image0.gif')
        print('message sent: cock')
    
    if(time.strftime('%H%M').count('420') >= 1):
        await message.channel.send('cock https://media.discordapp.net/attachments/296056831514509312/659169975541432320/image0.gif')
        print('time-prompted message sent: cock')
    

client.run('Njc3NjI1NjAxNzU4MDY4ODA0.XkW-5w.UaLV0uSMsT1W1oZp92IhicpI0-I')#that string is the bot token for cock#9160