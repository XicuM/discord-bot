# -*- coding: utf-8 -*-

from classes import JsonFile


class Participantes(JsonFile):
    
    def __init__(self):
        JsonFile.__init__(self, 'participar', 'participar.json')
        self.numbers = ['⠀⠀1️⃣ ', '⠀⠀2️⃣ ', '⠀⠀3️⃣ ', '⠀⠀4️⃣ ']
        self.message = ''
        
        
    async def unirme(self, now, message):
        print(now, '|', message.author.name, 'has confirmed participation')
        self.load()
        member = message.author
        
        if len(self.file['participantes']) == 4:
            self.message = '😅 Número máximo de participantes alcanzado.\n✅ ¡Apúntate en la próxima sesión!\n⠀\n'
        else:
            if str(member.id) not in self.file['participantes']:
                self.file['participantes'][str(member.id)] = member.name
            else:
                self.message = 'Ya estás participando... ¿No querrás hablar contigo mismo?\n⠀\n'
            
        await self.update(message.channel)
        
        
    async def cancel(self, now, message):
        print(now, '|', message.author.name, 'has canceled participation')
        self.load()
        member = message.author
        
        if str(member.id) in self.file['participantes']:
            del self.file['participantes'][str(member.id)]
            self.message = 'Listo, ya no participas en la próxima sesión. ¡Espero verte pronto! \n⠀\n'
        else:
            self.message = 'No estás participando 🤯\n⠀\n'
                
        await self.update(message.channel)
        
        
    async def fecha(self, now, message):
        print(now, '| Setting new session date')
        self.load()
        self.file['fecha'] = message.content.split('"')[1]
        
        if self.file['fecha'] != 'sin especificar':
            for member in message.guild.members:
                if not member.bot:
                    print(now, '| Sending direct message to ', member.name)
                    await member.send(''.join(('Hola ', member.name, ', \nLa próxima sesión de Revolutions será el ', self.file['fecha'], '.\n¡Espero poder verte pronto!')))
            self.message = '¡Nueva fecha para la siguiente sesión!\n⠀\n'
        
        await self.update(message.channel)  
        
        
    async def clear(self, now, message):
        print(now, '| Clearing participations')
        if message.author.id == 601403969163493388:
            async for i in message.channel.history():
                await i.delete()
            self.file = {'fecha': 'sin especificar', 'participantes': {}}
            self.save()
            
    
    async def update(self, channel):
        self.message += '*PRÓXIMA SESIÓN*\n**Fecha:** ' + self.file['fecha'] + '\n**Participantes (4 max):**\n'
        for i, name in enumerate(self.file['participantes'].values()):
            self.message += '⠀'.join((self.numbers[i], name))
        await channel.send(self.message)
        self.message = ''
        self.save()