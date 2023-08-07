from discord.ext.commands import Bot
import discord
import asyncio
import aiohttp
import urllib.parse
import random
import os


intents = discord.Intents.default()
intents.members = True
intents.typing = True
intents.message_content = True
intents.presences = True

bot = Bot(command_prefix=';', intents=intents)


@bot.event
async def on_ready():
    print('Hello, there.')


@bot.command(name='hi')
async def hi(ctx):
    '''

    Sends Nanashi Mumei's Oh Hi - as a video

    '''
    msg = await ctx.send('Oh Hi.')
    await ctx.send(file=discord.File('assets/oh_hi.mp4'))
    await msg.delete()


@bot.command(name='sui')
async def suisei_talala(ctx):
    '''

    Sends that Hoshimachi Suisei GIF

    '''
    await ctx.send('https://tenor.com/view/suisei-hoshimachi-suisei-vtuber-gif-26220796')


@bot.command(name='yabe')
async def yabe(ctx):
    '''

    Sends that FBK GIF

    '''
    await ctx.send('https://tenor.com/view/shirakami-fubuki-hololive-yabe-vtuber-gif-19227770')


@bot.command(name='s-manga')
async def manga_search(ctx, *args):
    '''

    Search for a Manga series.

    '''
    name = ' '.join(args)
    name = urllib.parse.quote(name)

    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://kitsu.io/api/edge/manga?filter[text]={name}') as resp:
            print(resp.status)
            response = await resp.json()

    # print(response)

    series = response['data'][0]
    print(series)

    try:
        embed = discord.Embed()
        embed.description = series['attributes']['synopsis']
        embed.title = series['attributes']['titles']['en_jp']
        embed.set_image(url=series['attributes']['posterImage']['small'])

        embed.url = f"https://kitsu.io/manga/{series['attributes']['slug']}"

        await ctx.send('Shiori~n!')
        await ctx.send(embed=embed)
    except IndexError:
        await ctx.send('Yeah, no. That didn\'t work.')
    except discord.ext.commands.errors.CommandInvokeError:
        await ctx.send('Huh, that didn\'t work. I wonder why.')


@bot.command(name='s-anime')
async def anime_search(ctx, *args):
    '''

    Search for an anime series

    '''
    name = ' '.join(args)
    name = urllib.parse.quote(name)

    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://kitsu.io/api/edge/anime?filter[text]={name}') as resp:
            print(resp.status)
            response = await resp.json()

    series = response['data'][0]
    print(series)

    try:
        embed = discord.Embed()
        embed.description = series['attributes']['synopsis']
        embed.title = series['attributes']['titles']['en_jp']
        embed.set_image(url=series['attributes']['posterImage']['small'])

        embed.url = f"https://kitsu.io/manga/{series['attributes']['slug']}"

        await ctx.send('Shiori~n!')
        await ctx.send(embed=embed)
    except IndexError:
        await ctx.send('Yeah, no. That didn\'t work.')
    except discord.ext.commands.errors.CommandInvokeError:
        await ctx.send('Huh, that didn\'t work. I wonder why.')



@bot.event
async def on_ready():
    songs = ["Utaite Covers", "Anime Openings", "Vocaloid Songs"]
    watchable = ["Vtuber Clips", "AMVs", "Domestic Girlfriend"]

    activities = [
        discord.Activity(type=discord.ActivityType.listening, name=random.choice(songs)),
        discord.Activity(type=discord.ActivityType.watching, name=random.choice(watchable))
    ]

    activity = random.choice(activities)
    await bot.change_presence(activity=activity)


if __name__ == '__main__':
    with open('.token') as f:
        token = f.read().strip()

    bot.run(token=token)