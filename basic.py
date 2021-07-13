import discord 
import json

c_palette  = {
    'red': 0xED254E,
    'black': 0x040404,
    'white': 0xEBEBEB,
    'green': 0x04D243,
    'yellow': 0xFFA400,
    'blue': 0x4A7B9D,
    'grey': 0x747474

}

def check(author):
    def inner_check(message):
        print('too gay')
        return message.author == author 
    return inner_check

def mk_embed(title = "", msg = "", color = 'red'):
    return discord.Embed(title = title, description = msg, color = c_palette[color])