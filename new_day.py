from pathlib import Path
from string import Template


year, day = input("Which year/day do you want to start?").split("/")
day = day.zfill(2)

# Create subdir
p = Path.joinpath(Path(year), "day_" + day )
try:
    p.mkdir(parents=True, exist_ok=False)
except FileExistsError:
    print("Day already exists!")
    exit()

# Create files
with open('new_day.template', 'r') as f:
    src = Template(f.read())
    t = src.substitute({'day': day})

(p / ("day_" + day + "_input.txt")).write_text('', encoding="utf-8")
(p / ("day_" + day + "_test_input.txt")).write_text('', encoding="utf-8")
(p / ("day_" + day + ".py")).write_text(t, encoding="utf-8")
(p / ("day_" + day + "_2.py")).write_text(t, encoding="utf-8")