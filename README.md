# Open Data Analysis of Drought in Madagascar

The project explores the reuse of open datasets to analyze spatial and temporal
patterns of drought and water stress in Madagascar, with particular attention to
legal, ethical, and technical aspects of open data reuse.

## Project structure
```text
/data
  /raw        # original datasets (or references)
/docs         # one-page website (GitHub Pages), processed data, RDF mirror
/rdf          # DCAT-AP metadata and RDF files
/scripts      # data processing scripts
```


## Methodology

The project combines multiple open datasets published by international organizations
(e.g. Copernicus, GPCC/DWD, World Bank, geoBoundaries) to produce an aggregated
mash-up dataset at regional level. The workflow includes data selection, quality
assessment, legal and ethical analysis, and publication as Linked Open Data.

## Data structure

- `data/raw/` — original datasets as downloaded from official sources
- `docs/data/processed/` — curated and aggregated datasets used for visualization
- `scripts/` — scripts used to prepare mash-up and time series
- `docs/` — one-page website and RDF metadata (DCAT-AP)

## Data preparation scripts

Key normalization steps are documented as scripts in `scripts/`:

- `scripts/prepare_mashup.py` cleans multi-line CSV cells and enforces quoting.
- `scripts/prepare_spi_timeseries.py` normalizes SPI time series to 2024 data.

## Open data and licenses

Original datasets are reused according to their respective licenses.
The mash-up dataset and the project documentation are published under open licenses.
The source code is released under the MIT License.

## Website

The results of the project, including documentation, visualizations, and metadata,
are published as a one-page website using GitHub Pages.

## Disclaimer

This project uses aggregated data and does not contain personal data.
The analysis is descriptive and does not imply causal relationships or predictions.
