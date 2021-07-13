import discord
import asyncio
import basic 
import requests
import shutil
import os
# from matplotlib import pyplot as plt 
from discord.ext import commands

class Messages(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command(name = 'send_embed', aliases = ['se'])
    async def _send_embed(self, ctx:commands.Context):

        #get ctx attributes 
        user = ctx.message.author
        channel = ctx.channel
        guild = ctx.guild

        #set title
        title = ctx.message.content
        title = title.replace(str(ctx.prefix), "")
        title = title.replace(str(ctx.invoked_with), "")

        #delete original message
        await ctx.message.delete()

        try:

            #set channel
            t_channels = guild.text_channels
            t_msg = "Pick embed color (defaults to red) for __**%s**__ \n List of available channels : " % (title)
            for i, c in enumerate(t_channels):
                t_msg += "\n *%s)* *%s*" % (i, c.name)
            t_embed = basic.mk_embed(title = "Embed Channel", msg = t_msg, color = "green") 

            s_msg = await ctx.channel.send(embed = t_embed)

            u_msg = await self.bot.wait_for('message', check = basic.check(user), timeout=60*3)

            # get channel

            channel = t_channels[int(u_msg.content.lower())]

            await s_msg.delete()
            await u_msg.delete()

            #set color
            t_msg = "Pick embed color (defaults to red) for __**%s**__ in %s \n List of available colours : " % (title, channel.name)
            for c in basic.c_palette.keys():
                t_msg += "\n *%s*" % (c) 
            t_embed = basic.mk_embed(title = "Embed Colour", msg = t_msg)

            s_msg = await ctx.channel.send(embed = t_embed)

            u_msg = await self.bot.wait_for('message', check = basic.check(user), timeout=60*3)

            color = u_msg.content.lower()

            await s_msg.delete()
            await u_msg.delete()
            

            #set image
            t_msg = "Post the image you want to embed for __**%s**__ (type skip to skip this step)\n " % (title)

            t_embed = basic.mk_embed(title = "Embed Image", msg = t_msg, color = color)

            s_msg = await ctx.channel.send(embed = t_embed)

            i_msg = await self.bot.wait_for('message', check = basic.check(user), timeout=60*3)

            if i_msg.content != "skip":

                i_url = i_msg.attachments[0].url

                img = requests.get(i_url, stream = True)
                fname = "t_img.png"
                if img.status_code == 200:
                    with open(fname, "wb") as f:
                        img.raw.decode_content = True
                        shutil.copyfileobj(img.raw, f)
                    f.close()
                    i_file = discord.File(fname)

            await s_msg.delete()

            #set message
            t_msg = "Enter the message you want to embed for __**%s**__ \n " % (title)

            t_embed = basic.mk_embed(title = "Embed Message", msg = t_msg, color = color)

            s_msg = await ctx.channel.send(embed = t_embed)

            u_msg = await self.bot.wait_for('message', check = basic.check(user), timeout=60*3)
            msg = u_msg.content

            await s_msg.delete()
            await u_msg.delete()

            embed = basic.mk_embed(title = title, msg = msg, color = color)
            try:   
                embed.set_image(url = "attachment://%s"%(fname))
            except: 
                pass
            embed.set_author(name = user.display_name, icon_url = user.avatar_url)

            try:
                await channel.send(embed = embed, file=i_file)   
            except:
                await channel.send(embed = embed)     

        except:            
            t_msg = "⛔ Sorry, couldn't post your message TwT "
            t_embed = basic.mk_embed(title = "ERROR!", msg = t_msg, color = "red")
            await ctx.channel.send(embed = t_embed)

        try:
            await i_msg.delete()
            os.remove(fname)
        except:
            print("nothing to remove")
        