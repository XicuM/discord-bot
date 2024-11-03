# -*- coding: utf-8 -*-

import nest_asyncio
from datetime          import datetime as dt
from discord           import Intents, Client

from src.classes       import Cron, TextChannel
from src.participar    import Participantes
from src.chat          import ChatHelp, PregData, EncData
from src.trabajo       import TrabajoData
from src.otros_canales import General, direct_f, clear

# Load token
with open('TOKEN.txt', 'r') as f:
    TOKEN = f.read().strip()

c = Cron()
print(dt.now(), '| Loading')
intents = Intents.default()
intents.members = True
client = Client(intents=intents)


# Text Channels Commands
general = TextChannel({
    '!act':       General().act
    })
participar = TextChannel({
    '!help':      lambda *x: None,
    '!unirme':    Participantes().unirme,
    '!cancel':    Participantes().cancel,
    '!fecha':     Participantes().fecha, 
    '!clear':     Participantes().clear
    })
chat = TextChannel({
    '!help':      ChatHelp().chathelp,
    '!preg -add': PregData().add,
    '!preg':      PregData().preg,
    '!enc -add':  EncData().add,
    '!enc':       EncData().enc
    })
anotaciones = TextChannel({
    '!help':      lambda *x: None,
    '!horas':     TrabajoData().horas,
    })
direct = TextChannel({
    '!dm':    direct_f
    })
testbench = TextChannel({
    '!clear':     clear
    }).copy(participar)


@client.event
async def on_ready():
    c.stop()
                

@client.event
async def on_message(message):
    
    # ignore bot messages
    if message.author == client.user:
        return
    
    # return direct messages
    elif str(message.channel.type) == 'private':
        c = Cron()
        print(dt.now(), '| Direct message by', message.author.name, 'received')
        dchannel = client.get_channel(805451244624936961)
        await dchannel.send('**'+message.author.name+':**')
        await dchannel.send(message.content)
        c.stop()
        
    # message as bot
    elif message.content.startswith('!bot') and message.author.id == 601403969163493388:
        c = Cron()
        print(dt.now(), '| Sending message as bot in', message.channel.name)
        await message.channel.send(message.content[4:])
        await message.delete()
        c.stop()
    
    # text channels commands
    else:
        await { 
            'general':     general.activate,
            'participar':  participar.activate,
            'chat':        chat.activate,
            'anotaciones': anotaciones.activate,
            'direct':      direct.activate,
            'testbench':   testbench.activate
        }.get(message.channel.name, lambda *x: None)(dt.now(), message)
    
    
@client.event
async def on_voice_state_update(member, before, after): 
    if before.channel == None and after.channel.name == 'trabajando':
        c = Cron()
        await TrabajoData().entrar(dt.now(), member)
        c.stop()
    elif before.channel.name == 'trabajando' and after.channel == None:
        c = Cron()
        await TrabajoData().salir(dt.now(), member)
        c.stop()
        
    
@client.event
async def on_member_join(member):
    c = Cron()
    print(dt.now(), '| Sending welcome message to', member.name)
    await member.send(' '.join((
        '🤗 Bienvenido a La caverna ecléctica,', 
        member.name, 
        '/nSi quieres saber más sobre el servidor, ve al canal #general de información.'
    )))
    c.stop()


nest_asyncio.apply()
client.run(TOKEN)