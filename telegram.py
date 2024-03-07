from pyrogram import Client
from pyrogram.enums import MessageMediaType
import deep_translator
from dotenv import load_dotenv
import os

load_dotenv()
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
from_id = int(os.getenv("FROM_ID"))
to_id = int(os.getenv("TO_ID"))
print("Forward messages from", from_id, "to", to_id)

app = Client("my_account", api_id, api_hash)

async def translate(text: str, lang: str = "pt"):
    translator = deep_translator.google.GoogleTranslator(source="auto", target=lang)
    return translator.translate(text)

@app.on_message()
async def my_handler(client, message):
    if message.chat.id == from_id:
        print('new message -', message)
        if message.media == MessageMediaType.PHOTO:
            # await app.send_photo(to_id, message.photo.file_id, caption=message.caption)
            text = await translate(message.caption)
            await app.send_message(to_id, text)
        text = await translate(message.text)
        await app.send_message(to_id, text)
        # await app.forward_messages(to_id, from_id, message.id)

app.run()