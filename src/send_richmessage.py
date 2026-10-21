import aiohttp
from src.api import TELEGRAM_API

async def send_rich_message(chat_id: int, html_content: str, method: str, reply_markup=None, message_id: int = None, rtl: bool = True):
    url = f"{TELEGRAM_API}/{method}"
    payload = {
        "chat_id": chat_id,
        "rich_message": {
            "html": html_content.strip(),
            "is_rtl": rtl
        }
    }

    if reply_markup:
        payload['reply_markup'] = reply_markup

    if message_id:
         payload['message_id'] = message_id
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as response:
                if not response.ok:
                     error = response.text()
                     await session.post(f'{TELEGRAM_API}/sendMessage', json={
                          "chat_id": chat_id,
                          "text": f"⚠️ Error ({response.status}): {error}"
                    })      
    return
