import random
import uuid
from pathlib import Path

def main():
    folder = Path(__file__).resolve().parent
    mp3_files = [f for f in folder.iterdir() if f.is_file() and f.suffix.lower() == ".mp3"]
    if not mp3_files:
        return
    # UUIDs for temporary names to prevent conflicts
    temp_files = []
    for f in mp3_files:
        temp_name = folder / f"{uuid.uuid4().hex}.mp3.tmp"
        f.rename(temp_name)
        temp_files.append(temp_name)
    random.shuffle(temp_files)
    for index, f in enumerate(temp_files, start=1):
        f.rename(folder / f"{index}.mp3")
if __name__ == "__main__":
    main()