# plazi-multipanel-figures
Subdivide multipanel figures and complex captions to individual image / caption pairs

## About

The [Plazi](https://plazi.org) project has accumulated a large repository of figures and figure captions from species description publications, which are available via zenodo in the [Biodiversity Literature Repository](https://zenodo.org/communities/biosyslit/). However, figure captions typically consist of multiple subcaptions, each of which describes a different subfigure. The figures are images consisting of multiple subfigures. In theory, these high-quality biodiversity specimen images with associated textual description (of species, and often occurrence location and/or notable traits shown in the (sub)figure) could be very valuable for CLIP model training for biology, but for this to be effective, we need pairs of text descriptions that describe only one image (as a subfigure), and one subfigure image.

## Aim

To produce a dataset of individual images with associated description suitable for CLIP-model training

## Context

Part of the [Image Datapalooza](https://github.com/Imageomics/Image-Datapalooza-2023) event held at Ohio State University, Columbus, 14-17th August 2023.

## Data

- [Data in zenodo filtered by type = image](https://zenodo.org/communities/biosyslit/search?type=image)
- [Turtle RDF format data from github](https://github.com/plazi/treatments-rdf)

## Tasks

- Subdivision of complex captions into subfigure captions, with an identifier to correlate these to image segment
- Segmentation of multi-panel images to one image per subfigure

## Process

TBC

## Contacts

- [Jim Balhoff](https://github.com/balhoff)
- [Hilmar Lapp](https://github.com/hlapp)
- [Nicky Nicolson](https://github.com/nickynicolson)
