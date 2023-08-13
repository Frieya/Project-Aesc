# bot.py
import os
import discord
from dotenv import load_dotenv
import openai


load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
OPENAI_KEY = os.getenv('OPENAI_KEY')

# Set up the OpenAI API client
openai.api_key = OPENAI_KEY

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)

@client.event
async def on_message(message):
# Only respond to messages from other users, not from the bot itself
  if message.author == client.user:
    return
  # Use the OpenAI API to generate a response to the message
  response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=f"{message.content}",
  max_tokens=2048,
  temperature=0.5,
  )
  # Send the response as a message
  await message.channel.send(response.choices[0].text)

# Start the bot
client.run("DISCORD_BOT_TOKEN")