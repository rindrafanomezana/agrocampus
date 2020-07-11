# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,../src//py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.5.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + [markdown] slideshow={"slide_type": "slide"}
# # Installation with conda
#
# - **Conda is already installed on workstations.**
#
# - Steps below are for students who prefer to use their personal laptops

# + [markdown] slideshow={"slide_type": "slide"}
# ##  Install [Anaconda](https://www.anaconda.com/downloads) (large) or [Miniconda](https://conda.io/miniconda.html) (small)
#
#

# + [markdown] slideshow={"slide_type": "slide"}
# ##  Open a terminal (Linux/MacOSX) or a conda prompt (Windows)

# + [markdown] slideshow={"slide_type": "slide"}
# ## Create a new conda environment from file
#
# ```bash
# # # cd big-data
# conda env create
# ```
#
# [Conda envs documentation](https://conda.io/docs/using/envs.html).

# + [markdown] slideshow={"slide_type": "slide"}
# ## Activate the new environment (for all students)
#
# Activating the conda environment will change your shell’s prompt to show what virtual environment you’re using, and modify the environment so that running python will get you that particular version and installation of Python. 
# <pre>
# $ conda activate big-data
# (big-data) $ python
# Python 3.6.2 (default, Jul 17 2017, 16:44:45) 
# [GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> quit()
# </pre>
#
#
#
# **You must do this everytime you open a new terminal**
# -

# ## Create the kernel for jupyter
#
# ```bash
# python -m ipykernel install --user \
#        --name big-data
# ```
