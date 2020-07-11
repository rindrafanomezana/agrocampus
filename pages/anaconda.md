---
title: Anaconda
parent: manual.md
---

## Download

Download <a href="https://www.anaconda.com/download"><img src="fig/anaconda.png" style="display:inline" alt="Anaconda logo" width="100px"></a> for Python 3.X for your operating system and install it.

On Linux, open *Terminal* application and type:

```bash
cd Downloads
bash ./Anaconda*.sh
```

## Install the *Exercise2* extension for Jupyter

Use the Command line interface on:

- Windows : *Start menu > All programms > Anaconda3 (64bits) > Anaconda Prompt*
- Linux or Mac : open *Terminal*

Type:

```bash
conda install -c conda-forge jupyter_contrib_nbextensions
jupyter nbextension enable exercise2/main
```
