import urllib.request
import json

API_URL = "https://api-inference.huggingface.co/models/cvssp/audioldm-m-full"
headers = {"Content-Type": "application/json"}
data = {"inputs": "Dense contemporary urban traffic from street level, distant engines."}

req = urllib.request.Request(API_URL, headers=headers, data=json.dumps(data).encode('utf-8'))
try:
    with urllib.request.urlopen(req) as response:
        audio = response.read()
        with open("test_traffic.flac", "wb") as f:
            f.write(audio)
        print("Success! Downloaded via free API.")
except urllib.error.HTTPError as e:
    print(f"Failed with {e.code}: {e.read().decode('utf-8')}")
