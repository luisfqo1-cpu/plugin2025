# plugin2025

A [napari](https://napari.org) plugin for ROI-based quantification of fluorescence microscopy images: segmentation, per-cell and per-pixel antibody intensity, colocalization and polygon export. It includes the `imagetools` helper functions it is built on.

This is the newer, extended version of the plugin used in [ACSL4-iso2-image-analysis](https://github.com/luisfqo1-cpu/ACSL4-iso2-image-analysis). That repository keeps the manuscript version as an installable package (`imagetools`, shown in napari as *ImageTools*).

## Contents

| Path | What it is |
|---|---|
| `__init__.py`, `_reader.py`, `_widget.py`, `napari.yaml` | The napari plugin (Python package `plugin`): file reader, widgets and plugin manifest |
| `_tests/` | pytest tests for the reader and widgets |
| `imagetools/util.py` | Helper functions: ROI cropping, StarDist/Cellpose segmentation (also chunked for large images), per-cell measurements, image registration and BrainGlobe atlas slice matching |
| `imagetools/nd2_npy_converter.py` | Converts every `.nd2` file in a folder (recursively) to `.npy` |

## Reader

Opens `.npy`, `.nd2` (Nikon) and `.czi` (Zeiss) files as image layers.

## Widgets

**Display and preprocessing**

| Widget | What it does |
|---|---|
| Adjust Contrast | Sets an image's contrast limits to `[0, max]` |
| Set Contrast | Sets contrast limits to chosen `min` / `max` values (default 1050–4095) |
| Slider | Interactive threshold: shows the first image above the slider value as a new layer |
| Denoise | Wavelet denoising (`skimage.restoration.denoise_wavelet`), added as a new layer |
| Register Images | Aligns a target image to a reference by cross-correlating binarised crops inside the drawn ROIs. Adds the shifted image and saves it as `<name>_shifted.npy` |

**Segmentation and ROIs**

| Widget | What it does |
|---|---|
| Stardist Segmentation | Segments cells inside rectangular ROIs with StarDist or Cellpose (`method` = `stardist` / `cellpose`) |
| Twochannel Segmentation | The same, on one plane (`segment`) of a multi-channel image |
| Shapes2Labels | Converts a Shapes layer into a Labels layer |
| polygons | Exports the drawn polygons with `mouse_id`, `slice_id`, `condition` and `antibody` taken from the first image's name (`<mouse>_<slice>_<condition>_<antibody>`). This is the input format of `circularity.py` in ACSL4-iso2-image-analysis |

**Quantification**

| Widget | What it does |
|---|---|
| Calculate Target Rate | For each ROI, the fraction of reference cells (labels) overlapping the target signal by more than `coloc_thr` |
| Calculate Target Intensity | For each ROI, the mean (or another `regionprops` property) of the target image over the reference cells |
| Antibody Intensity | Splits the reference cells in each ROI into target-positive and target-negative, then measures antibody intensity in each group. `expand` grows the labels by that many pixels first |
| Antibody pixel Intensity | Mean, SD and all pixel values of the target image inside each ROI |
| antibody_pixel_intensity_twochannel | Pixel values inside every polygon of every Shapes layer, for one plane (`segment`) of a multi-channel image, with polygon coordinates |
| Timeseries pixel Intensity | Mean ROI intensity for every frame of a 3-D (time × y × x) image |
| colocalization | Per-cell pixel values of every open image inside each ROI, for colocalization analysis. Reads mouse, slide, slice and region from fields 4–7 of the label layer's name (split on `_`), and the channel from field 8 of each image name |
| zebrafish | Red (channel 0) and green (channel 2) pixel values inside each ROI of the first image |
| Draw Contours | Draws ROI outlines filled with the rates from a saved CSV |

Measurement widgets save their results as `<save>.csv` in the folder napari was started from. Running a widget again with the same name merges the new rows into the existing file.

## Requirements

`numpy`, `scipy`, `scikit-image`, `pandas`, `matplotlib`, `tqdm`, `shapely`, `psutil`, `dask`, `napari`, `magicgui`, `qtpy`, `opencv-python`, `nd2`, `czifile`, plus `cellpose` (< 4), `stardist` and `csbdeep` for segmentation and `bg-atlasapi` for atlas matching.

## Installation

This repository holds the plugin's source files but no packaging files (`setup.cfg` / `pyproject.toml`) yet, so it can't be installed with `pip` directly. For a ready-to-install version, use the `imagetools` package in [ACSL4-iso2-image-analysis](https://github.com/luisfqo1-cpu/ACSL4-iso2-image-analysis/tree/main/imagetools).

## License

MIT License. See [`LICENSE`](LICENSE).
