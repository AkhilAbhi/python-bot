from telethon.sync import TelegramClient, events

# Replace with your own values
api_id = '27376757'
api_hash = '27d4e363b3524401b62e86f1cc16c096'
bot_token = '6038826331:AAEbTWf0thTYGF2yZFEG6mJuzkdLW8YS5_M'

# Create a TelegramClient instance
client = TelegramClient('bot_session', api_id, api_hash)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Hello! I am your Telethon bot.')

@client.on(events.NewMessage(pattern='/hello'))
async def hello(event):
    await event.respond('Hello, how can I help you?')

async def main():
    # Start the
    print("starting")
    await client.start(bot_token=bot_token)
    await client.run_until_disconnected()

if __name__ == '__main__':
    client.loop.run_until_complete(main())
