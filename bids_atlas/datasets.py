import os
import seedir as sd
from templateflow import api as tflow

from bids_atlas.utils import check_output_path, resample_atlas_target, generate_json_sidecar_file

import pandas as pd

import nibabel as nb
from nilearn import datasets


# define function to get the AAL atlas
def get_AAL(target_space=None, resolution=None, path=None):
    """
    Download the AAL atlas in specified target space and resolution,
    providing it in a BIDS-Atlas compliant manner.

    Parameters
    ----------
    target_space : string
        Target space the atlas should be provided in. If None, the atlas
        will be provided in MNI152NLin6Asym. Default = None.
    resolution : string
        Resolution the atlas should be provided in. If None, the atlas
        will be provided in 2mm resolution. Default = None.
    path : string
        Path where the atlas will be saved. If None, the file will be saved
        in the current working directory. Default = None.

    Returns
    -------
    dict : Dictionary
        A Dictionary containing the paths to the atlas image, tsv and json files.

    Examples
    --------
    Download the AAL atlas to the current directory.

    >>> get_AAL()

    Download the atlas to a specific path, e.g. the user's Desktop
    and indicate a resolution.

    >>> get_AAL(resolution=1, path='/home/user/Desktop')
    """

    # check input arguments and if not provided assign default
    # target_space will be actively supported soon
    if target_space is None:
        target_space = 'MNI152NLin6Asym'
    else:
        print('Spatial transformations of atlases will soon be supported.')
        print('At the moment only MNI152NLin6Asym is available.')
        target_space = 'MNI152NLin6Asym'
    if resolution is None:
        resolution = 2
    if path is None:
        path = os.curdir

    # get the AAL atlas as provided by nilearn
    aal_atlas = datasets.fetch_atlas_aal(version='SPM12')

    # get the target/reference as provided by templateflow
    target = tflow.get(target_space, desc='brain', resolution=resolution, suffix='T1w',
                       extension='nii.gz')

    # resample the atlas to the indicated resolution if needed
    aal_atlas_nii = resample_atlas_target(aal_atlas.maps, target)

    # generate the output path
    outpath = check_output_path(path, atlas='AAL')

    # generate the filename pattern
    atlas_file_name = 'atlas-AAL_res-%s_dseg.nii.gz' % resolution

    # save the atlas at the indicated path with the generated filename
    nb.save(aal_atlas_nii, os.path.join(outpath, atlas_file_name))

    # create the atlas .tsv file
    aal_df = pd.DataFrame({'Index': aal_atlas.indices,
                           'Label': aal_atlas.labels,
                           'Hemisphere': ['L' if '_L' in label else 'R' if "_R" in label else 'NA' for label in aal_atlas.labels]
                           })
    
    # save the atlas .tsv file
    aal_df.to_csv(os.path.join(outpath, atlas_file_name.replace('.nii.gz', '.tsv')),
                  index=False)

    # generate the atlas json sidecar file
    generate_json_sidecar_file('AAL',
                               os.path.join(outpath, atlas_file_name.replace('.nii.gz', '.json')))

    # print a message indicating what files were downloaded where
    print('The following files were downloaded at %s' % outpath)
    sd.seedir(outpath)

    aal_atlas_dict = {'AtlasImage': os.path.join(outpath, atlas_file_name),
                      'AtlasTSV': os.path.join(outpath, atlas_file_name.replace('.nii.gz', '.tsv')),
                      'AtlasJson': os.path.join(outpath, atlas_file_name.replace('.nii.gz', '.json'))}

    return aal_atlas_dict
