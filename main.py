from dotenv import load_dotenv
import requests
import os

load_dotenv()


def hello():
    url = os.getenv("BASE_URL")
    response = requests.get(url)
    print(response.json())

hello()