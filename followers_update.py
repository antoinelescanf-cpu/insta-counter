import requests
import json

USERNAME = "veterinaires.lannion.sevetys"
JSON_FILE = "followers.json"
URL = f"https://www.instagram.com/{USERNAME}/?__a=1&__d=dis"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def get_followers():
    try:
        response = requests.get(URL, headers=HEADERS, timeout=10)
        response.raise_for_status()
        data = response.json()
        followers = data['graphql']['user']['edge_followed_by']['count']
        return followers
    except Exception as e:
        print("Erreur:", e)
        return None

def update_json(followers):
    if followers is not None:
        with open(JSON_FILE, "w") as f:
            json.dump({"followers": followers}, f)
        print(f"Mise à jour : {followers} followers")
    else:
        print("Mise à jour échouée.")

if __name__ == "__main__":
    followers_count = get_followers()
    update_json(followers_count)
