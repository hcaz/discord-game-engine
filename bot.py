import os
import discord
import asyncio
import random
import string

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('game'):
        client.send_typing(message.channel)
        intent = message.content[5:].split()
        if intent[0].startswith('start'):
            if intent[1].startswith('tic-tac-toe'):
                if len(intent) > 2:
                    server = message.channel.server
                    friend = intent[2]
                    await client.send_message(message.channel, 'Starting a game ' + intent[1])
                    name = 'GAME-'.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(2))
                    channel = await client.create_channel(server, name, type=discord.ChannelType.text)
                    await client.send_message(channel, 'Welcome ' + message.author + ', and ' + friend + ' to a new game of ' + intent[1])
                else:
                    await client.send_message(message.channel, 'That user does not exist')
            else:
                await client.send_message(message.channel, 'This game does not exist')
        elif intent[0].startswith('types'):
            embed=discord.Embed(title="Game Types", description="Below is a list of game types available", color=0xa709ff)
            embed.set_author(name="Game Engine", url="https://github.com/hcaz/discord-game-engine", icon_url="https://api.adorable.io/avatars/285/" + message.author.name)
            embed.set_thumbnail(url="https://image.flaticon.com/icons/svg/148/148769.svg")
            embed.add_field(name="tie-tac-toe", value="2 players", inline=False)
            embed.add_field(name="connect-four", value="2 players", inline=False)
            embed.add_field(name="chess", value="2 players", inline=True)
            embed.set_footer(text="For more help, visit the discord!")
            await client.send_message(message.channel, embed=embed)
        else:
            embed=discord.Embed(title="Help", description="This is a list of all commands available from this bot", color=0xa709ff)
            embed.set_author(name="Game Engine", url="https://github.com/hcaz/discord-game-engine", icon_url="https://api.adorable.io/avatars/285/" + message.author.name)
            embed.set_thumbnail(url="https://image.flaticon.com/icons/svg/148/148769.svg")
            embed.add_field(name="types", value="Lists all available game types", inline=False)
            embed.add_field(name="start {type} {user}", value="Starts a new game with a specific user", inline=True)
            embed.set_footer(text="For more help, visit the discord!")
            await client.send_message(message.channel, embed=embed)

client.run(os.environ['TOKEN'])