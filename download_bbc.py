import urllib.request
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# API for BBC Sound Effects is https://r.bbcsounds.co.uk
# Actually I'll just download a couple of high quality known CC0 youtube videos for "City Traffic Ambient" and "Ambulance Siren" and "Mouse Clicks".
# I'll use yt-dlp to grab CC0 / royalty free clips to prove it.
