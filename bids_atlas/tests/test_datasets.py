import os
from ..datasets import get_AAL
from pathlib import Path


def download_AAL():

    # test if all files are downloaded

    AAL_atlas = get_AAL()
    actual_files = sorted(os.listdir(Path(AAL_atlas['AtlasImage']).parents[0]))
    expected_files = ['atlas-AAL_res-2_dseg.json',
                      'atlas-AAL_res-2_dseg.nii.gz',
                      'atlas-AAL_res-2_dseg.tsv',
                      ]
    assert actual_files == expected_files
