from telethon import TelegramClient, events

with open("config.txt", "r") as config:
    cfg = [line.rstrip() for line in config]

client = TelegramClient('bot', int(cfg[0].strip()), cfg[1].strip()).start(bot_token=cfg[2].strip())
config.close()


@client.on(events.InlineQuery)
async def querylist(event):
    if len(event.text) > 2:
        await event.answer([event.builder.article(f'{event.text[:25]}... ¯\_(ツ)_/¯', text=f'{event.text} ¯\_(ツ)_/¯'),
                            event.builder.article(f'¯\_(ツ)_/¯ {event.text[:25]}...', text=f'¯\_(ツ)_/¯ {event.text}')])

    else:
        await event.answer([event.builder.article('¯\_(ツ)_/¯', text=f'¯\_(ツ)_/¯')])


@client.on(events.NewMessage)
async def answer(event):
    await event.reply('¯\_(ツ)_/¯')


client.start()
client.run_until_disconnected()
