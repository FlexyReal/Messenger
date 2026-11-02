import os
from dotenv import load_dotenv
import requests

load_dotenv()

topic = os.getenv("topic")

requests.post(
    f"https://ntfy.sh/{topic}",
    data="Oh my ...",
    #headers={"Title": "Dogs are better than cats"},
)