import requests
from pyrogram import Client, filters
from pyrogram.enums import ChatAction
from SONALI_MUSIC import app  # बॉट का एप्लिकेशन इंपोर्ट करें

@app.on_message(filters.command("ask"))
async def fetch_med_info(client, message):
    query = " ".join(message.command[1:]) if len(message.command) > 1 else None
    if not query:
        await message.reply_text("**ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ǫᴜᴇʀʏ ᴛᴏ ᴀsᴋ.**")
        return

    await client.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)

    api_url = f"https://chatwithai.codesearch.workers.dev/?chat={query}"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            reply = data.get("data", "**sᴏʀʀʏ, ɪ ᴄᴏᴜʟᴅɴ'ᴛ ғᴇᴛᴄʜ ᴛʜᴇ ᴅᴀᴛᴀ.**")
        else:
            reply = "**ғᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ ᴅᴀᴛᴀ ғʀᴏᴍ ᴛʜᴇ ᴀᴘɪ.**"
    except Exception as e:
        reply = f"**ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ :** {e}"

    reply += "\n\n**❍ ᴀɴsᴡᴇʀ ʙʏ :- @Sonali_Music_Bot**"
    await message.reply_text(reply)

@app.on_message(filters.mentioned & filters.group)
async def fetch_med_info_group(client, message):
    query = message.text.replace(f"@{client.me.username}", "").strip()
    if not query:
        await message.reply_text("**ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴍᴇᴅɪᴄᴀʟ ǫᴜᴇʀʏ ᴛᴏ ᴀsᴋ.**")
        return

    await client.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)

    api_url = f"https://chatwithai.codesearch.workers.dev/?chat={query}"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            reply = data.get("data", "**sᴏʀʀʏ, ɪ ᴄᴏᴜʟᴅɴ'ᴛ ғᴇᴛᴄʜ ᴛʜᴇ ᴅᴀᴛᴀ.**")
        else:
            reply = "**ғᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ ᴅᴀᴛᴀ ғʀᴏᴍ ᴛʜᴇ ᴀᴘɪ.**"
    except Exception as e:
        reply = f"**ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ :** {e}"

    reply += "\n\n**❍ ᴀɴsᴡᴇʀ ʙʏ :- @Sonali_Music_Bot**"
    await message.reply_text(reply)
