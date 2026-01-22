# URI strategy

This document records the project's URI strategy (persistent identifiers and patterns) — part of the Technical analysis (section 7).

Base URI
---------

Use the project's GitHub Pages base as the canonical root for published RDF and linked data:

https://arinee01.github.io/madagascar-drought-open-data/

Datasets
--------

Canonical dataset descriptions live under the `/rdf` space. Example:

https://arinee01.github.io/madagascar-drought-open-data/rdf/datasets.ttl#dataset-mashup

Or as a relative pattern:

…/rdf/datasets.ttl#dataset-mashup

Distributions (downloadable files)
-------------------------------

Point to download URLs hosted under `/data/processed` (or a stable data host):

https://arinee01.github.io/madagascar-drought-open-data/data/processed/mashup.csv

Regions and identifiers
-----------------------

Use a stable id pattern for administrative regions. Example (ADM1 = region level 1):

https://arinee01.github.io/madagascar-drought-open-data/id/region/{ADM1_CODE}

Example: `https://arinee01.github.io/madagascar-drought-open-data/id/region/MG-01`

Guidelines and notes
--------------------

- Use HTTP URIs that resolve to human-readable HTML and machine-readable RDF (content negotiation) when possible.
- Prefer fragment identifiers (`#dataset-mashup`) in TTL files for dataset records bundled in a single Turtle file.
- Keep data download links under `/data/processed/` and avoid including volatile query parameters in canonical URIs.
- Document any changes to the URI scheme in this file and avoid reusing identifiers for different resources.

Relation to Technical analysis (section 7)
-----------------------------------------

This URI strategy belongs in the Technical analysis section as it describes how resources will be identified, published and dereferenced for both humans and machines.

If you'd like, I can:
- add a small `.htaccess` or GitHub Pages configuration guidance for content negotiation, or
- generate example RDF pages for `id/region/{ADM1_CODE}` and a dereferenceable HTML representation.
