
import csv
from telethon import TelegramClient, events
from dotenv import load_dotenv
import os
import asyncio

os.environ.clear()
load_dotenv(override=True)

TELEGRAM_API_ID = os.environ.get("TELEGRAM_APP_ID")
TELEGRAM_API_HASH = os.environ.get("TELEGRAM_APP_HASH")


async def scrape_channel(client, channel_username, writer, media_dir):
    entity = await client.get_entity(channel_username)
    channel_title = entity.title
    async for message in client.iter_messages(entity, limit=1000):
        media_path = None
        if message.media and hasattr(message.media, 'photo'):
            filename = f"{channel_username}_{message.id}.jpg"
            media_path = os.path.join(media_dir, filename)

            await client.download_media(message.media, media_path)

        view = getattr(message, 'views', None)
        writer.writerow([channel_title,channel_username,message.id, message.message, message.date, media_path,view])

client = TelegramClient('session_name', TELEGRAM_API_ID, TELEGRAM_API_HASH)

async def main():
    
    await client.start()

    media_dir = "photos"
    os.makedirs(media_dir, exist_ok=True)

    with open('telegram_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Channel Title', 'Channel Username', 'Message ID', 'Message Text', 'Date', 'Media Path','View Count'])

        channels = [
            '@qnashcom',
            '@AwasMart',
            '@belaclassic',
            '@marakisat2',
            '@aradabrand2',
            '@MerttEka',
            '@kuruwear',
            '@modernshoppingcenter',
            '@Shewabrand',
            '@Leyueqa'
        ]  
        for channel in channels:
            try:
                await scrape_channel(client, channel, writer, media_dir)
                print(f"Successfully scraped channel {channel}")
            except Exception as e:
                print(f"Error scraping channel {channel}: {e}")

with client:
    client.loop.run_until_complete(main())

# asyncio.run(main())