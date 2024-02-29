from pyrogram import Client


api_id = 20288082
api_hash = "7a4dd2b78620362f1fab3c3422eee24b"
print('\nID Chat')
# from_id = input('From:')
# to_id = input('To:')
from_id = -1001287170333
to_id = 1128002511

app = Client("my_account", api_id, api_hash)


@app.on_message()
async def my_handler(client, message):
    if message.chat.id == from_id:
        print(message.chat.id, message.text)
        await app.send_message(to_id, message.text)
        # await app.forward_messages(to_id, from_id, message.id)

app.run()