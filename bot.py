import logging

import discord

BACKEND_URL = "https://charlesfrye-ask-fsdl.hf.space/run/predict"

intents = discord.Intents.default()
intents.message_content = True

TARGETED_CHANNELS = [
    1066450466898186382, # dev channel: `ask-fsdl-dev`
    1066557596313604200, # main channel: `ask-fsdl`
    984528990368825395,  # `instructor-lounge`
]


def make_client():
    client = discord.Client(intents=intents)  # connection to Discord

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        if message.channel.id not in TARGETED_CHANNELS:
            return

        if message.author == client.user:  # ignore posts by self
            return
        else:
            respondent = message.author


        if message.content.startswith('$ask-fsdl'):
            header, *content = message.content.split("$ask-fsdl")  # parse
            content =  "".join(content).strip()
            response = runner(content)  # execute
            await message.channel.send(f'{respondent.mention} {response}')  # respond

    return client


def runner(content):
    import logging

    import requests

    logging.info(f"RUNNING: {content}")

    response = requests.post(BACKEND_URL, json={
    "data": [
        f"{content}",
    ]}).json()

    text_response = response["data"][0]

    return text_response
