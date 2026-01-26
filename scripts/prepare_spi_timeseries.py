#!/usr/bin/env python3
import csv
from pathlib import Path

# Normalize SPI time series into CSV with region_name,date,spi
# - Fills missing region names from previous row
# - Keeps only rows from 2024
# - Normalizes region names to match regions.geojson

SRC = Path("docs/data/processed/spi_timeseries.csv")
OUT = Path("docs/data/processed/spi_timeseries.csv")

NAME_MAP = {
    "Alaotra Mangoro": "Alaotra-Mangoro",
    "Amoron I Mania": "Amoron'i Mania",
    "Analajifora": "Analanjirofo",
    "Atsimo Andrefana": "Atsimo-Andrefana",
    "Atsimo Atsinanana": "Atsimo-Atsinanana",
    "Haute Matsiatra": "Matsiatra Ambony",
    "Vatovavy Fitovinany": "Vatovavy-Fitovinany",
}


def main() -> None:
    raw_lines = SRC.read_text().splitlines()
    rows = []
    current_region = None

    for line in raw_lines:
        if not line.strip():
            continue
        parts = line.split(";")
        while parts and parts[-1] == "":
            parts.pop()
        if not parts:
            continue
        if parts[0].strip().lower() == "regions":
            continue

        region = parts[0].strip()
        date = parts[1].strip() if len(parts) > 1 else ""
        value = parts[2].strip() if len(parts) > 2 else ""

        if region:
            current_region = region

        if not current_region or not date:
            continue

        if not date.startswith("2024-"):
            continue

        region_name = NAME_MAP.get(current_region, current_region)
        rows.append({"region_name": region_name, "date": date, "spi": value})

    with OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["region_name", "date", "spi"], lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
