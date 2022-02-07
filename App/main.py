#   Copyright (c) 2022, VEERT00X
#   All rights reserved.


import discord      # We need this to use our discord bot.
import dhooks       # Discord - WebHooks.
import os           # We need it to access files.
import winsound     # This will play our alarm (works only on windows) (THE ALARM MUST BE A .wav FILE)
from dhooks import Embed, Webhook # Security embed

TokenFile = open("token.env", "r")
Token = TokenFile.read()

TriggerList = list
TriggerList = ['test' , 'Test']    # This words will trigger the alarm.


UseWebHooks = True     # Configure this if you want webhooks alerts.

WebHookUrl = Webhook('')    # Input your webhook url here.


DiscordClient = discord.Client()

# Script

embed = Embed(
    description='A HIGH ALERT TREATH HAS BEEN DETECTED',
    color=16711680,
    timestamp='now' 
)


embedNoraml = Embed(
    timestamp='now' 
)


def Main():

    @DiscordClient.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(DiscordClient))

    @DiscordClient.event
    async def on_message(message):


        if message.author == DiscordClient.user:
            return

        if message.content in TriggerList:
        
            if UseWebHooks == True:
                embed.add_field(name='Author', value=message.author.mention)
                embed.add_field(name='Message content', value=message.content)
                embed.add_field(name="Channal Name", value=message.channel.name)

                
                WebHookUrl.send(embed=embed)
            

            print("Alert")
            print(message)
            print(message.author.mention + " " + message.content + " " + message.channel.name)

            winsound.PlaySound('alarm.wav', winsound.SND_FILENAME)
        
        else:

            if UseWebHooks == True:
                embedNoraml.add_field(name='Author', value=message.author.mention)
                embedNoraml.add_field(name='Message content', value=message.content)
                embedNoraml.add_field(name="Channal Name", value=message.channel.name)
                WebHookUrl.send(embed=embedNoraml)

        print(message.author.name + ": " + message.content + ": " + message.channel.name)

    DiscordClient.run(Token)


Main()            


           



