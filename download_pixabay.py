import urllib.request
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def fetch_pixabay(query, filename):
    url = f"https://pixabay.com/api/audio/?key=YOUR_KEY&q={urllib.parse.quote(query)}"
    # Wait, I don't have a pixabay key. 
    pass
