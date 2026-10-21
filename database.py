import requests
import json
import base64
from cryptography.fernet import Fernet
from src.api import GIT, KEY

fernet = Fernet(KEY)

def upload_github(data):
    if not GIT:
        raise RuntimeError("GITHUB_TOKEN is not set")

    url = 'https://api.github.com/repos/Sinaksh0/warp-config/contents/rich_message/rich_users.json'
    headers = {
        "Authorization": f"Bearer {GIT}",
        "Accept": "application/vnd.github+json"
    }

    payload = json.dumps({
        "count": len(data),
        "users": data
        }, 
        ensure_ascii=False).encode('utf-8')
    encrypt = fernet.encrypt(payload)
    encoded = base64.b64encode(encrypt).decode("utf-8")

    resp = requests.get(url, headers=headers, timeout=20)

    body = {
        "message": "Auto updating users",
        "content": encoded,
        "branch": "main"
    }

    if resp.status_code == 200:
        body["sha"] = resp.json().get("sha")

    requests.put(url, headers=headers, json=body, timeout=20)
    return

def load_users() -> list:
    url = 'https://raw.githubusercontent.com/Sinaksh0/warp-config/refs/heads/main/rich_message/rich_users.json'
    try:
        response = requests.get(url, timeout=15)
        if response.status_code != 200:
            return []

        body = response.text.strip()

        if not body:
            return []

        try:
            decrypt = fernet.decrypt(body).decode()
            data = json.loads(decrypt)
        except ValueError:
            try:
                decoded = base64.b64decode(body)
                decrypt = fernet.decrypt(decoded).decode('utf-8')
                data = json.loads(decrypt)
            except Exception:
                return []

        return data["users"]
    except requests.RequestException:
        return []
