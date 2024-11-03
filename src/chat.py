# -*- coding: utf-8 -*-


from classes import JsonFile, TxtFiles
from numpy.random import randint


class ChatHelp(TxtFiles):

    def __init__(self):
        TxtFiles.__init__(self, 'chat', 'help')

    def chathelp(self, now, message):
        print(now, '|', message.author.name, 'is requesting chat help')
        self.send(message.channel)


class PregData(JsonFile):
    
    def __init__(self):
        JsonFile.__init__(self, 'chat', 'preguntas.json')
        
    async def preg(self, now, message):
        print(now, '|', message.author.name, 'is requesting a question')
        self.load()
        
        m = message.content
        if m.split(' ')[1] == 'random':
            lista = []
            for tema in self.file.values():
                lista.extend(tema)
            i = randint(len(lista))
            await message.channel.send(lista[i])
        else:
            lista = self.file.get(m.split(' ')[1], None)
            if lista is None:
                await message.channel.send('**Error:** Tema no encontrado')
            else:
                i = randint(len(lista))
                await message.channel.send(lista[i])
            
    async def add(self, now, message):
        print(now, '| Adding new question')
        self.load()
        m = message.content
        self.file[m.split(' ')[2]].append(m.split('"')[1])
        self.save()


class EncData(JsonFile):
    
    def __init__(self):
        JsonFile.__init__(self, 'chat', 'encuestas.json')
    
    async def enc(self, now, message):
        print(now, '|', message.author.name, 'is requesting a poll')
        self.load()
    
        lista = self.file['random']
        i = randint(len(lista))
        await message.channel.send('***ENCUESTA***\nEscoge tu respuesta favorita:')
        for opcion in lista[i]:
            await message.channel.send(''.join(('```', opcion, '```')))
                
    async def add(self, now, message):
        print(now, '| Adding new poll')
        self.load()
        self.file['random'].append(message.content.split('"')[1].split(', '))
        self.save()