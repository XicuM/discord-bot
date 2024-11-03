# -*- coding: utf-8 -*-

from classes import JsonFile
from time import time


class TrabajoData(JsonFile):
    
    def __init__(self):
        JsonFile.__init__(self, 'trabajo', 'trabajo.json')


    def get_rol(self, horas):
        if   horas>=5040: return {'name': 'maestro vital', 'id': 807190805000618004}
        elif horas>= 720: return {'name':       'magnate', 'id': 807192335699279882}
        elif horas>= 120: return {'name':    'empresario', 'id': 807192300702007296}
        elif horas>=  24: return {'name':   'emprendedor', 'id': 807192280640913449}
        elif horas>=   6: return {'name':       'padawan', 'id': 807191639649943552}
        elif horas>=   2: return {'name':      'iniciado', 'id': 807191452047638559}
        elif horas>=   1: return {'name':        'novato', 'id': 805140610881028166}
        else:             return {'name':          'nini', 'id': None}


    async def act_horas(self, member, hora):    
        hora_in = float(self.file[str(member.id)]['in'])
        horas = float(self.file[str(member.id)]['horas'])
        old_rol = self.file[str(member.id)]['rol']
        
        self.file[str(member.id)]['in'] = str(hora)
        total = horas + hora - hora_in
        self.file[str(member.id)]['horas'] = str(total)
        new_rol = self.get_rol(total)
        if old_rol != new_rol:
            self.file[str(member.id)]['rol'] = new_rol
            if old_rol['id'] is not None:
                await member.remove_roles(member.guild.get_role(old_rol['id']))
            await member.add_roles(member.guild.get_role(new_rol['id']))
        
        
    async def horas(self, now, message):
        print(now, '|', message.author.name, 'is requesting worked hours')
        self.load()
        member = message.author
        
        if str(member.id) in self.file:
            if member.voice is None:
                self.file[str(member.id)]['in'] = None
            else:
                await self.act_horas(member, time()/3600)
        else:
            self.file[str(member.id)] = {'in': str(time()/3600), 'horas': '0', 'rol': {'name': 'nini', 'id': None}}
        
        total = str(int(float(self.file[str(member.id)]['horas'])))
        total += ' hora' + 's'*(total!='1')
        rol_name = self.file[str(member.id)]['rol']['name']
        await message.channel.send(''.join(('**', message.author.name, ':** ', 'Llevas ', total, ' trabajadas. Eres un **', rol_name, '**.')))
        self.save()


    async def entrar(self, now, member):
        print(now, '|', member.name, 'started working')
        self.load()
        if str(member.id) in self.file:
            self.file[str(member.id)]['in'] = str(time()/3600)
        else:
            self.file[str(member.id)] = {'in': str(time()/3600), 'horas': '0', 'rol': {'name': 'nini', 'id': None}}
        self.save()
        
        
    async def salir(self, now, member):
        print(now, '|', member.name, 'ended working')
        self.load()
        await self.act_horas(member, time()/3600)
        self.file[str(member.id)]['in'] = None
        self.save()