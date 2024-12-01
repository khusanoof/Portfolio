import requests
def send_message(text):
    BOT_TOKEN = '6296896255:AAE61tZKCU1kLsKsHeDzkoQslBdPKgTtYJc'
    CHAT_ID = '5688781057'
    TEXT = text
    PHOTO = 'https://logos-world.net/wp-content/uploads/2023/03/Messages-Logo.png'
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendphoto?chat_id={CHAT_ID}&photo={PHOTO}&caption={TEXT}"
    response = requests.get(url)
