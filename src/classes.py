# -*- coding: utf-8 -*-

from os import listdir
from time import time
from os.path import join
from json import load, dump


class Cron(object):
    
    def __init__(self):
        self.start = time()
    
    def stop(self):
        print('DONE %.4f' % (time()-self.start), 's\n')
        

class JsonFile(object):
    
    def __init__(self, *path):
        self.path = join('data', *path)
        self.file = None
        
    def load(self):
        with open(self.path, 'r', encoding='utf8') as f:
            self.file = load(f)
            
    def save(self):
        with open(self.path, 'w', encoding='utf8') as f:
            dump(self.file, f, indent=4)
        self.file = None


class TxtFiles(object):
    
    def __init__(self, *path):
        self.path = join('data', *path)
        self.files = []
        
    def load(self):
        for file in sorted(listdir(self.path)):
            with open(join(self.path, file), 'r', encoding='utf8') as f:
                self.files.append(f.read())
    
    def save(self):
        for file in self.file:
            with open(join(self.path, file), 'r', encoding='utf8') as f:
                self.files.append(f.read())
    
    async def send(self, channel):
        self.load()
        for file in self.files:
            await channel.send(file)


class TextChannel(object):
    
    def __init__(self, commands):
        self.commands = commands
        
    def copy(self, *textchannels):
        for textchannel in textchannels:
            self.commands.update(textchannel.commands)
        return self
    
    async def activate(self, now, message):
        for command in self.commands:
            if message.content.startswith(command):
                c = Cron()
                await self.commands[command](now, message)
                c.stop()
                break