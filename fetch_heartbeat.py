import urllib.request
import json
import ssl
import os

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://archive.org/advancedsearch.php?q=subject:"heartbeat"+AND+mediatype:"audio"&fl[]=identifier,title&sort[]=downloads+desc&rows=5&page=1&output=json'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req, context=ctx)
data = json.loads(response.read())

docs = data.get('response', {}).get('docs', [])
if docs:
    identifier = docs[0]['identifier']
    print(f"Found IA item: {identifier}")
    
    # Get metadata to find the audio file
    meta_url = f"https://archive.org/metadata/{identifier}"
    meta_req = urllib.request.Request(meta_url, headers={'User-Agent': 'Mozilla/5.0'})
    meta_response = urllib.request.urlopen(meta_req, context=ctx)
    meta_data = json.loads(meta_response.read())
    
    files = meta_data.get('files', [])
    for f in files:
        if f.get('name', '').lower().endswith(('.wav', '.flac', '.ogg', '.mp3')):
            filename = f['name']
            download_url = f"https://archive.org/download/{identifier}/{filename}"
            print(f"Downloading from {download_url}...")
            
            ext = filename.split('.')[-1].lower()
            out_path = f"SFX/GLOBAL/heartbeat/SFX-33A_HB_CANONICAL_IA_v01_RAW.{ext}"
            
            dl_req = urllib.request.Request(download_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(dl_req, context=ctx) as dl_resp, open(out_path, 'wb') as out_file:
                out_file.write(dl_resp.read())
            print(f"Successfully downloaded to: {out_path}")
            break
else:
    print("No results found on Internet Archive.")
