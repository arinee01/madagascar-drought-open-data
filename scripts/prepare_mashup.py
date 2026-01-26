#!/usr/bin/env python3
import csv
from pathlib import Path

# Normalize mashup.csv so quoted text stays on one line and text fields are quoted.

SRC = Path("docs/data/processed/mashup.csv")
OUT = Path("docs/data/processed/mashup.csv")


def main() -> None:
    rows = []
    with SRC.open(newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue
            cleaned = []
            for cell in row:
                text = cell.replace("\r", "\n").replace("\n", " ").strip()
                cleaned.append(text)
            rows.append(cleaned)

    if not rows:
        return

    quote_cols = {7, 8, 9, 10}
    lines = []
    for r, row in enumerate(rows):
        out_cells = []
        for i, cell in enumerate(row):
            if r == 0:
                out_cells.append(cell)
                continue
            if i in quote_cols:
                cell = cell.replace('"', '""')
                out_cells.append(f"\"{cell}\"")
            else:
                out_cells.append(cell)
        lines.append(",".join(out_cells))

    OUT.write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
