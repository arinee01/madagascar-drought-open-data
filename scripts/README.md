# Data prep scripts

These scripts document the manual preprocessing steps used in the project.

## SPI time series

Normalize the raw SPI file (semicolon-delimited, with repeated region names) into:
`docs/data/processed/spi_timeseries.csv`

```bash
python3 scripts/prepare_spi_timeseries.py
```

## Mashup CSV cleanup

Fix multi-line quoted cells and enforce quoting for text columns in:
`docs/data/processed/mashup.csv`

```bash
python3 scripts/prepare_mashup.py
```
