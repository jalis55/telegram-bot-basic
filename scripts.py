from telethon import TelegramClient, events


api_id =   #number
api_hash = ''
client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage(chats = ['@PerfectMateMatch']))
async def my_event_handler(event):
    print(event.raw_text)
    #print(event.stringify())
       

client.start()
client.run_until_disconnected()