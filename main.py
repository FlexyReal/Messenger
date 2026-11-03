import os
from dotenv import load_dotenv
import requests

load_dotenv()

topic = os.getenv("topic")

requests.post(
    "https://ntfy.sh/"+topic,
    data=" ",
    headers={"Title": "Grueße!"},
)