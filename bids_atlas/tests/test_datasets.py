import os
from ..datasets import get_AAL, get_Destrieux
from pathlib import Path


def test_download_AAL():

    # test if all files are downloaded

    AAL_atlas = get_AAL()
    actual_files = sorted(os.listdir(Path(AAL_atlas['AtlasImage']).parents[0]))
    expected_files = ['atlas-AAL_res-2_dseg.json',
                      'atlas-AAL_res-2_dseg.nii.gz',
                      'atlas-AAL_res-2_dseg.tsv',
                      ]
    assert actual_files == expected_files


def test_download_Destrieux():

    # test if all files are downloaded

    Destrieux_atlas = get_Destrieux()
    actual_files = sorted(os.listdir(Path(Destrieux_atlas['AtlasImage']).parents[0]))
    expected_files = ['atlas-Destrieux_res-2_dseg.json',
                      'atlas-Destrieux_res-2_dseg.nii.gz',
                      'atlas-Destrieux_res-2_dseg.tsv',
                      ]
    assert actual_files == expected_files
