---
title: Manual
parent: home
---

## Execute the Jupyter notebooks

This course content is provided as Jupyter notebooks that require to be powered by a Jupyter server with Python3 kernel.

### Install Jupyter and other dependencies

#### First install Miniconda

For a detailed installation on Windows, Mac or Linux, follow the instructions <a href="pages/miniconda.md"><img src="images/conda_logo.svg" style="display:inline" alt="Conda logo" width="100px"></a>.

#### Finalize installation with conda

From the project root directory, type:

```bash
conda env update --file environment.yml
```

### Run a Jupyter notebook

#### Start a Jupyter server

- From the command line interface (anaconda prompt on windows)  from the project root directory:

```bash
jupyter-notebook
```

#### Execute a notebook

- Download and extract the archive of the first chapter
- In the Jupyter, open the `.ipynb` file
- Execute the notebook using the menu "Cell > Run All"
