import discord #We need to use discord
import winsound #We need to play the alarm
import os #OS is needed for path
from dhooks import Webhook, Embed #For discord webhoks


WordList = list
WordList = ['test' , 'Test']    #Configure this to add words that the bot will detect.

hook = Webhook('')              #Configure this to add discord alerts to a webhook.

Token = ""                      #Configure this to enable discord alert using a bot




embed = Embed(
    description='A HIGH ALERT TREATH HAS BEEN DETECTED',
    color=16711680,
    timestamp='now' 
    )


embedNoraml = Embed(
    timestamp='now' 
)

#DISCORD
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):


    if message.author == client.user:
        return

    if message.content in WordList:
        embed.add_field(name='Author', value=message.author.mention)
        embed.add_field(name='Message content', value=message.content)
        embed.add_field(name="Channal Name", value=message.channel.name)
        
        
        print("Alert")
        print(message)
        hook.send(embed=embed)
        print(message.author.mention + " " + message.content + " " + message.channel.name)

        #Alarm
        winsound.PlaySound('alarm.wav', winsound.SND_FILENAME)

        if input("Replay?") == "Yes":
            MessageToSend = input("What shood i replay?")
            await message.channel.send(MessageToSend)

            print("You" + ": " + MessageToSend + message.channel.name)


    else:
        embedNoraml.add_field(name='Author', value=message.author.mention)
        embedNoraml.add_field(name='Message content', value=message.content)
        embedNoraml.add_field(name="Channal Name", value=message.channel.name)
        hook.send(embed=embedNoraml)

        print(message.author.name + ": " + message.content + ": " + message.channel.name)





client.run(Token)
