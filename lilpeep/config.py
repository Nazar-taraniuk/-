from dotenv import load_dotenv, find_dotenv
import os


def get_token():
    load_dotenv(find_dotenv())
    token = os.getenv('token')

    if not token:
        raise ValueError("not .env")
    return token
