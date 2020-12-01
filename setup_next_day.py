import shutil
from pathlib import Path

last_day_folder = str(sorted(Path(".").glob("day*"))[-1])
prev_day = int(last_day_folder.replace("day", "").lstrip("0") or 0)
shutil.copytree("day00", f"day{prev_day+1:02d}")
