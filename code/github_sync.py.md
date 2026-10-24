# publisher/github_sync.py
import subprocess
import json
import os

def save_to_github(data, filename):
    path = f"../agrix-knowledge-base/{filename}"
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

    subprocess.run(["git", "add", path])
    subprocess.run(["git", "commit", "-m", f"Add {filename}"])
    subprocess.run(["git", "push"])