import discord 
import json 
import messages

from discord.ext import commands 

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix = '%', intents = intents)

@bot.event
async def on_ready():
    activity = discord.Game(name='Welcome to KACD Matsuri 2021')
    await bot.change_presence(activity=activity)
    print(f'Logged in as {bot.user.name}')
    bot.add_cog(messages.Messages(bot))

def main():
    with open('config.json') as fh:
        bot.config = json.load(fh)

    bot.run(bot.config['token'])
    #bot.run(os.environ['token'])
        


if __name__ == "__main__":
    main()