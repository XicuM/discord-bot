# -*- coding: utf-8 -*-

from classes import TxtFiles


async def clear(now, message):
    print(now, '| Clearing ', message.channel.name)
    async for m in message.channel.history(): 
        await m.delete()


async def direct_f(now, message):
    msplit = message.content.split('"')
    for member in message.guild.members:
        if (not member.bot and msplit[1] == 'all') or member.name == msplit[1]:
            print(now, '| Sending direct message to ', member.name)
            await member.send(''.join(('Hola ', member.name, ', \n', ' '.join(msplit[2:])[1:])))


class General(TxtFiles):

    def __init__(self):
        TxtFiles.__init__(self, 'chat', 'help')

    async def act(self, now, message):
        await clear(now, message)
        print(now, '| Updating general')
        await self.send(message.channel)