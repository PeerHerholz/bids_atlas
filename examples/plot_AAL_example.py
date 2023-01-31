# -*- coding: utf-8 -*-
"""
Fetching BIDS-Atlas compliant atlases
=====================================
This example demonstrates how to use :mod:`bids_atlas.datasets` to fetch
atlases that confirm to BIDS-Atlas.
"""

###############################################################################
# Much of the functionality of the ``bids_atlas`` toolbox relies on downloading
# commonly used publicly available atlases. Each atlas has its own ``function``, with certain
# arguments being shared across all of them.
# This specifically refers to the ``target space`` and ``resolution`` the given ``atlas`` should
# be obtained in. 
#
# Here we show how download a few atlases, using the respective ``functions`` and ``arguments``.
#
# First of all, we are going to import ``bids_atlas`` ``dataset`` ``module``, as this will give us
# access to all respective functions.

from bids_atlas import datasets

###############################################################################
# Lets start with the ``AAL`` ``atlas``. In order to obtain it in a ``BIDS-Atlas`` compliant manner, we only need to
# use the respective function, called ``get_AAL``. If we run it without specifying any arguments, it will be provided
# in the current directory and default specifications, ie 2mm resolution. The function will return a dictionary with 
# the paths to atlas image, .tsv and .json files.

AAL_atlas = datasets.get_AAL()

###############################################################################
# Now the respective files can be accessed via their ``keys``. The path to the ``atlas image`` can be obtained via

AAL_atlas['AtlasImage']

###############################################################################
# and thus easily be loaded, plotted, or utilized within an analysis.

from nilearn.plotting import plot_roi

plot_roi(AAL_atlas['AtlasImage'], draw_cross=False, cmap='Set2')

###############################################################################
# The .tsv and .json files contain important information and metadata concerning the atlas. The former entails a DataFrame
# indicating the indices of the atlas and details thereof. 

import pandas as pd

pd.read_csv(AAL_atlas['AtlasTSV'])

###############################################################################
# The latter comprises the atlas' metadata following ``BIDS`` specifications.

import json

with open(AAL_atlas['AtlasJson'], 'r') as AAL_atlas_json:
    AAL_atlas_json_load = json.load(AAL_atlas_json)
    AAL_atlas_json_load = json.dumps(AAL_atlas_json_load, indent=4)
    print(AAL_atlas_json_load)
