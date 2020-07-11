---
title: Manual
parent: home
---

## Execute the Jupyter notebooks

This course content is provided as Jupyter notebooks that require to be powered by a Jupyter server with Python3 kernel.

### Install Jupyter and other dependencies

#### First install Anaconda

Anaconda is easy to install but the installer is quite heavy to download because it contains a lot of components.
In particular, it is shipped with:

- [Jupyter](http://jupyter.org/)
- The [Spyder](https://github.com/spyder-ide/spyder) IDE
- Scipy libraries: Numpy, Pandas, etc.

For a detailed installation of Anaconda and its extensions on Windows, Mac or Linux, follow the instructions <a href="pages/anaconda.md"><img src="fig/anaconda.png" style="display:inline" alt="Anaconda logo" width="100px"></a>.

#### Finalize installation with conda

From the project root directory, type:

```bash
conda install --file requirements.txt
```

### Run a Jupyter notebook

#### Start a Jupyter server

- Either from Anaconda graphical interface
- or from the command line interface from the project root directory:

```bash
jupyter-notebook
```

#### Execute a notebook

- Download and extract the archive of the first chapter
- In the Jupyter, open the `.ipynb` file
- Execute the notebook using the menu "Cell > Run All"

## Optional: build and publish

If you want be able to build and publish this course material, follow these [instructions](pages/build.md).
