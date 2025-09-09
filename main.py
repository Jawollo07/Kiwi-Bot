import discord
from discord.ext import commands
import random
import requests
import os
from dotenv import load_dotenv

load_env()
BOT_TOKEN=os.getenv("TOKEN",none)
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

KIWI_FACTS = [
    "Kiwis are flightless birds native to New Zealand.",
    "The kiwi is the only bird in the world with nostrils at the end of its beak.",
    "Kiwi birds lay the largest egg in relation to their body size of any bird.",
    "Kiwis are nocturnal and very shy.",
    "There are five recognized species of kiwi."
]

KIWI_JOKES = [
    "Why did the kiwi cross the road? To prove it wasn’t chicken!",
    "What do you call a bird that likes fruit? A kiwi!",
    "Why was the kiwi always invited to parties? Because it was a little birdy!",
    "What did the kiwi say to the fruit? You’re berry nice!",
]

def get_kiwi_image_url():
    # Example: Use Wikimedia Commons or Unsplash for random kiwi bird images
    images = [
        "https://upload.wikimedia.org/wikipedia/commons/5/5c/TeTuatahianui.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/1/1b/Kiwi_aka.jpg",
        "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80",
    ]
    return random.choice(images)

@bot.event
async def on_ready():
    print(f'Kiwi Bot is online as {bot.user}!')

@bot.command()
async def kiwifact(ctx):
    fact = random.choice(KIWI_FACTS)
    await ctx.send(f"🥝 **Kiwi Fact:** {fact}")

@bot.command()
async def kiwijoke(ctx):
    joke = random.choice(KIWI_JOKES)
    await ctx.send(f"😄 **Kiwi Joke:** {joke}")

@bot.command()
async def kiwiimage(ctx):
    image_url = get_kiwi_image_url()
    await ctx.send(f"🦤 **Here’s a kiwi image!**\n{image_url}")

if __name__ == '__main__':
    bot.run(BOT_TOKEN)
