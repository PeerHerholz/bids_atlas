import os
from ..datasets import get_AAL, get_Destrieux, get_HarvardOxford, get_Talairach, get_Juelich, get_Schaefer
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


def test_download_HarvardOxford():

    # test if all files are downloaded

    HarvardOxford_atlas = get_HarvardOxford()
    actual_files = sorted(os.listdir(Path(HarvardOxford_atlas['AtlasImage']).parents[0]))
    expected_files = ['atlas-HarvardOxford_res-2_desc-thr25_dseg.json',
                      'atlas-HarvardOxford_res-2_desc-thr25_dseg.nii.gz',
                      'atlas-HarvardOxford_res-2_desc-thr25_dseg.tsv',
                      ]
    assert actual_files == expected_files


def test_download_Talairach():

    # test if all files are downloaded

    Talairach_atlas = get_Talairach()
    actual_files = sorted(os.listdir(Path(Talairach_atlas['AtlasImage']).parents[0]))
    expected_files = ['atlas-Talairach_res-2_desc-gyrus_dseg.json',
                      'atlas-Talairach_res-2_desc-gyrus_dseg.nii.gz',
                      'atlas-Talairach_res-2_desc-gyrus_dseg.tsv',
                      ]
    assert actual_files == expected_files


def test_download_Juelich():

    # test if all files are downloaded

    Juelich_atlas = get_Juelich()
    actual_files = sorted(os.listdir(Path(Juelich_atlas['AtlasImage']).parents[0]))
    expected_files = ['atlas-Juelich_res-2_desc-thr25_dseg.json',
                      'atlas-Juelich_res-2_desc-thr25_dseg.nii.gz',
                      'atlas-Juelich_res-2_desc-thr25_dseg.tsv',
                      ]
    assert actual_files == expected_files


def test_download_Schaefer():

    # test if all files are downloaded

    Schaefer_atlas = get_Schaefer()
    actual_files = sorted(os.listdir(Path(Schaefer_atlas['AtlasImage']).parents[0]))
    expected_files = ['atlas-Schaefer100_res-2_probseg.json',
                      'atlas-Schaefer100_res-2_probseg.nii.gz',
                      'atlas-Schaefer100_res-2_probseg.tsv',
                      ]
    assert actual_files == expected_files
