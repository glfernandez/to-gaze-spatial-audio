import urllib.request
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def fetch_ia_audio(query, out_filepath):
    url = f'https://archive.org/advancedsearch.php?q={urllib.parse.quote(query)}&fl[]=identifier,title&sort[]=downloads+desc&rows=5&page=1&output=json'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        response = urllib.request.urlopen(req, context=ctx)
        data = json.loads(response.read())
        docs = data.get('response', {}).get('docs', [])
        
        for doc in docs:
            identifier = doc['identifier']
            meta_url = f"https://archive.org/metadata/{identifier}"
            meta_req = urllib.request.Request(meta_url, headers={'User-Agent': 'Mozilla/5.0'})
            meta_response = urllib.request.urlopen(meta_req, context=ctx)
            meta_data = json.loads(meta_response.read())
            
            for f in meta_data.get('files', []):
                if f.get('name', '').lower().endswith(('.wav', '.flac', '.mp3', '.ogg')):
                    filename = f['name']
                    download_url = f"https://archive.org/download/{identifier}/{urllib.parse.quote(filename)}"
                    ext = filename.split('.')[-1].lower()
                    final_out = out_filepath + "." + ext
                    print(f"Downloading {identifier} to {final_out}...")
                    
                    dl_req = urllib.request.Request(download_url, headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(dl_req, context=ctx) as dl_resp, open(final_out, 'wb') as out_file:
                        out_file.write(dl_resp.read())
                    return True
    except Exception as e:
        print(f"Failed to fetch {query}: {e}")
    return False

print("Fetching real Traffic recording...")
fetch_ia_audio('subject:"traffic" AND mediatype:"audio"', 'SFX/P1_WORLD/traffic/SFX-03_TRAFFIC_CITYBED_REC_v01_RAW')

print("Fetching real Ambulance/Siren recording...")
fetch_ia_audio('subject:"siren" AND mediatype:"audio"', 'SFX/P1_WORLD/emergency/SFX-05_AMBULANCE_EMERGENCY_REC_v01_RAW')

