# Open Data Analysis of Drought in Madagascar

This repository contains a student project developed for the course
**Open Access and Digital Ethics (CFU 6)** held by Monica Palmirani.

The project explores the reuse of open datasets to analyze spatial and temporal
patterns of drought and water stress in Madagascar, with particular attention to
legal, ethical, and technical aspects of open data reuse.

## Project structure



/data
/raw # original datasets (or references)
/processed # mash-up output datasets
/docs # one-page website (GitHub Pages)
/rdf # DCAT-AP metadata and RDF files
/scripts # data processing scripts


## Methodology

The project combines multiple open datasets published by international organizations
(e.g. FAO, Copernicus, World Bank) to produce an aggregated mash-up dataset at regional
level. The workflow includes data selection, quality assessment, legal and ethical
analysis, and publication as Linked Open Data.

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
