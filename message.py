import os
from dotenv import load_dotenv
import requests
import login

load_dotenv()


def send(message):

    topic = os.getenv("topic")
    requests.post(
        "https://ntfy.sh/"+topic,
        data=message,
        headers={"Title": login.username},
    )