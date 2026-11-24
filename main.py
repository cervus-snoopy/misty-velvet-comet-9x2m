#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply (R2).

Writes a single out-of-office auto-reply line to
$MAKEFUN_OUTPUT_DIR/entry.txt.
"""
import os
import sys

LINE = "Out of office. This auto-reply has promoted you to inbox manager. Your first ticket is the email you just sent. Salary: exposure to my inbox."

def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    os.chmod(out_dir, 0o755)
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == LINE
        assert 1 <= len(LINE) <= 159

if __name__ == "__main__":
    main()
