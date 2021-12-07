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
first_lines = """from utils import Parser
from utils.lib import get_timer, panswer, pruntime
_ST = get_timer()

f = open("ass-{}-test-input.txt", "r")
commands = Parser.split_by(f.read(), "\\n", conv_func=None)  # lambda x:int(x)

# CODE HERE


panswer("answer")
pruntime(_ST)


""".format(base_name)

(p / ("ass-" + base_name + "-input.txt")).write_text('', encoding="utf-8")
(p / ("ass-" + base_name + "-test-input.txt")).write_text('', encoding="utf-8")
(p / ("ass-" + base_name + ".py")).write_text(first_lines, encoding="utf-8")
(p / ("ass-" + base_name + "-2.py")).write_text(first_lines, encoding="utf-8")