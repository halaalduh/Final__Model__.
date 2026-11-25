"""Minimal Python example for the Khota API."""
import argparse
import json
from mimetypes import guess_type
from pathlib import Path

import requests

API = "http://localhost:8000"
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("photo", type=Path, help="Path to a local image")
args = parser.parse_args()
PHOTO = args.photo
CONTENT_TYPE = guess_type(PHOTO)[0] or "application/octet-stream"

print(requests.get(f"{API}/health", timeout=10).json())
with PHOTO.open("rb") as f:
    r = requests.post(f"{API}/predict", files={"image": (PHOTO.name, f, CONTENT_TYPE)}, timeout=120)
r.raise_for_status()
result = r.json()
print(result["model_version"], result["result"])
for d in result["defects"]:
    print(d["class"], d["severity"], d["box_xyxy"], d["confidence"])

# detection model only (no severity)
with PHOTO.open("rb") as f:
    det = requests.post(f"{API}/detect", files={"image": (PHOTO.name, f, CONTENT_TYPE)}, timeout=120).json()

# severity model only, for boxes you already have (pixels of the photo, e.g. det["defects"][i]["box_xyxy"])
boxes = [d["box_xyxy"] for d in det["defects"]]
if boxes:
    with PHOTO.open("rb") as f:
        sev = requests.post(f"{API}/severity", files={"image": (PHOTO.name, f, CONTENT_TYPE)},
                            data={"boxes": json.dumps(boxes)}, timeout=120).json()
    for d in sev["defects"]:
        print(d["box_xyxy"], d["severity"], d["p_high"])
