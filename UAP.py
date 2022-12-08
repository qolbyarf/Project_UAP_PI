import json, requests

headers = {
    "Content-Type": "application/json",
    "Tracking-Api-Key": "v83qnksa-b42c-vnfw-f68f-gh4sw90lx5kl"
}

track = requests.get('https://api.trackingmore.com/v4/trackings/get', headers=headers)

track = track.json()

track['data']
