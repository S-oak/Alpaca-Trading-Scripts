import os
from dotenv import load_dotenv


def load_api_keys():
    """
    Loads API credentials from a .env file or system environment variables.

    Returns:
        tuple: (API_KEY, API_SECRET)
    Raises:
        ValueError: if any required key is missing.
    """
    load_dotenv()

    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")

    if not api_key or not api_secret:
        raise ValueError("Missing API_KEY or API_SECRET in environment variables.")

    return api_key, api_secret
