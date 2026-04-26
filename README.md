# 🌍 GIS Programming & Spatial Analysis Portfolio

> **Yilin Pu** · GIS Programming and Customization · University of Southern California

[![ArcGIS Pro](https://img.shields.io/badge/ArcGIS%20Pro-ModelBuilder%20%7C%20Toolbox-blue?logo=esri)](https://pro.arcgis.com/)
[![Python](https://img.shields.io/badge/Python-ArcPy%20%7C%20GeoPandas-yellow?logo=python)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)](https://jupyter.org)
[![GeoPandas](https://img.shields.io/badge/GeoPandas-Spatial%20Analysis-green)](https://geopandas.org)

---

## About This Portfolio

This portfolio showcases **5 geospatial projects** completed in a graduate-level GIS programming study. Each project demonstrates a progressive command of spatial analysis tools — from visual ModelBuilder workflows through Python scripting with ArcPy, to fully open-source spatial data science with GeoPandas and JupyterLab.

Projects span real-world themes including **earthquake preparedness**, **cultural access equity**, **urban land use**, **economic inequality**, and **energy pricing** — across study areas in Los Angeles, California, San Diego, Antwerp, and the entire United States.

---

## 🗂️ Project Index

| # | Project | Tools | Scale | Theme |
|---|---------|-------|-------|-------|
| 1 | [🏫 Earthquake Risk for LA Schools](#project-1) | ArcGIS Pro · ModelBuilder | LA County | Public Safety |
| 2 | [🎭 Cultural Centers Mapping with ArcPy](#project-2) | Python · ArcPy | Los Angeles | Cultural Access |
| 3 | [🐼 Spatial Analysis with GeoPandas](#project-3) | Python · GeoPandas · Jupyter | Antwerp + San Diego | Urban Planning |
| 4 | [💰 CA Income Distribution Toolbox](#project-4) | Python · ArcPy · Pandas | California | Socioeconomics |
| 5 | [⛽ U.S. Gasoline Price Toolbox](#project-5) | Python · ArcPy · Pandas | United States | Energy Economics |

---

## Project Summaries

### Project 1
## 🏫 Earthquake Risk Analysis for Schools in LA County
**[→ View Repository](./project1-earthquake-risk-la/)**

Identifies K–12 schools in Los Angeles County most at risk from earthquake faults, using USGS fault slip-rate data to prioritize schools for seismic retrofit funding.

- **Method:** ArcGIS Pro ModelBuilder — Merge, Clip, Buffer (1 mile), Intersect
- **Output:** Risk-coded map of at-risk schools (color-coded by USGS slip rate)
- **Impact:** Data-driven prioritization tool for earthquake preparedness planning

**Skills:** `ModelBuilder` · `Buffer Analysis` · `Spatial Intersect` · `Risk Classification`

---

### Project 2
## 🎭 Mapping LA Cultural Centers & Theaters with ArcPy
**[→ View Repository](./project2-cultural-centers-arcpy/)**

Collects geographic coordinates for 29 DCA Cultural Centers and Theaters in Los Angeles, then automates the conversion from CSV to point shapefile using a Python/ArcPy script.

- **Method:** Python script using `arcpy.management.XYTableToPoint()`
- **Data:** 29 facilities with X/Y/Z coordinates, manually collected via Google Earth
- **Output:** Validated point shapefile and distribution map of LA cultural facilities

**Skills:** `ArcPy` · `CSV → Shapefile` · `Coordinate Systems` · `Python Automation`

---

### Project 3
## 🐼 Spatial Analysis with GeoPandas — Antwerp & San Diego
**[→ View Repository](./project3-geopandas-spatial-analysis/)**

Open-source spatial analysis using Python, GeoPandas, and JupyterLab — producing 5 multi-layer maps including buffer analysis, proximity calculations, and zoning visualizations.

- **Method:** GeoPandas `read_file()`, `.buffer()`, `.distance()`, `matplotlib` rendering
- **Data:** Land use, zoning, street centerlines, recreation centers (San Diego); land use & addresses (Antwerp)
- **Output:** 5 multi-layer maps including green area buffers and proximity heatmaps

**Skills:** `GeoPandas` · `JupyterLab` · `Buffer Analysis` · `Proximity Analysis` · `Multi-layer Mapping`

---

### Project 4
## 💰 California Income Distribution — Custom ArcGIS Python Toolbox
**[→ View Repository](./project4-income-distribution-toolbox/)**

Builds a reusable custom Python Toolbox (`.pyt`) for ArcGIS Pro that classifies median family income using IQR-based quantile statistics and joins the results to California county boundaries.

- **Method:** Custom `.pyt` toolbox with `pandas.DataFrame.quantile()`, `arcpy.AddJoin_management()`, `CopyFeatures_management()`
- **Data:** Median family income by CA county (Excel) + CA county boundaries (ESRI GDB)
- **Output:** 6-class choropleth map of income distribution across 58 California counties

**Skills:** `ArcGIS Toolbox (.pyt)` · `Quantile Classification` · `Table Joins` · `Choropleth Mapping`

---

### Project 5
## ⛽ U.S. Gasoline Price Distribution — Extended Toolbox
**[→ View Repository](./project5-gasoline-price-toolbox/)**

Extends the Project 4 toolbox to national scale, mapping retail gasoline prices across all U.S. states with data cleaning for missing territories and the same IQR classification engine.

- **Method:** Adapted `.pyt` toolbox — data cleaning, quantile classification, state boundary join
- **Data:** Retail gasoline prices by state (Statista 2022) + U.S. state boundaries (Census)
- **Output:** National choropleth map of gasoline price distribution across 50 U.S. states

**Skills:** `Toolbox Reuse` · `Data Cleaning` · `National-Scale Mapping` · `Quantile Statistics`

---

## 🛠️ Technical Skills Demonstrated

### GIS Platforms
- **ArcGIS Pro** — ModelBuilder, Python Toolbox, Geodatabases, Symbology
- **QGIS** (open source alternative, comparable workflows)
- **JupyterLab + Anaconda** — open-source geospatial environment

### Python Libraries
| Library | Usage |
|---------|-------|
| `arcpy` | ArcGIS Pro automation, geoprocessing, toolbox scripting |
| `geopandas` | Open-source spatial data I/O, analysis, mapping |
| `pandas` | Tabular data manipulation, quantile statistics |
| `matplotlib` | Multi-layer map rendering |
| `earthpy` | Reprojection utilities |

### Spatial Analysis Techniques
- Proximity & buffer analysis
- Spatial intersect and clip operations
- Feature selection by attribute and location
- Table joins (Excel/CSV ↔ geodatabase)
- Quantile-based data classification
- Choropleth and risk-level mapping
- Coordinate system management (WGS 1984, NAD 1983, EPSG codes)

### Data Formats Worked With
`Shapefile (.shp)` · `File Geodatabase (.gdb)` · `CSV` · `Excel (.xlsx)` · `GeoJSON` · `Jupyter Notebook (.ipynb)` · `ArcGIS Toolbox (.pyt)` · `ArcGIS Project (.aprx)`

---

## 📈 Progression Map

```
Project 1          Project 2          Project 3          Project 4 → 5
ModelBuilder   →   ArcPy Script   →   GeoPandas +    →   Custom ArcGIS
(Visual GUI)       (Automation)       JupyterLab         Python Toolbox
                                      (Open Source)       (Reusable Tool)
```

---

## 📬 Contact

**Yilin Pu**
- 🎓 MS in Spatial Data Science
- 📍 University of Southern California
---

*All projects completed as part of study in GIS Programming and Customization, instructed by Professor Andrew Marx.*
