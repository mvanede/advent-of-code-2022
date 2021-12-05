from pathlib import Path


base_name = "day-" + input("Which day do you want to start?")

# Create subdir
p = Path(base_name)
try:
    p.mkdir(parents=False, exist_ok=False)
except FileExistsError:
    print("Day already exists!")
    exit()

# Create files
first_lines = """f = open("ass-{}-test-input.txt", "r")
lines = f.read().split("\\n\\n")
""".format(base_name)

(p / ("ass-" + base_name + "-input.txt")).write_text('', encoding="utf-8")
(p / ("ass-" + base_name + "-test-input.txt")).write_text('', encoding="utf-8")
(p / ("ass-" + base_name + ".py")).write_text(first_lines, encoding="utf-8")
(p / ("ass-" + base_name + "-2.py")).write_text(first_lines, encoding="utf-8")