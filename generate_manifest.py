import os, json, re

# Define the root where SFX folders reside (relative to this script)
workspace_root = os.path.abspath(os.path.join(os.path.dirname(__file__), 'SFX'))
manifest = {}

# Pattern to capture SFX ID and version number
pattern = re.compile(r'(SFX-\d+[A-Z]?)_REC_v(\d{2})_RAW\.wav')

for root, dirs, files in os.walk(workspace_root):
    for f in files:
        m = pattern.match(f)
        if not m:
            continue
        sfx_id, ver_str = m.group(1), m.group(2)
        ver = int(ver_str)
        rel_path = os.path.relpath(os.path.join(root, f), start=os.path.dirname(__file__))
        rel_path = rel_path.replace(os.sep, '/')
        entry = manifest.setdefault(sfx_id, {"opt1": null, "opt2": null, "opt3": null})
        if ver == 1:
            entry["opt1"] = rel_path
        elif ver == 2:
            entry["opt2"] = rel_path
        elif ver == 3:
            entry["opt3"] = rel_path

out_path = os.path.join(os.path.dirname(__file__), 'sfx_manifest.json')
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=2)
print(f"Manifest written to {out_path}")
