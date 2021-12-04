from pathlib import Path


base_name = "day-" + "4" #input("Which day do you want to start?")

# Create subdir
p = Path(base_name)
try:
    p.mkdir(parents=False, exist_ok=False)
except FileExistsError:
    print("Day already exists!")
    exit()

# Create files
(p / ("ass-" + base_name + "-input.txt")).write_text('', encoding="utf-8")
(p / ("ass-" + base_name + ".py")).write_text('', encoding="utf-8")
(p / ("ass-" + base_name + "-2.py")).write_text('', encoding="utf-8")