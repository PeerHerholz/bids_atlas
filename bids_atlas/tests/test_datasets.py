import os
from ..datasets import get_AAL

def test_download_HBN():

    # test if all files are downloaded

    aal_files = get_AAL()
    actual_files = sorted(os.listdir(aal_files))
    expected_files = ['atlas-AAL_res-2_dseg.json',
                      'atlas-AAL_res-2_dseg.nii.gz',
                      'atlas-AAL_res-2_dseg.tsv',
                      ]
    assert actual_files == expected_files
