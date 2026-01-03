import requests
import os
import json
from pathlib import Path

def get_creds():
    kaggle_json = Path.home() / ".kaggle" / "kaggle.json"
    if kaggle_json.exists():
        with open(kaggle_json, "r") as f:
            data = json.load(f)
            return data.get("username"), data.get("key")
    return os.environ.get("KAGGLE_USERNAME"), os.environ.get("KAGGLE_KEY")

def diagnose(handle):
    username, key = get_creds()
    if not username or not key:
        print("No credentials found.")
        return

    auth = (username, key)
    base_url = "https://www.kaggle.com/api/v1"
    
    print(f"--- Diagnosing handle: {handle} ---")
    
    # Try 1: Standard segment-based URL
    owner, slug = handle.split('/')
    url1 = f"{base_url}/datasets/list/files/{owner}/{slug}"
    print(f"Trying URL 1: {url1}")
    res1 = requests.get(url1, auth=auth)
    print(f"Response 1: {res1.status_code}")
    if res1.status_code == 200:
        print("Success with URL 1!")
    
    # Try 2: Alternative (handle as a single segment)
    url2 = f"{base_url}/datasets/list/files/{handle}"
    print(f"Trying URL 2: {url2}")
    res2 = requests.get(url2, auth=auth)
    print(f"Response 2: {res2.status_code}")
    
    # Try 4: Competition File Listing (Maybe it's a competition?)
    url4 = f"{base_url}/competitions/storage/list/files/{owner}/{slug}"
    print(f"Trying Competition URL: {url4}")
    res4 = requests.get(url4, auth=auth)
    print(f"Response 4: {res4.status_code}")

    # Try 5: Datasets Listing without segments (Official Style)
    url5 = f"{base_url}/datasets/list/files/{handle}"
    print(f"Trying URL 5: {url5}")
    res5 = requests.get(url5, auth=auth)
    print(f"Response 5: {res5.status_code}")

if __name__ == "__main__":
    import sys
    handle = sys.argv[1] if len(sys.argv) > 1 else "madhavms1/titanik1"
    diagnose(handle)
