TOKEN = #Insert your server token here!
import discord
import requests
import json


client = discord.Client()

def get_promise():
	promise = requests.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=twopart")
	json_data = dict(json.loads(promise.text))

	promise = json_data["setup"] +  " " + json_data["delivery"]

	return promise

@client.event

async def on_ready():
	print("We have logged in as {0.user}".format(client))


@client.event

async def on_message(message):
	if message.author == client.user:
		return None
	if message.content.startswith("$joke"):
		promise = get_promise()
		await message.channel.send(promise)



client.run(TOKEN)


