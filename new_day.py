from pathlib import Path

year, day = input("Which year/day do you want to start?").split("/")
base_name = "day_" + day

# Create subdir
p = Path.joinpath(Path(year), base_name)
try:
    p.mkdir(parents=True, exist_ok=False)
except FileExistsError:
    print("Day already exists!")
    exit()

# Create files
first_lines = """from utils import Parser
from utils.lib import get_timer, panswer, pruntime
_ST = get_timer()

f = open("ass_{}_test_input.txt", "r")
commands = Parser.split_by(f.read(), "\\n", conv_func=None)  # lambda x:int(x)

# CODE HERE


panswer("answer")
pruntime(_ST)


""".format(base_name)

(p / ("ass_" + base_name + "_input.txt")).write_text('', encoding="utf-8")
(p / ("ass_" + base_name + "_test_input.txt")).write_text('', encoding="utf-8")
(p / ("ass_" + base_name + ".py")).write_text(first_lines, encoding="utf-8")
(p / ("ass_" + base_name + "_2.py")).write_text(first_lines, encoding="utf-8")