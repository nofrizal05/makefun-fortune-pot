"""Fortune in a Pot — make.fun entry.

Writes one kind, funny fortune for the houseplant on the windowsill
to /output/entry.txt (one line, at most 120 characters).
Standard library only.
"""

import os

FORTUNE = "By spring, you will outgrow this windowsill, and the sun will book an appointment just to bask in your shade."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(FORTUNE + "\n")
